"""
Type annotations for route53-recovery-control-config service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_route53_recovery_control_config.client import Route53RecoveryControlConfigClient

    session = get_session()
    async with session.create_client("route53-recovery-control-config") as client:
        client: Route53RecoveryControlConfigClient
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .type_defs import (
    AssertionRuleUpdateTypeDef,
    CreateClusterResponseTypeDef,
    CreateControlPanelResponseTypeDef,
    CreateRoutingControlResponseTypeDef,
    CreateSafetyRuleResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeControlPanelResponseTypeDef,
    DescribeRoutingControlResponseTypeDef,
    DescribeSafetyRuleResponseTypeDef,
    GatingRuleUpdateTypeDef,
    ListAssociatedRoute53HealthChecksResponseTypeDef,
    ListClustersResponseTypeDef,
    ListControlPanelsResponseTypeDef,
    ListRoutingControlsResponseTypeDef,
    ListSafetyRulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NewAssertionRuleTypeDef,
    NewGatingRuleTypeDef,
    UpdateControlPanelResponseTypeDef,
    UpdateRoutingControlResponseTypeDef,
    UpdateSafetyRuleResponseTypeDef,
)
from .waiter import (
    ClusterCreatedWaiter,
    ClusterDeletedWaiter,
    ControlPanelCreatedWaiter,
    ControlPanelDeletedWaiter,
    RoutingControlCreatedWaiter,
    RoutingControlDeletedWaiter,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53RecoveryControlConfigClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class Route53RecoveryControlConfigClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53RecoveryControlConfigClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#can_paginate)
        """

    async def create_cluster(
        self, *, ClusterName: str, ClientToken: str = ..., Tags: Mapping[str, str] = ...
    ) -> CreateClusterResponseTypeDef:
        """
        Create a new cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.create_cluster)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#create_cluster)
        """

    async def create_control_panel(
        self,
        *,
        ClusterArn: str,
        ControlPanelName: str,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateControlPanelResponseTypeDef:
        """
        Creates a new control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.create_control_panel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#create_control_panel)
        """

    async def create_routing_control(
        self,
        *,
        ClusterArn: str,
        RoutingControlName: str,
        ClientToken: str = ...,
        ControlPanelArn: str = ...
    ) -> CreateRoutingControlResponseTypeDef:
        """
        Creates a new routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.create_routing_control)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#create_routing_control)
        """

    async def create_safety_rule(
        self,
        *,
        AssertionRule: "NewAssertionRuleTypeDef" = ...,
        ClientToken: str = ...,
        GatingRule: "NewGatingRuleTypeDef" = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateSafetyRuleResponseTypeDef:
        """
        Creates a safety rule in a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.create_safety_rule)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#create_safety_rule)
        """

    async def delete_cluster(self, *, ClusterArn: str) -> Dict[str, Any]:
        """
        Delete a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.delete_cluster)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#delete_cluster)
        """

    async def delete_control_panel(self, *, ControlPanelArn: str) -> Dict[str, Any]:
        """
        Deletes a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.delete_control_panel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#delete_control_panel)
        """

    async def delete_routing_control(self, *, RoutingControlArn: str) -> Dict[str, Any]:
        """
        Deletes a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.delete_routing_control)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#delete_routing_control)
        """

    async def delete_safety_rule(self, *, SafetyRuleArn: str) -> Dict[str, Any]:
        """
        Deletes a safety rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.delete_safety_rule)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#delete_safety_rule)
        """

    async def describe_cluster(self, *, ClusterArn: str) -> DescribeClusterResponseTypeDef:
        """
        Display the details about a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.describe_cluster)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#describe_cluster)
        """

    async def describe_control_panel(
        self, *, ControlPanelArn: str
    ) -> DescribeControlPanelResponseTypeDef:
        """
        Displays details about a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.describe_control_panel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#describe_control_panel)
        """

    async def describe_routing_control(
        self, *, RoutingControlArn: str
    ) -> DescribeRoutingControlResponseTypeDef:
        """
        Displays details about a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.describe_routing_control)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#describe_routing_control)
        """

    async def describe_safety_rule(
        self, *, SafetyRuleArn: str
    ) -> DescribeSafetyRuleResponseTypeDef:
        """
        Returns information about a safety rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.describe_safety_rule)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#describe_safety_rule)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#generate_presigned_url)
        """

    async def list_associated_route53_health_checks(
        self, *, RoutingControlArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListAssociatedRoute53HealthChecksResponseTypeDef:
        """
        Returns an array of all Amazon Route 53 health checks associated with a specific
        routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_associated_route53_health_checks)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#list_associated_route53_health_checks)
        """

    async def list_clusters(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListClustersResponseTypeDef:
        """
        Returns an array of all the clusters in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_clusters)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#list_clusters)
        """

    async def list_control_panels(
        self, *, ClusterArn: str = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> ListControlPanelsResponseTypeDef:
        """
        Returns an array of control panels in an account or in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_control_panels)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#list_control_panels)
        """

    async def list_routing_controls(
        self, *, ControlPanelArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListRoutingControlsResponseTypeDef:
        """
        Returns an array of routing controls for a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_routing_controls)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#list_routing_controls)
        """

    async def list_safety_rules(
        self, *, ControlPanelArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListSafetyRulesResponseTypeDef:
        """
        List the safety rules (the assertion rules and gating rules) that you've defined
        for the routing controls in a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_safety_rules)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#list_safety_rules)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#list_tags_for_resource)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.tag_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.untag_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#untag_resource)
        """

    async def update_control_panel(
        self, *, ControlPanelArn: str, ControlPanelName: str
    ) -> UpdateControlPanelResponseTypeDef:
        """
        Updates a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.update_control_panel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#update_control_panel)
        """

    async def update_routing_control(
        self, *, RoutingControlArn: str, RoutingControlName: str
    ) -> UpdateRoutingControlResponseTypeDef:
        """
        Updates a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.update_routing_control)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#update_routing_control)
        """

    async def update_safety_rule(
        self,
        *,
        AssertionRuleUpdate: "AssertionRuleUpdateTypeDef" = ...,
        GatingRuleUpdate: "GatingRuleUpdateTypeDef" = ...
    ) -> UpdateSafetyRuleResponseTypeDef:
        """
        Update a safety rule (an assertion rule or gating rule).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.update_safety_rule)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#update_safety_rule)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_created"]) -> ClusterCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["control_panel_created"]
    ) -> ControlPanelCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["control_panel_deleted"]
    ) -> ControlPanelDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["routing_control_created"]
    ) -> RoutingControlCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["routing_control_deleted"]
    ) -> RoutingControlDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html#get_waiter)
        """

    async def __aenter__(self) -> "Route53RecoveryControlConfigClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/client.html)
        """
