"""
Type annotations for wafv2 service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_wafv2.client import WAFV2Client

    session = get_session()
    async with session.create_client("wafv2") as client:
        client: WAFV2Client
    ```
"""
from datetime import datetime
from typing import Any, Dict, Mapping, Sequence, Type, Union

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import IPAddressVersionType, ResourceTypeType, ScopeType
from .type_defs import (
    CaptchaConfigTypeDef,
    CheckCapacityResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateRegexPatternSetResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    CreateWebACLResponseTypeDef,
    CustomResponseBodyTypeDef,
    DefaultActionTypeDef,
    DeleteFirewallManagerRuleGroupsResponseTypeDef,
    DescribeManagedRuleGroupResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetManagedRuleSetResponseTypeDef,
    GetPermissionPolicyResponseTypeDef,
    GetRateBasedStatementManagedKeysResponseTypeDef,
    GetRegexPatternSetResponseTypeDef,
    GetRuleGroupResponseTypeDef,
    GetSampledRequestsResponseTypeDef,
    GetWebACLForResourceResponseTypeDef,
    GetWebACLResponseTypeDef,
    ListAvailableManagedRuleGroupsResponseTypeDef,
    ListAvailableManagedRuleGroupVersionsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListManagedRuleSetsResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListResourcesForWebACLResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebACLsResponseTypeDef,
    LoggingConfigurationTypeDef,
    PutLoggingConfigurationResponseTypeDef,
    PutManagedRuleSetVersionsResponseTypeDef,
    RegexTypeDef,
    RuleTypeDef,
    TagTypeDef,
    TimeWindowTypeDef,
    UpdateIPSetResponseTypeDef,
    UpdateManagedRuleSetVersionExpiryDateResponseTypeDef,
    UpdateRegexPatternSetResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateWebACLResponseTypeDef,
    VersionToPublishTypeDef,
    VisibilityConfigTypeDef,
)

__all__ = ("WAFV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    WAFAssociatedItemException: Type[BotocoreClientError]
    WAFDuplicateItemException: Type[BotocoreClientError]
    WAFExpiredManagedRuleGroupVersionException: Type[BotocoreClientError]
    WAFInternalErrorException: Type[BotocoreClientError]
    WAFInvalidOperationException: Type[BotocoreClientError]
    WAFInvalidParameterException: Type[BotocoreClientError]
    WAFInvalidPermissionPolicyException: Type[BotocoreClientError]
    WAFInvalidResourceException: Type[BotocoreClientError]
    WAFLimitsExceededException: Type[BotocoreClientError]
    WAFLogDestinationPermissionIssueException: Type[BotocoreClientError]
    WAFNonexistentItemException: Type[BotocoreClientError]
    WAFOptimisticLockException: Type[BotocoreClientError]
    WAFServiceLinkedRoleErrorException: Type[BotocoreClientError]
    WAFSubscriptionNotFoundException: Type[BotocoreClientError]
    WAFTagOperationException: Type[BotocoreClientError]
    WAFTagOperationInternalErrorException: Type[BotocoreClientError]
    WAFUnavailableEntityException: Type[BotocoreClientError]


class WAFV2Client(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WAFV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#exceptions)
        """

    async def associate_web_acl(self, *, WebACLArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        Associates a web ACL with a regional application resource, to protect the
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.associate_web_acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#associate_web_acl)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#can_paginate)
        """

    async def check_capacity(
        self, *, Scope: ScopeType, Rules: Sequence["RuleTypeDef"]
    ) -> CheckCapacityResponseTypeDef:
        """
        Returns the web ACL capacity unit (WCU) requirements for a specified scope and
        set of rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.check_capacity)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#check_capacity)
        """

    async def create_ip_set(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        IPAddressVersion: IPAddressVersionType,
        Addresses: Sequence[str],
        Description: str = ...,
        Tags: Sequence["TagTypeDef"] = ...
    ) -> CreateIPSetResponseTypeDef:
        """
        Creates an  IPSet , which you use to identify web requests that originate from
        specific IP addresses or ranges of IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.create_ip_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#create_ip_set)
        """

    async def create_regex_pattern_set(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        RegularExpressionList: Sequence["RegexTypeDef"],
        Description: str = ...,
        Tags: Sequence["TagTypeDef"] = ...
    ) -> CreateRegexPatternSetResponseTypeDef:
        """
        Creates a  RegexPatternSet , which you reference in a
        RegexPatternSetReferenceStatement , to have WAF inspect a web request component
        for the specified patterns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.create_regex_pattern_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#create_regex_pattern_set)
        """

    async def create_rule_group(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Capacity: int,
        VisibilityConfig: "VisibilityConfigTypeDef",
        Description: str = ...,
        Rules: Sequence["RuleTypeDef"] = ...,
        Tags: Sequence["TagTypeDef"] = ...,
        CustomResponseBodies: Mapping[str, "CustomResponseBodyTypeDef"] = ...
    ) -> CreateRuleGroupResponseTypeDef:
        """
        Creates a  RuleGroup per the specifications provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.create_rule_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#create_rule_group)
        """

    async def create_web_acl(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        DefaultAction: "DefaultActionTypeDef",
        VisibilityConfig: "VisibilityConfigTypeDef",
        Description: str = ...,
        Rules: Sequence["RuleTypeDef"] = ...,
        Tags: Sequence["TagTypeDef"] = ...,
        CustomResponseBodies: Mapping[str, "CustomResponseBodyTypeDef"] = ...,
        CaptchaConfig: "CaptchaConfigTypeDef" = ...
    ) -> CreateWebACLResponseTypeDef:
        """
        Creates a  WebACL per the specifications provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.create_web_acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#create_web_acl)
        """

    async def delete_firewall_manager_rule_groups(
        self, *, WebACLArn: str, WebACLLockToken: str
    ) -> DeleteFirewallManagerRuleGroupsResponseTypeDef:
        """
        Deletes all rule groups that are managed by Firewall Manager for the specified
        web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_firewall_manager_rule_groups)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#delete_firewall_manager_rule_groups)
        """

    async def delete_ip_set(
        self, *, Name: str, Scope: ScopeType, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified  IPSet .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_ip_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#delete_ip_set)
        """

    async def delete_logging_configuration(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Deletes the  LoggingConfiguration from the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_logging_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#delete_logging_configuration)
        """

    async def delete_permission_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Permanently deletes an IAM policy from the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_permission_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#delete_permission_policy)
        """

    async def delete_regex_pattern_set(
        self, *, Name: str, Scope: ScopeType, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified  RegexPatternSet .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_regex_pattern_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#delete_regex_pattern_set)
        """

    async def delete_rule_group(
        self, *, Name: str, Scope: ScopeType, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified  RuleGroup .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_rule_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#delete_rule_group)
        """

    async def delete_web_acl(
        self, *, Name: str, Scope: ScopeType, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified  WebACL .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.delete_web_acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#delete_web_acl)
        """

    async def describe_managed_rule_group(
        self, *, VendorName: str, Name: str, Scope: ScopeType, VersionName: str = ...
    ) -> DescribeManagedRuleGroupResponseTypeDef:
        """
        Provides high-level information for a managed rule group, including descriptions
        of the rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.describe_managed_rule_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#describe_managed_rule_group)
        """

    async def disassociate_web_acl(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Disassociates a web ACL from a regional application resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.disassociate_web_acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#disassociate_web_acl)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#generate_presigned_url)
        """

    async def get_ip_set(self, *, Name: str, Scope: ScopeType, Id: str) -> GetIPSetResponseTypeDef:
        """
        Retrieves the specified  IPSet .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_ip_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_ip_set)
        """

    async def get_logging_configuration(
        self, *, ResourceArn: str
    ) -> GetLoggingConfigurationResponseTypeDef:
        """
        Returns the  LoggingConfiguration for the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_logging_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_logging_configuration)
        """

    async def get_managed_rule_set(
        self, *, Name: str, Scope: ScopeType, Id: str
    ) -> GetManagedRuleSetResponseTypeDef:
        """
        Retrieves the specified managed rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_managed_rule_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_managed_rule_set)
        """

    async def get_permission_policy(
        self, *, ResourceArn: str
    ) -> GetPermissionPolicyResponseTypeDef:
        """
        Returns the IAM policy that is attached to the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_permission_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_permission_policy)
        """

    async def get_rate_based_statement_managed_keys(
        self,
        *,
        Scope: ScopeType,
        WebACLName: str,
        WebACLId: str,
        RuleName: str,
        RuleGroupRuleName: str = ...
    ) -> GetRateBasedStatementManagedKeysResponseTypeDef:
        """
        Retrieves the keys that are currently blocked by a rate-based rule instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_rate_based_statement_managed_keys)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_rate_based_statement_managed_keys)
        """

    async def get_regex_pattern_set(
        self, *, Name: str, Scope: ScopeType, Id: str
    ) -> GetRegexPatternSetResponseTypeDef:
        """
        Retrieves the specified  RegexPatternSet .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_regex_pattern_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_regex_pattern_set)
        """

    async def get_rule_group(
        self, *, Name: str = ..., Scope: ScopeType = ..., Id: str = ..., ARN: str = ...
    ) -> GetRuleGroupResponseTypeDef:
        """
        Retrieves the specified  RuleGroup .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_rule_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_rule_group)
        """

    async def get_sampled_requests(
        self,
        *,
        WebAclArn: str,
        RuleMetricName: str,
        Scope: ScopeType,
        TimeWindow: "TimeWindowTypeDef",
        MaxItems: int
    ) -> GetSampledRequestsResponseTypeDef:
        """
        Gets detailed information about a specified number of requests--a sample--that
        WAF randomly selects from among the first 5,000 requests that your Amazon Web
        Services resource received during a time range that you choose.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_sampled_requests)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_sampled_requests)
        """

    async def get_web_acl(
        self, *, Name: str, Scope: ScopeType, Id: str
    ) -> GetWebACLResponseTypeDef:
        """
        Retrieves the specified  WebACL .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_web_acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_web_acl)
        """

    async def get_web_acl_for_resource(
        self, *, ResourceArn: str
    ) -> GetWebACLForResourceResponseTypeDef:
        """
        Retrieves the  WebACL for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.get_web_acl_for_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#get_web_acl_for_resource)
        """

    async def list_available_managed_rule_group_versions(
        self,
        *,
        VendorName: str,
        Name: str,
        Scope: ScopeType,
        NextMarker: str = ...,
        Limit: int = ...
    ) -> ListAvailableManagedRuleGroupVersionsResponseTypeDef:
        """
        Returns a list of the available versions for the specified managed rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_group_versions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_available_managed_rule_group_versions)
        """

    async def list_available_managed_rule_groups(
        self, *, Scope: ScopeType, NextMarker: str = ..., Limit: int = ...
    ) -> ListAvailableManagedRuleGroupsResponseTypeDef:
        """
        Retrieves an array of managed rule groups that are available for you to use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_groups)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_available_managed_rule_groups)
        """

    async def list_ip_sets(
        self, *, Scope: ScopeType, NextMarker: str = ..., Limit: int = ...
    ) -> ListIPSetsResponseTypeDef:
        """
        Retrieves an array of  IPSetSummary objects for the IP sets that you manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_ip_sets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_ip_sets)
        """

    async def list_logging_configurations(
        self, *, Scope: ScopeType, NextMarker: str = ..., Limit: int = ...
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        Retrieves an array of your  LoggingConfiguration objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_logging_configurations)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_logging_configurations)
        """

    async def list_managed_rule_sets(
        self, *, Scope: ScopeType, NextMarker: str = ..., Limit: int = ...
    ) -> ListManagedRuleSetsResponseTypeDef:
        """
        Retrieves the managed rule sets that you own.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_managed_rule_sets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_managed_rule_sets)
        """

    async def list_regex_pattern_sets(
        self, *, Scope: ScopeType, NextMarker: str = ..., Limit: int = ...
    ) -> ListRegexPatternSetsResponseTypeDef:
        """
        Retrieves an array of  RegexPatternSetSummary objects for the regex pattern sets
        that you manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_regex_pattern_sets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_regex_pattern_sets)
        """

    async def list_resources_for_web_acl(
        self, *, WebACLArn: str, ResourceType: ResourceTypeType = ...
    ) -> ListResourcesForWebACLResponseTypeDef:
        """
        Retrieves an array of the Amazon Resource Names (ARNs) for the regional
        resources that are associated with the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_resources_for_web_acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_resources_for_web_acl)
        """

    async def list_rule_groups(
        self, *, Scope: ScopeType, NextMarker: str = ..., Limit: int = ...
    ) -> ListRuleGroupsResponseTypeDef:
        """
        Retrieves an array of  RuleGroupSummary objects for the rule groups that you
        manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_rule_groups)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_rule_groups)
        """

    async def list_tags_for_resource(
        self, *, ResourceARN: str, NextMarker: str = ..., Limit: int = ...
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the  TagInfoForResource for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_tags_for_resource)
        """

    async def list_web_acls(
        self, *, Scope: ScopeType, NextMarker: str = ..., Limit: int = ...
    ) -> ListWebACLsResponseTypeDef:
        """
        Retrieves an array of  WebACLSummary objects for the web ACLs that you manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.list_web_acls)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#list_web_acls)
        """

    async def put_logging_configuration(
        self, *, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutLoggingConfigurationResponseTypeDef:
        """
        Enables the specified  LoggingConfiguration , to start logging from a web ACL,
        according to the configuration provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.put_logging_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#put_logging_configuration)
        """

    async def put_managed_rule_set_versions(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        LockToken: str,
        RecommendedVersion: str = ...,
        VersionsToPublish: Mapping[str, "VersionToPublishTypeDef"] = ...
    ) -> PutManagedRuleSetVersionsResponseTypeDef:
        """
        Defines the versions of your managed rule set that you are offering to the
        customers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.put_managed_rule_set_versions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#put_managed_rule_set_versions)
        """

    async def put_permission_policy(self, *, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        Attaches an IAM policy to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.put_permission_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#put_permission_policy)
        """

    async def tag_resource(
        self, *, ResourceARN: str, Tags: Sequence["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Associates tags with the specified Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.tag_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#tag_resource)
        """

    async def untag_resource(self, *, ResourceARN: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Disassociates tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.untag_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#untag_resource)
        """

    async def update_ip_set(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        Addresses: Sequence[str],
        LockToken: str,
        Description: str = ...
    ) -> UpdateIPSetResponseTypeDef:
        """
        Updates the specified  IPSet .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_ip_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#update_ip_set)
        """

    async def update_managed_rule_set_version_expiry_date(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        LockToken: str,
        VersionToExpire: str,
        ExpiryTimestamp: Union[datetime, str]
    ) -> UpdateManagedRuleSetVersionExpiryDateResponseTypeDef:
        """
        Updates the expiration information for your managed rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_managed_rule_set_version_expiry_date)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#update_managed_rule_set_version_expiry_date)
        """

    async def update_regex_pattern_set(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        RegularExpressionList: Sequence["RegexTypeDef"],
        LockToken: str,
        Description: str = ...
    ) -> UpdateRegexPatternSetResponseTypeDef:
        """
        Updates the specified  RegexPatternSet .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_regex_pattern_set)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#update_regex_pattern_set)
        """

    async def update_rule_group(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        VisibilityConfig: "VisibilityConfigTypeDef",
        LockToken: str,
        Description: str = ...,
        Rules: Sequence["RuleTypeDef"] = ...,
        CustomResponseBodies: Mapping[str, "CustomResponseBodyTypeDef"] = ...
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        Updates the specified  RuleGroup .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_rule_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#update_rule_group)
        """

    async def update_web_acl(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        DefaultAction: "DefaultActionTypeDef",
        VisibilityConfig: "VisibilityConfigTypeDef",
        LockToken: str,
        Description: str = ...,
        Rules: Sequence["RuleTypeDef"] = ...,
        CustomResponseBodies: Mapping[str, "CustomResponseBodyTypeDef"] = ...,
        CaptchaConfig: "CaptchaConfigTypeDef" = ...
    ) -> UpdateWebACLResponseTypeDef:
        """
        Updates the specified  WebACL .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client.update_web_acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html#update_web_acl)
        """

    async def __aenter__(self) -> "WAFV2Client":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_wafv2/client.html)
        """
