"""
Type annotations for redshift-data service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_redshift_data.client import RedshiftDataAPIServiceClient

    session = get_session()
    async with session.create_client("redshift-data") as client:
        client: RedshiftDataAPIServiceClient
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import StatusStringType
from .paginator import (
    DescribeTablePaginator,
    GetStatementResultPaginator,
    ListDatabasesPaginator,
    ListSchemasPaginator,
    ListStatementsPaginator,
    ListTablesPaginator,
)
from .type_defs import (
    BatchExecuteStatementOutputTypeDef,
    CancelStatementResponseTypeDef,
    DescribeStatementResponseTypeDef,
    DescribeTableResponseTypeDef,
    ExecuteStatementOutputTypeDef,
    GetStatementResultResponseTypeDef,
    ListDatabasesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListStatementsResponseTypeDef,
    ListTablesResponseTypeDef,
    SqlParameterTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RedshiftDataAPIServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ActiveStatementsExceededException: Type[BotocoreClientError]
    BatchExecuteStatementException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DatabaseConnectionException: Type[BotocoreClientError]
    ExecuteStatementException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class RedshiftDataAPIServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RedshiftDataAPIServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#exceptions)
        """

    async def batch_execute_statement(
        self,
        *,
        Database: str,
        Sqls: Sequence[str],
        ClusterIdentifier: str = ...,
        DbUser: str = ...,
        SecretArn: str = ...,
        StatementName: str = ...,
        WithEvent: bool = ...
    ) -> BatchExecuteStatementOutputTypeDef:
        """
        Runs one or more SQL statements, which can be data manipulation language (DML)
        or data definition language (DDL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.batch_execute_statement)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#batch_execute_statement)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#can_paginate)
        """

    async def cancel_statement(self, *, Id: str) -> CancelStatementResponseTypeDef:
        """
        Cancels a running query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.cancel_statement)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#cancel_statement)
        """

    async def describe_statement(self, *, Id: str) -> DescribeStatementResponseTypeDef:
        """
        Describes the details about a specific instance when a query was run by the
        Amazon Redshift Data API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_statement)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#describe_statement)
        """

    async def describe_table(
        self,
        *,
        Database: str,
        ClusterIdentifier: str = ...,
        ConnectedDatabase: str = ...,
        DbUser: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        Schema: str = ...,
        SecretArn: str = ...,
        Table: str = ...
    ) -> DescribeTableResponseTypeDef:
        """
        Describes the detailed information about a table from metadata in the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_table)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#describe_table)
        """

    async def execute_statement(
        self,
        *,
        Database: str,
        Sql: str,
        ClusterIdentifier: str = ...,
        DbUser: str = ...,
        Parameters: Sequence["SqlParameterTypeDef"] = ...,
        SecretArn: str = ...,
        StatementName: str = ...,
        WithEvent: bool = ...
    ) -> ExecuteStatementOutputTypeDef:
        """
        Runs an SQL statement, which can be data manipulation language (DML) or data
        definition language (DDL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.execute_statement)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#execute_statement)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#generate_presigned_url)
        """

    async def get_statement_result(
        self, *, Id: str, NextToken: str = ...
    ) -> GetStatementResultResponseTypeDef:
        """
        Fetches the temporarily cached result of an SQL statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_statement_result)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#get_statement_result)
        """

    async def list_databases(
        self,
        *,
        Database: str,
        ClusterIdentifier: str = ...,
        DbUser: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        SecretArn: str = ...
    ) -> ListDatabasesResponseTypeDef:
        """
        List the databases in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_databases)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#list_databases)
        """

    async def list_schemas(
        self,
        *,
        Database: str,
        ClusterIdentifier: str = ...,
        ConnectedDatabase: str = ...,
        DbUser: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        SchemaPattern: str = ...,
        SecretArn: str = ...
    ) -> ListSchemasResponseTypeDef:
        """
        Lists the schemas in a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_schemas)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#list_schemas)
        """

    async def list_statements(
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        RoleLevel: bool = ...,
        StatementName: str = ...,
        Status: StatusStringType = ...
    ) -> ListStatementsResponseTypeDef:
        """
        List of SQL statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_statements)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#list_statements)
        """

    async def list_tables(
        self,
        *,
        Database: str,
        ClusterIdentifier: str = ...,
        ConnectedDatabase: str = ...,
        DbUser: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        SchemaPattern: str = ...,
        SecretArn: str = ...,
        TablePattern: str = ...
    ) -> ListTablesResponseTypeDef:
        """
        List the tables in a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_tables)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#list_tables)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_table"]) -> DescribeTablePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_statement_result"]
    ) -> GetStatementResultPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_statements"]) -> ListStatementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html#get_paginator)
        """

    async def __aenter__(self) -> "RedshiftDataAPIServiceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/client.html)
        """
