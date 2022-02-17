# OTHER IMPORTS
from typing import Optional, List

# ROS IMPORTS
from std_msgs.msg import UInt64, String

# EAGERx IMPORTS
from eagerx.bridges.test.bridge import TestBridgeNode
from eagerx.core.entities import Object, EngineNode, SpaceConverter, EngineState, BaseConverter
from eagerx.core.specs import ObjectSpec, AgnosticSpec, SpecificSpec
from eagerx.core.graph_engine import EngineGraph
import eagerx.core.register as register


class Arm(Object):
    @staticmethod
    @register.sensors(N6=UInt64, N7=UInt64)
    @register.actuators(N8=String, ref_vel=UInt64)
    @register.simstates(N9=UInt64, N10=UInt64)
    @register.agnostic_params(
        position=[0, 0, 0],
        orientation=[0, 0, 0],
        arg_rate=15,
        low=None,
        string=None,
        test_string=None,
        test_list=None,
    )
    def agnostic(spec: AgnosticSpec):
        """Agnostic definition of the Arm object"""
        # Set state properties: space_converters
        space_rosuint64 = SpaceConverter.make("Space_RosUInt64", [0], [100], dtype="uint64")
        spec.set_space_converter(space_rosuint64, "sensors", "N6")
        spec.set_parameter("rate", "$(default arg_rate)", "sensors", "N6")
        spec.set_space_converter(space_rosuint64, "sensors", "N7")
        spec.set_parameter("rate", 2, "sensors", "N7")

        # Set actuator properties: space_converters
        space_rosstring = SpaceConverter.make("Space_RosString", [0], [100], dtype="uint64")
        spec.set_space_converter(space_rosstring, "actuators", "N8")
        spec.set_parameter("rate", "$(default arg_rate)", "actuators", "N8")
        spec.set_space_converter(space_rosuint64, "actuators", "ref_vel")
        spec.set_parameter("rate", 1, "actuators", "ref_vel")

        # Set state properties: space_converters
        spec.set_space_converter(space_rosuint64, "states", "N9")
        spec.set_space_converter(space_rosuint64, "states", "N10")

        # Test AgnosticSpec
        spec.set_parameter("rate", spec.get_parameter("rate", "actuators", "N8"), "actuators", "N8")
        spec.set_parameters(spec.get_parameters("actuators", "N8"), "actuators", "N8")

    @staticmethod
    @register.spec("Arm", Object)
    def spec(
        spec: ObjectSpec,
        name: str,
        sensors: Optional[List[str]] = None,
        actuators: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        position: Optional[List[str]] = None,
        orientation: Optional[List[str]] = None,
        string: Optional[str] = "test_arg",
        test_string: Optional[str] = "$(default string)",
        test_list: Optional[str] = "$(default orientation)",
        low: Optional[int] = 0,
    ):
        """Object spec of Arm"""
        # Performs all the steps to fill-in the params with registered info about all functions.
        spec.initialize(Arm)

        # Set default
        sensors = sensors if sensors else ["N6", "N7"]
        actuators = actuators if actuators else ["ref_vel"]
        states = states if states else ["N9", "N10"]
        position = position if position else [0, 0, 0]
        orientation = orientation if orientation else [0, 0, 0]

        # Modify default node params
        # Only allow changes to the agnostic params (rates, windows, (space)converters, etc...
        default = dict(name=name, sensors=sensors, actuators=actuators, states=states)
        spec.set_parameters(default)

        # Add custom params
        params = dict(
            position=position,
            orientation=orientation,
            string=string,
            test_string=test_string,
            test_list=test_list,
            low=low,
            arg_rate=15,
        )
        spec.set_parameters(params)

        spec.set_parameters(params, level="default")

        # Add bridge implementation
        Arm.test_bridge(spec)

        # Test ObjectSpec
        c = "sensors"
        cn = "N6"
        spec.set_parameters(spec.get_parameters(c, cn, level="agnostic"), c, cn, level="agnostic")
        spec.set_parameter("name", spec.get_parameter("name", level="default"), level="default")
        spec.set_parameters(spec.get_parameters(level="default"), level="default")
        return spec

    @classmethod
    @register.bridge(TestBridgeNode)  # This decorator pre-initializes bridge implementation with default object_params
    def test_bridge(cls, spec: SpecificSpec, graph: EngineGraph):
        """Engine-specific implementation of the Arm with the test bridge."""
        # Set object arguments
        object_params = dict(req_arg="TEST", xacro="$(find some_package)/urdf/arm.urdf.xacro")
        spec.set_parameters(object_params)

        # Create simstates
        spec.set_state(EngineState.make("TestEngineState", test_arg="arg_N9"), "N9")

        # Create sensor engine nodes
        N6 = EngineNode.make(
            "TestSensor",
            "N6",
            rate=1,
            process=2,
            inputs=["tick", "in_1"],
            outputs=["out_1"],
            states=["state_1"],
            test_arg="$(default req_arg)",
        )
        N7 = EngineNode.make(
            "TestSensor",
            "N7",
            rate=1,
            process=2,
            inputs=["tick", "in_1"],
            outputs=["out_1"],
            states=[],
            test_arg="$(default test_string)",
        )

        # Create actuator engine nodes
        N8 = EngineNode.make(
            "TestActuator",
            "N8",
            rate=1,
            process=2,
            inputs=["tick", "in_2", "in_3"],
            outputs=["out_1"],
            test_arg="$(default test_string)",
            color="green",
        )
        ref_vel = EngineNode.make(
            "TestActuator",
            "ref_vel",
            rate=1,
            process=2,
            inputs=["tick", "in_1", "in_2"],
            outputs=["out_1"],
            test_arg="$(default test_string)",
            color="green",
        )

        # Test SpecificSpec:
        _ = spec.__str__()
        spec.set_parameters(spec.get_parameters())
        spec.set_state_parameter("test_arg", "test2", "N9")

        # Test EngineGraph: Add/remove sensor
        graph.add(N6)
        _ = graph.__str__()
        graph.add_component("N6", "outputs", "out_2")
        graph.remove_component("N6", "outputs", "out_2")
        graph.connect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.remove("N6")

        # Test EngineGraph: Add/remove actuator
        graph.add(N8)
        graph.connect(actuator="N8", target=("N8", "inputs", "in_3"))
        graph.remove("N8")

        # Test EngineGraph: Remove component
        graph.add(N6)
        graph.connect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.rename("N6", "N6_new")  # Test renaming
        graph.remove_component("N6_new", "outputs", "out_1")
        graph.add_component("N6_new", "outputs", "out_1")
        graph.remove("N6_new")

        # Test EngineGraph: Remove component
        graph.add(N8)
        graph.connect(actuator="N8", target=("N8", "inputs", "in_3"))
        graph.remove_component("N8", "inputs", "in_3")
        graph.add_component("N8", "inputs", "in_3")
        graph.remove("N8")

        # Test EngineGraph: parameters
        graph.add([N6, N8])
        graph.connect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.connect(actuator="N8", target=("N8", "inputs", "in_3"))
        graph.get_parameter("converter", "N6", "outputs", "out_1")
        graph.set_parameter("test_arg", "NEW_ARG", "N6")
        graph.get_parameter("converter", actuator="N8")
        graph.get_parameter("converter", sensor="N6")
        graph.get_parameters(sensor="N6")
        graph.get_parameters(actuator="N8")
        graph.get_parameters("N6", "outputs", "out_1")
        graph.remove(["N6", "N8"])

        # Add nodes to graph and connect them to actuators/sensors
        graph.add([N6, N7, N8, ref_vel])

        # Connect sensors & actuators to engine nodes
        graph.connect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.disconnect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.connect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.connect(source=("N7", "outputs", "out_1"), sensor="N7")
        graph.connect(actuator="N8", target=("N8", "inputs", "in_3"))
        graph.connect(actuator="ref_vel", target=("ref_vel", "inputs", "in_1"))

        # Interconnect engine nodes
        id = BaseConverter.make("Identity")
        graph.connect(
            source=("N8", "outputs", "out_1"),
            target=("N7", "inputs", "in_1"),
            skip=True,
        )
        graph.connect(source=("N6", "outputs", "out_1"), target=("N8", "inputs", "in_2"), window=1, converter=id)
        graph.connect(source=("N6", "outputs", "out_1"), target=("ref_vel", "inputs", "in_2"), delay=0.0)

        # Connect simnode with external address (cannot be actuator or sensor)
        graph.connect(
            address="$(ns env_name)/nonreactive_input_topic",
            target=("N6", "inputs", "in_1"),
            external_rate=20,
        )
        graph.disconnect(target=("N6", "inputs", "in_1"))
        graph.connect(
            address="$(ns env_name)/nonreactive_input_topic",
            target=("N6", "inputs", "in_1"),
            external_rate=20,
        )

        # Test EngineGraph: Test acyclic check
        import matplotlib.pyplot as plt

        plt.ion()

        graph.add_component("N8", "inputs", "in_1")
        graph.connect(source=("N7", "outputs", "out_1"), target=("N8", "inputs", "in_1"))
        graph.disconnect(source=("N8", "outputs", "out_1"), target=("N7", "inputs", "in_1"))
        graph.connect(source=("N8", "outputs", "out_1"), target=("N7", "inputs", "in_1"))
        try:
            graph.is_valid(plot=True)
        except AssertionError as e:
            if "Algebraic" in e.args[0]:
                pass
            else:
                raise
        # Reconnect
        graph.remove_component("N8", "inputs", "in_1")
        graph.disconnect(source=("N8", "outputs", "out_1"), target=("N7", "inputs", "in_1"))
        graph.connect(source=("N8", "outputs", "out_1"), target=("N7", "inputs", "in_1"), skip=True)


class Viper(Arm):
    @staticmethod
    @register.spec("Viper", Object)
    def spec(
        spec: ObjectSpec,
        name: str,
        sensors: Optional[List[str]] = None,
        actuators: Optional[List[str]] = None,
        states: Optional[List[str]] = None,
        position: Optional[List[float]] = None,
        orientation: Optional[List[float]] = None,
        string: Optional[str] = "test_arg",
        test_string: Optional[str] = "$(default string)",
        test_list: Optional[str] = "$(default orientation)",
        low: Optional[int] = 0,
    ):
        """Object spec of Viper"""
        # Performs all the steps to fill-in the params with registered info about all functions.
        spec.initialize(Viper)

        # Set default
        sensors = sensors if sensors else ["N6", "N7"]
        actuators = actuators if actuators else ["ref_vel"]
        states = states if states else ["N9", "N10"]
        position = position if position else [0, 0, 0]
        orientation = orientation if orientation else [0, 0, 0]

        # Modify default agnostic params
        # Only allow changes to the agnostic params (rates, windows, (space)converters, etc...
        default = dict(name=name, sensors=sensors, actuators=actuators, states=states)
        spec.set_parameters(default, level="default")

        # Add custom agnostic params
        params = dict(
            position=position,
            orientation=orientation,
            string=string,
            test_string=test_string,
            test_list=test_list,
            low=low,
            arg_rate=15,
        )
        spec.set_parameters(params, level="default")

        # Add bridge implementation
        Viper.test_bridge(spec)
        return spec

    @classmethod
    @register.bridge(TestBridgeNode)  # This decorator pre-initializes bridge implementation with default object_params
    def test_bridge(cls, spec: SpecificSpec, graph: EngineGraph):
        """Engine-specific implementation of the Viper with the test bridge."""
        # Set object arguments
        object_params = dict(req_arg="TEST ARGUMENT", xacro="$(find some_package)/urdf/viper.urdf.xacro")
        spec.set_parameters(object_params)

        # Create simstates
        spec.set_state(EngineState.make("TestEngineState", test_arg="arg_N9"), "N9")
        # spec.set_state('N10', SimState.make('TestEngineState', test_arg='arg_N10'))

        # Create sensor engine nodes
        N6 = EngineNode.make(
            "TestSensor",
            "N6",
            rate=1,
            process=2,
            inputs=["tick", "in_1"],
            outputs=["out_1"],
            states=["state_1"],
            test_arg="$(default req_arg)",
        )
        N7 = EngineNode.make(
            "TestSensor",
            "N7",
            rate=1,
            process=2,
            inputs=["tick", "in_1"],
            outputs=["out_1"],
            states=[],
            test_arg="$(default test_string)",
        )

        # Create actuator engine nodes
        N8 = EngineNode.make(
            "TestActuator",
            "N8",
            rate=1,
            process=2,
            inputs=["tick", "in_2", "in_3"],
            outputs=["out_1"],
            test_arg="$(default test_string)",
            color="green",
        )
        ref_vel = EngineNode.make(
            "TestActuator",
            "ref_vel",
            rate=1,
            process=2,
            inputs=["tick", "in_1", "in_2"],
            outputs=["out_1"],
            test_arg="$(default test_string)",
            color="green",
        )

        # Add nodes to graph and connect them to actuators/sensors
        graph.add([N6, N7, N8, ref_vel])

        # Connect sensors & actuators to engine nodes
        graph.connect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.disconnect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.connect(source=("N6", "outputs", "out_1"), sensor="N6")
        graph.connect(source=("N7", "outputs", "out_1"), sensor="N7")
        graph.connect(actuator="N8", target=("N8", "inputs", "in_3"))
        graph.connect(actuator="ref_vel", target=("ref_vel", "inputs", "in_1"))

        # Interconnect engine nodes
        graph.connect(
            source=("N8", "outputs", "out_1"),
            target=("N7", "inputs", "in_1"),
            skip=True,
        )
        graph.connect(source=("N6", "outputs", "out_1"), target=("N8", "inputs", "in_2"))
        graph.connect(source=("N6", "outputs", "out_1"), target=("ref_vel", "inputs", "in_2"))

        # Connect simnode with external address (cannot be actuator or sensor)
        graph.connect(
            address="$(ns env_name)/nonreactive_input_topic",
            target=("N6", "inputs", "in_1"),
            external_rate=20,
        )
        graph.disconnect(target=("N6", "inputs", "in_1"))
        graph.connect(
            address="$(ns env_name)/nonreactive_input_topic",
            target=("N6", "inputs", "in_1"),
            external_rate=20,
        )
