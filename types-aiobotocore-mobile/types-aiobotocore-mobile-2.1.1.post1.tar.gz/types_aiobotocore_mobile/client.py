"""
Type annotations for mobile service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_mobile.client import MobileClient

    session = get_session()
    async with session.create_client("mobile") as client:
        client: MobileClient
    ```
"""
import sys
from typing import IO, Any, Dict, Mapping, Type, Union, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .literals import PlatformType
from .paginator import ListBundlesPaginator, ListProjectsPaginator
from .type_defs import (
    CreateProjectResultTypeDef,
    DeleteProjectResultTypeDef,
    DescribeBundleResultTypeDef,
    DescribeProjectResultTypeDef,
    ExportBundleResultTypeDef,
    ExportProjectResultTypeDef,
    ListBundlesResultTypeDef,
    ListProjectsResultTypeDef,
    UpdateProjectResultTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MobileClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccountActionRequiredException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class MobileClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MobileClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#can_paginate)
        """

    async def create_project(
        self,
        *,
        name: str = ...,
        region: str = ...,
        contents: Union[bytes, IO[bytes], StreamingBody] = ...,
        snapshotId: str = ...
    ) -> CreateProjectResultTypeDef:
        """
        Creates an AWS Mobile Hub project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.create_project)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#create_project)
        """

    async def delete_project(self, *, projectId: str) -> DeleteProjectResultTypeDef:
        """
        Delets a project in AWS Mobile Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.delete_project)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#delete_project)
        """

    async def describe_bundle(self, *, bundleId: str) -> DescribeBundleResultTypeDef:
        """
        Get the bundle details for the requested bundle id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.describe_bundle)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#describe_bundle)
        """

    async def describe_project(
        self, *, projectId: str, syncFromResources: bool = ...
    ) -> DescribeProjectResultTypeDef:
        """
        Gets details about a project in AWS Mobile Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.describe_project)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#describe_project)
        """

    async def export_bundle(
        self, *, bundleId: str, projectId: str = ..., platform: PlatformType = ...
    ) -> ExportBundleResultTypeDef:
        """
        Generates customized software development kit (SDK) and or tool packages used to
        integrate mobile web or mobile app clients with backend AWS resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.export_bundle)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#export_bundle)
        """

    async def export_project(self, *, projectId: str) -> ExportProjectResultTypeDef:
        """
        Exports project configuration to a snapshot which can be downloaded and shared.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.export_project)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#export_project)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#generate_presigned_url)
        """

    async def list_bundles(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListBundlesResultTypeDef:
        """
        List all available bundles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.list_bundles)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#list_bundles)
        """

    async def list_projects(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListProjectsResultTypeDef:
        """
        Lists projects in AWS Mobile Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.list_projects)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#list_projects)
        """

    async def update_project(
        self, *, projectId: str, contents: Union[bytes, IO[bytes], StreamingBody] = ...
    ) -> UpdateProjectResultTypeDef:
        """
        Update an existing project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.update_project)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#update_project)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_bundles"]) -> ListBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html#get_paginator)
        """

    async def __aenter__(self) -> "MobileClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/client.html)
        """
