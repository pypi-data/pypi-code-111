from __future__ import annotations

import time

from pylox.environment import Environment, EnvironmentLookupError
from pylox.errors import LoxError
from pylox.lox_types import LoxType, Number
from pylox.nodes import (
    Assignment,
    Binary,
    Block,
    Call,
    Expr,
    ExprStmt,
    For,
    FunctionDef,
    Grouping,
    If,
    Literal,
    Node,
    Print,
    Program,
    ReturnStmt,
    Stmt,
    Unary,
    VarDeclaration,
    Variable,
    While,
)
from pylox.tokens import TokenType
from pylox.utils import get_lox_type_name, is_lox_callable, is_truthy
from pylox.visitor import Visitor


class NativeClock:
    def __repr__(self) -> str:
        return "<native function 'clock'>"

    def call(self, _: Interpreter, __: list[LoxType]) -> Number:
        return time.time()

    def arity(self) -> int:
        return 0


def create_globals() -> Environment:
    globals = Environment()
    globals.define("clock", NativeClock())
    return globals


class Return(Exception):
    """Used to return a value from inside an executing function"""

    def __init__(self, value: LoxType) -> None:
        self.value = value


class LoxFunction:
    def __init__(self, declaration: FunctionDef, closure: Environment) -> None:
        self.declaration = declaration
        self.closure = closure

    def __repr__(self) -> str:
        function_name = self.declaration.name.string
        return f"<function {function_name!r}>"

    def arity(self) -> int:
        return len(self.declaration.parameters)

    def call(self, interpreter: Interpreter, arguments: list[LoxType]) -> LoxType:
        # Each function call creates a new local environment
        environment = Environment(self.closure)
        for parameter, argument in zip(self.declaration.parameters, arguments):
            # First, define the arguments
            environment.define(parameter.string, argument)

        # Then, run the code in the new context
        # TODO: there's similar code in visit_Block. Refactor?
        parent_enviroment = interpreter.environment
        interpreter.environment = environment

        try:
            for statement in self.declaration.body:
                interpreter.execute(statement)
        except Return as ret:
            return ret.value
        finally:
            interpreter.environment = parent_enviroment

        return None


class InterpreterError(LoxError):
    def __init__(self, message: str, node: Node) -> None:
        super().__init__(message, node.index)
        self.node = node


class Interpreter(Visitor[LoxType]):
    def __init__(self) -> None:
        self.globals = create_globals()
        self.environment = self.globals
        self.locals: dict[Expr, int] = {}

    def visit(self, node: Program | Block) -> None:
        for stmt in node.body:
            self.generic_visit(stmt)

    def resolve(self, expr: Expr, depth: int) -> None:
        self.locals[expr] = depth

    def execute(self, stmt: Stmt) -> None:
        self.generic_visit(stmt)

    def evaluate(self, expr: Expr) -> LoxType:
        return self.generic_visit(expr)

    def visit_Literal(self, literal: Literal) -> LoxType:
        return literal.value

    def visit_Unary(self, unary: Unary) -> LoxType:
        if unary.operator.token_type == TokenType.MINUS:
            right_value = self.evaluate(unary.right)
            if not isinstance(right_value, Number):
                raise InterpreterError(
                    f"Expected number for unary '-', got {right_value}",
                    unary,
                )

            return -right_value

        elif unary.operator.token_type == TokenType.BANG:
            right_value = self.evaluate(unary.right)
            if is_truthy(right_value):
                return False

            return True

        raise NotImplementedError(
            f"Unary {unary.operator.token_type.value!r} not supported"
        )

    def visit_Binary(self, binary: Binary) -> LoxType:
        """Note that we evaluate both sides before type checking."""
        left_value = self.evaluate(binary.left)

        # Short circuited operators: `and` and `or`, can return early
        if binary.operator.token_type == TokenType.OR and is_truthy(left_value):
            return left_value
        if binary.operator.token_type == TokenType.AND and not is_truthy(left_value):
            return left_value

        right_value = self.evaluate(binary.right)

        # If short circuits didn't return early, they'll return the right value
        if binary.operator.token_type in (TokenType.AND, TokenType.OR):
            return right_value

        if binary.operator.token_type == TokenType.EQUAL_EQUAL:
            return left_value == right_value
        if binary.operator.token_type == TokenType.BANG_EQUAL:
            return left_value != right_value

        if (
            isinstance(left_value, str)
            and isinstance(right_value, str)
            and binary.operator.token_type == TokenType.PLUS
        ):
            return left_value + right_value

        if isinstance(left_value, Number) and isinstance(right_value, Number):
            if binary.operator.token_type == TokenType.PLUS:
                return left_value + right_value
            if binary.operator.token_type == TokenType.MINUS:
                return left_value - right_value
            if binary.operator.token_type == TokenType.STAR:
                return left_value * right_value
            if binary.operator.token_type == TokenType.SLASH:
                # TODO: catch ZeroDivisionError
                return left_value / right_value
            if binary.operator.token_type == TokenType.PERCENT:
                return left_value % right_value

            if binary.operator.token_type == TokenType.GREATER:
                return left_value > right_value
            if binary.operator.token_type == TokenType.GREATER_EQUAL:
                return left_value >= right_value
            if binary.operator.token_type == TokenType.LESS:
                return left_value < right_value
            if binary.operator.token_type == TokenType.LESS_EQUAL:
                return left_value <= right_value

        raise InterpreterError(
            f"Unsupported types for {binary.operator.token_type.value!r}: "
            f"{get_lox_type_name(left_value)!r} and {get_lox_type_name(right_value)!r}",
            binary,
        )

    def visit_Grouping(self, grouping: Grouping) -> LoxType:
        return self.evaluate(grouping.expression)

    def visit_Print(self, print_stmt: Print) -> None:
        value = self.evaluate(print_stmt.value)
        if value is None:
            print("nil")
        elif value is True:
            print("true")
        elif value is False:
            print("false")
        else:
            print(value)

    def visit_ExprStmt(self, expr_stmt: ExprStmt) -> None:
        self.evaluate(expr_stmt.expression)

    def visit_VarDeclaration(self, var_decl: VarDeclaration) -> None:
        if var_decl.initializer is None:
            value = None
        else:
            value = self.evaluate(var_decl.initializer)

        variable = var_decl.name.string
        self.environment.define(variable, value)

    def visit_Variable(self, variable: Variable) -> LoxType:
        depth = self.locals.get(variable)
        if depth is not None:
            return self.environment.get_at(depth, variable.name.string)

        try:
            return self.globals.get(variable.name.string)
        except EnvironmentLookupError as exc:
            raise InterpreterError(exc.message, variable)

    def visit_Assignment(self, assignment: Assignment) -> LoxType:
        value = self.evaluate(assignment.value)
        variable = assignment.name.string

        depth = self.locals.get(assignment)
        if depth is not None:
            self.environment.assign_at(depth, variable, value)
            return value

        try:
            self.globals.assign(variable, value)
        except EnvironmentLookupError as exc:
            raise InterpreterError(exc.message, assignment)

        # Remember that assignment expressions return the assigned value
        return value

    def visit_Block(self, block: Block) -> None:
        own_environment = self.environment
        try:
            child_environment = Environment(self.environment)
            self.environment = child_environment
            self.visit(block)
        finally:
            self.environment = own_environment

    def visit_If(self, if_stmt: If) -> None:
        condition = self.evaluate(if_stmt.condition)
        if is_truthy(condition):
            self.execute(if_stmt.body)
        elif if_stmt.else_body is not None:
            self.execute(if_stmt.else_body)

    def visit_While(self, while_stmt: While) -> None:
        while is_truthy(self.evaluate(while_stmt.condition)):
            self.execute(while_stmt.body)

    def visit_For(self, for_stmt: For) -> None:
        if for_stmt.initializer is not None:
            self.execute(for_stmt.initializer)

        while for_stmt.condition is None or is_truthy(
            self.evaluate(for_stmt.condition)
        ):
            self.execute(for_stmt.body)
            if for_stmt.increment is not None:
                self.evaluate(for_stmt.increment)

    def visit_Call(self, call: Call) -> LoxType:
        function = self.evaluate(call.callee)

        # We will evaluate all arguments before checking if the function
        # is callable. This is done because that's what a programmer
        # would expect to happen. Seeing abc(xyz()), you'd expect xyz()
        # to finish before abc(...) is attempted.
        arguments: list[LoxType] = []
        for argument in call.arguments:
            arguments.append(self.evaluate(argument))

        if not is_lox_callable(function):
            object_type = get_lox_type_name(function)
            raise InterpreterError(f"{object_type} object is not callable", call)

        if function.arity() != len(arguments):
            expected = function.arity()
            got = len(arguments)
            raise InterpreterError(
                f"{function!r} expected {expected} arguments, got {got}", call
            )

        return function.call(self, arguments)

    def visit_FunctionDef(self, function_def: FunctionDef) -> None:
        function_object = LoxFunction(function_def, self.environment)
        self.environment.define(function_def.name.string, function_object)

    def visit_ReturnStmt(self, return_stmt: ReturnStmt) -> None:
        if return_stmt.value:
            return_value = self.evaluate(return_stmt.value)
        else:
            return_value = None

        raise Return(return_value)
