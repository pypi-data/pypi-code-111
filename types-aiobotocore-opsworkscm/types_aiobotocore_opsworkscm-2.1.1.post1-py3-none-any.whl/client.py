"""
Type annotations for opsworkscm service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_opsworkscm.client import OpsWorksCMClient

    session = get_session()
    async with session.create_client("opsworkscm") as client:
        client: OpsWorksCMClient
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateNodeResponseTypeDef,
    CreateBackupResponseTypeDef,
    CreateServerResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeNodeAssociationStatusResponseTypeDef,
    DescribeServersResponseTypeDef,
    DisassociateNodeResponseTypeDef,
    EngineAttributeTypeDef,
    ExportServerEngineAttributeResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RestoreServerResponseTypeDef,
    StartMaintenanceResponseTypeDef,
    TagTypeDef,
    UpdateServerEngineAttributesResponseTypeDef,
    UpdateServerResponseTypeDef,
)
from .waiter import NodeAssociatedWaiter

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OpsWorksCMClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class OpsWorksCMClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpsWorksCMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#exceptions)
        """

    async def associate_node(
        self,
        *,
        ServerName: str,
        NodeName: str,
        EngineAttributes: Sequence["EngineAttributeTypeDef"]
    ) -> AssociateNodeResponseTypeDef:
        """
        Associates a new node with the server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.associate_node)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#associate_node)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#can_paginate)
        """

    async def create_backup(
        self, *, ServerName: str, Description: str = ..., Tags: Sequence["TagTypeDef"] = ...
    ) -> CreateBackupResponseTypeDef:
        """
        Creates an application-level backup of a server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.create_backup)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#create_backup)
        """

    async def create_server(
        self,
        *,
        Engine: str,
        ServerName: str,
        InstanceProfileArn: str,
        InstanceType: str,
        ServiceRoleArn: str,
        AssociatePublicIpAddress: bool = ...,
        CustomDomain: str = ...,
        CustomCertificate: str = ...,
        CustomPrivateKey: str = ...,
        DisableAutomatedBackup: bool = ...,
        EngineModel: str = ...,
        EngineVersion: str = ...,
        EngineAttributes: Sequence["EngineAttributeTypeDef"] = ...,
        BackupRetentionCount: int = ...,
        KeyPair: str = ...,
        PreferredMaintenanceWindow: str = ...,
        PreferredBackupWindow: str = ...,
        SecurityGroupIds: Sequence[str] = ...,
        SubnetIds: Sequence[str] = ...,
        Tags: Sequence["TagTypeDef"] = ...,
        BackupId: str = ...
    ) -> CreateServerResponseTypeDef:
        """
        Creates and immedately starts a new server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.create_server)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#create_server)
        """

    async def delete_backup(self, *, BackupId: str) -> Dict[str, Any]:
        """
        Deletes a backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_backup)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#delete_backup)
        """

    async def delete_server(self, *, ServerName: str) -> Dict[str, Any]:
        """
        Deletes the server and the underlying AWS CloudFormation stacks (including the
        server's EC2 instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_server)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#delete_server)
        """

    async def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        Describes your OpsWorks-CM account attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_account_attributes)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#describe_account_attributes)
        """

    async def describe_backups(
        self,
        *,
        BackupId: str = ...,
        ServerName: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> DescribeBackupsResponseTypeDef:
        """
        Describes backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_backups)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#describe_backups)
        """

    async def describe_events(
        self, *, ServerName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeEventsResponseTypeDef:
        """
        Describes events for a specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_events)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#describe_events)
        """

    async def describe_node_association_status(
        self, *, NodeAssociationStatusToken: str, ServerName: str
    ) -> DescribeNodeAssociationStatusResponseTypeDef:
        """
        Returns the current status of an existing association or disassociation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_node_association_status)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#describe_node_association_status)
        """

    async def describe_servers(
        self, *, ServerName: str = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> DescribeServersResponseTypeDef:
        """
        Lists all configuration management servers that are identified with your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_servers)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#describe_servers)
        """

    async def disassociate_node(
        self,
        *,
        ServerName: str,
        NodeName: str,
        EngineAttributes: Sequence["EngineAttributeTypeDef"] = ...
    ) -> DisassociateNodeResponseTypeDef:
        """
        Disassociates a node from an AWS OpsWorks CM server, and removes the node from
        the server's managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.disassociate_node)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#disassociate_node)
        """

    async def export_server_engine_attribute(
        self,
        *,
        ExportAttributeName: str,
        ServerName: str,
        InputAttributes: Sequence["EngineAttributeTypeDef"] = ...
    ) -> ExportServerEngineAttributeResponseTypeDef:
        """
        Exports a specified server engine attribute as a base64-encoded string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.export_server_engine_attribute)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#export_server_engine_attribute)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#generate_presigned_url)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags that are applied to the specified AWS OpsWorks for Chef
        Automate or AWS OpsWorks for Puppet Enterprise servers or backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#list_tags_for_resource)
        """

    async def restore_server(
        self, *, BackupId: str, ServerName: str, InstanceType: str = ..., KeyPair: str = ...
    ) -> RestoreServerResponseTypeDef:
        """
        Restores a backup to a server that is in a `CONNECTION_LOST` , `HEALTHY` ,
        `RUNNING` , `UNHEALTHY` , or `TERMINATED` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.restore_server)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#restore_server)
        """

    async def start_maintenance(
        self, *, ServerName: str, EngineAttributes: Sequence["EngineAttributeTypeDef"] = ...
    ) -> StartMaintenanceResponseTypeDef:
        """
        Manually starts server maintenance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.start_maintenance)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#start_maintenance)
        """

    async def tag_resource(
        self, *, ResourceArn: str, Tags: Sequence["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Applies tags to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet
        Enterprise server, or to server backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.tag_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes specified tags from an AWS OpsWorks-CM server or backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.untag_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#untag_resource)
        """

    async def update_server(
        self,
        *,
        ServerName: str,
        DisableAutomatedBackup: bool = ...,
        BackupRetentionCount: int = ...,
        PreferredMaintenanceWindow: str = ...,
        PreferredBackupWindow: str = ...
    ) -> UpdateServerResponseTypeDef:
        """
        Updates settings for a server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#update_server)
        """

    async def update_server_engine_attributes(
        self, *, ServerName: str, AttributeName: str, AttributeValue: str = ...
    ) -> UpdateServerEngineAttributesResponseTypeDef:
        """
        Updates engine-specific attributes on a specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server_engine_attributes)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#update_server_engine_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_servers"]
    ) -> DescribeServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#get_paginator)
        """

    def get_waiter(self, waiter_name: Literal["node_associated"]) -> NodeAssociatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html#get_waiter)
        """

    async def __aenter__(self) -> "OpsWorksCMClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html#OpsWorksCM.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/client.html)
        """
