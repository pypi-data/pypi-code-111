"""
Type annotations for opensearch service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_opensearch.client import OpenSearchServiceClient

    session = get_session()
    async with session.create_client("opensearch") as client:
        client: OpenSearchServiceClient
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import EngineTypeType, LogTypeType, OpenSearchPartitionInstanceTypeType
from .type_defs import (
    AcceptInboundConnectionResponseTypeDef,
    AdvancedSecurityOptionsInputTypeDef,
    AssociatePackageResponseTypeDef,
    AutoTuneOptionsInputTypeDef,
    AutoTuneOptionsTypeDef,
    CancelServiceSoftwareUpdateResponseTypeDef,
    ClusterConfigTypeDef,
    CognitoOptionsTypeDef,
    CreateDomainResponseTypeDef,
    CreateOutboundConnectionResponseTypeDef,
    CreatePackageResponseTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteInboundConnectionResponseTypeDef,
    DeleteOutboundConnectionResponseTypeDef,
    DeletePackageResponseTypeDef,
    DescribeDomainAutoTunesResponseTypeDef,
    DescribeDomainConfigResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeDomainsResponseTypeDef,
    DescribeInboundConnectionsResponseTypeDef,
    DescribeInstanceTypeLimitsResponseTypeDef,
    DescribeOutboundConnectionsResponseTypeDef,
    DescribePackagesFilterTypeDef,
    DescribePackagesResponseTypeDef,
    DescribeReservedInstanceOfferingsResponseTypeDef,
    DescribeReservedInstancesResponseTypeDef,
    DissociatePackageResponseTypeDef,
    DomainEndpointOptionsTypeDef,
    DomainInformationContainerTypeDef,
    EBSOptionsTypeDef,
    EncryptionAtRestOptionsTypeDef,
    FilterTypeDef,
    GetCompatibleVersionsResponseTypeDef,
    GetPackageVersionHistoryResponseTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    GetUpgradeStatusResponseTypeDef,
    ListDomainNamesResponseTypeDef,
    ListDomainsForPackageResponseTypeDef,
    ListInstanceTypeDetailsResponseTypeDef,
    ListPackagesForDomainResponseTypeDef,
    ListTagsResponseTypeDef,
    ListVersionsResponseTypeDef,
    LogPublishingOptionTypeDef,
    NodeToNodeEncryptionOptionsTypeDef,
    PackageSourceTypeDef,
    PurchaseReservedInstanceOfferingResponseTypeDef,
    RejectInboundConnectionResponseTypeDef,
    SnapshotOptionsTypeDef,
    StartServiceSoftwareUpdateResponseTypeDef,
    TagTypeDef,
    UpdateDomainConfigResponseTypeDef,
    UpdatePackageResponseTypeDef,
    UpgradeDomainResponseTypeDef,
    VPCOptionsTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OpenSearchServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BaseException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DisabledOperationException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class OpenSearchServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpenSearchServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#exceptions)
        """

    async def accept_inbound_connection(
        self, *, ConnectionId: str
    ) -> AcceptInboundConnectionResponseTypeDef:
        """
        Allows the remote domain owner to accept an inbound cross-cluster connection
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.accept_inbound_connection)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#accept_inbound_connection)
        """

    async def add_tags(self, *, ARN: str, TagList: Sequence["TagTypeDef"]) -> None:
        """
        Attaches tags to an existing domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.add_tags)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#add_tags)
        """

    async def associate_package(
        self, *, PackageID: str, DomainName: str
    ) -> AssociatePackageResponseTypeDef:
        """
        Associates a package with an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.associate_package)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#associate_package)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#can_paginate)
        """

    async def cancel_service_software_update(
        self, *, DomainName: str
    ) -> CancelServiceSoftwareUpdateResponseTypeDef:
        """
        Cancels a scheduled service software update for an Amazon OpenSearch Service
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.cancel_service_software_update)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#cancel_service_software_update)
        """

    async def create_domain(
        self,
        *,
        DomainName: str,
        EngineVersion: str = ...,
        ClusterConfig: "ClusterConfigTypeDef" = ...,
        EBSOptions: "EBSOptionsTypeDef" = ...,
        AccessPolicies: str = ...,
        SnapshotOptions: "SnapshotOptionsTypeDef" = ...,
        VPCOptions: "VPCOptionsTypeDef" = ...,
        CognitoOptions: "CognitoOptionsTypeDef" = ...,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = ...,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = ...,
        AdvancedOptions: Mapping[str, str] = ...,
        LogPublishingOptions: Mapping[LogTypeType, "LogPublishingOptionTypeDef"] = ...,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = ...,
        AdvancedSecurityOptions: "AdvancedSecurityOptionsInputTypeDef" = ...,
        TagList: Sequence["TagTypeDef"] = ...,
        AutoTuneOptions: "AutoTuneOptionsInputTypeDef" = ...
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a new Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.create_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#create_domain)
        """

    async def create_outbound_connection(
        self,
        *,
        LocalDomainInfo: "DomainInformationContainerTypeDef",
        RemoteDomainInfo: "DomainInformationContainerTypeDef",
        ConnectionAlias: str
    ) -> CreateOutboundConnectionResponseTypeDef:
        """
        Creates a new cross-cluster connection from a local OpenSearch domain to a
        remote OpenSearch domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.create_outbound_connection)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#create_outbound_connection)
        """

    async def create_package(
        self,
        *,
        PackageName: str,
        PackageType: Literal["TXT-DICTIONARY"],
        PackageSource: "PackageSourceTypeDef",
        PackageDescription: str = ...
    ) -> CreatePackageResponseTypeDef:
        """
        Create a package for use with Amazon OpenSearch Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.create_package)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#create_package)
        """

    async def delete_domain(self, *, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        Permanently deletes the specified domain and all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.delete_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#delete_domain)
        """

    async def delete_inbound_connection(
        self, *, ConnectionId: str
    ) -> DeleteInboundConnectionResponseTypeDef:
        """
        Allows the remote domain owner to delete an existing inbound cross-cluster
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.delete_inbound_connection)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#delete_inbound_connection)
        """

    async def delete_outbound_connection(
        self, *, ConnectionId: str
    ) -> DeleteOutboundConnectionResponseTypeDef:
        """
        Allows the local domain owner to delete an existing outbound cross-cluster
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.delete_outbound_connection)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#delete_outbound_connection)
        """

    async def delete_package(self, *, PackageID: str) -> DeletePackageResponseTypeDef:
        """
        Deletes the package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.delete_package)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#delete_package)
        """

    async def describe_domain(self, *, DomainName: str) -> DescribeDomainResponseTypeDef:
        """
        Returns domain configuration information about the specified domain, including
        the domain ID, domain endpoint, and domain ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_domain)
        """

    async def describe_domain_auto_tunes(
        self, *, DomainName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> DescribeDomainAutoTunesResponseTypeDef:
        """
        Provides scheduled Auto-Tune action details for the domain, such as Auto-Tune
        action type, description, severity, and scheduled date.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_domain_auto_tunes)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_domain_auto_tunes)
        """

    async def describe_domain_config(
        self, *, DomainName: str
    ) -> DescribeDomainConfigResponseTypeDef:
        """
        Provides cluster configuration information about the specified domain, such as
        the state, creation date, update version, and update date for cluster options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_domain_config)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_domain_config)
        """

    async def describe_domains(
        self, *, DomainNames: Sequence[str]
    ) -> DescribeDomainsResponseTypeDef:
        """
        Returns domain configuration information about the specified domains, including
        the domain ID, domain endpoint, and domain ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_domains)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_domains)
        """

    async def describe_inbound_connections(
        self,
        *,
        Filters: Sequence["FilterTypeDef"] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeInboundConnectionsResponseTypeDef:
        """
        Lists all the inbound cross-cluster connections for a remote domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_inbound_connections)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_inbound_connections)
        """

    async def describe_instance_type_limits(
        self,
        *,
        InstanceType: OpenSearchPartitionInstanceTypeType,
        EngineVersion: str,
        DomainName: str = ...
    ) -> DescribeInstanceTypeLimitsResponseTypeDef:
        """
        Describe the limits for a given instance type and OpenSearch or Elasticsearch
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_instance_type_limits)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_instance_type_limits)
        """

    async def describe_outbound_connections(
        self,
        *,
        Filters: Sequence["FilterTypeDef"] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribeOutboundConnectionsResponseTypeDef:
        """
        Lists all the outbound cross-cluster connections for a local domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_outbound_connections)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_outbound_connections)
        """

    async def describe_packages(
        self,
        *,
        Filters: Sequence["DescribePackagesFilterTypeDef"] = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> DescribePackagesResponseTypeDef:
        """
        Describes all packages available to Amazon OpenSearch Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_packages)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_packages)
        """

    async def describe_reserved_instance_offerings(
        self, *, ReservedInstanceOfferingId: str = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> DescribeReservedInstanceOfferingsResponseTypeDef:
        """
        Lists available reserved OpenSearch instance offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_reserved_instance_offerings)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_reserved_instance_offerings)
        """

    async def describe_reserved_instances(
        self, *, ReservedInstanceId: str = ..., MaxResults: int = ..., NextToken: str = ...
    ) -> DescribeReservedInstancesResponseTypeDef:
        """
        Returns information about reserved OpenSearch instances for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.describe_reserved_instances)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#describe_reserved_instances)
        """

    async def dissociate_package(
        self, *, PackageID: str, DomainName: str
    ) -> DissociatePackageResponseTypeDef:
        """
        Dissociates a package from the Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.dissociate_package)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#dissociate_package)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#generate_presigned_url)
        """

    async def get_compatible_versions(
        self, *, DomainName: str = ...
    ) -> GetCompatibleVersionsResponseTypeDef:
        """
        Returns a list of upgrade-compatible versions of OpenSearch/Elasticsearch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.get_compatible_versions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#get_compatible_versions)
        """

    async def get_package_version_history(
        self, *, PackageID: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetPackageVersionHistoryResponseTypeDef:
        """
        Returns a list of package versions, along with their creation time and commit
        message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.get_package_version_history)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#get_package_version_history)
        """

    async def get_upgrade_history(
        self, *, DomainName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        Retrieves the complete history of the last 10 upgrades performed on the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.get_upgrade_history)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#get_upgrade_history)
        """

    async def get_upgrade_status(self, *, DomainName: str) -> GetUpgradeStatusResponseTypeDef:
        """
        Retrieves the latest status of the last upgrade or upgrade eligibility check
        performed on the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.get_upgrade_status)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#get_upgrade_status)
        """

    async def list_domain_names(
        self, *, EngineType: EngineTypeType = ...
    ) -> ListDomainNamesResponseTypeDef:
        """
        Returns the names of all domains owned by the current user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.list_domain_names)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#list_domain_names)
        """

    async def list_domains_for_package(
        self, *, PackageID: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListDomainsForPackageResponseTypeDef:
        """
        Lists all Amazon OpenSearch Service domains associated with the package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.list_domains_for_package)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#list_domains_for_package)
        """

    async def list_instance_type_details(
        self,
        *,
        EngineVersion: str,
        DomainName: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListInstanceTypeDetailsResponseTypeDef:
        """
        See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/ListInstanceTypeDetails).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.list_instance_type_details)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#list_instance_type_details)
        """

    async def list_packages_for_domain(
        self, *, DomainName: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListPackagesForDomainResponseTypeDef:
        """
        Lists all packages associated with the Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.list_packages_for_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#list_packages_for_domain)
        """

    async def list_tags(self, *, ARN: str) -> ListTagsResponseTypeDef:
        """
        Returns all tags for the given domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.list_tags)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#list_tags)
        """

    async def list_versions(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListVersionsResponseTypeDef:
        """
        List all supported versions of OpenSearch and Elasticsearch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.list_versions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#list_versions)
        """

    async def purchase_reserved_instance_offering(
        self, *, ReservedInstanceOfferingId: str, ReservationName: str, InstanceCount: int = ...
    ) -> PurchaseReservedInstanceOfferingResponseTypeDef:
        """
        Allows you to purchase reserved OpenSearch instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.purchase_reserved_instance_offering)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#purchase_reserved_instance_offering)
        """

    async def reject_inbound_connection(
        self, *, ConnectionId: str
    ) -> RejectInboundConnectionResponseTypeDef:
        """
        Allows the remote domain owner to reject an inbound cross-cluster connection
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.reject_inbound_connection)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#reject_inbound_connection)
        """

    async def remove_tags(self, *, ARN: str, TagKeys: Sequence[str]) -> None:
        """
        Removes the specified set of tags from the given domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.remove_tags)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#remove_tags)
        """

    async def start_service_software_update(
        self, *, DomainName: str
    ) -> StartServiceSoftwareUpdateResponseTypeDef:
        """
        Schedules a service software update for an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.start_service_software_update)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#start_service_software_update)
        """

    async def update_domain_config(
        self,
        *,
        DomainName: str,
        ClusterConfig: "ClusterConfigTypeDef" = ...,
        EBSOptions: "EBSOptionsTypeDef" = ...,
        SnapshotOptions: "SnapshotOptionsTypeDef" = ...,
        VPCOptions: "VPCOptionsTypeDef" = ...,
        CognitoOptions: "CognitoOptionsTypeDef" = ...,
        AdvancedOptions: Mapping[str, str] = ...,
        AccessPolicies: str = ...,
        LogPublishingOptions: Mapping[LogTypeType, "LogPublishingOptionTypeDef"] = ...,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = ...,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = ...,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = ...,
        AdvancedSecurityOptions: "AdvancedSecurityOptionsInputTypeDef" = ...,
        AutoTuneOptions: "AutoTuneOptionsTypeDef" = ...,
        DryRun: bool = ...
    ) -> UpdateDomainConfigResponseTypeDef:
        """
        Modifies the cluster configuration of the specified domain, such as setting the
        instance type and the number of instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.update_domain_config)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#update_domain_config)
        """

    async def update_package(
        self,
        *,
        PackageID: str,
        PackageSource: "PackageSourceTypeDef",
        PackageDescription: str = ...,
        CommitMessage: str = ...
    ) -> UpdatePackageResponseTypeDef:
        """
        Updates a package for use with Amazon OpenSearch Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.update_package)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#update_package)
        """

    async def upgrade_domain(
        self,
        *,
        DomainName: str,
        TargetVersion: str,
        PerformCheckOnly: bool = ...,
        AdvancedOptions: Mapping[str, str] = ...
    ) -> UpgradeDomainResponseTypeDef:
        """
        Allows you to either upgrade your domain or perform an upgrade eligibility check
        to a compatible version of OpenSearch or Elasticsearch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client.upgrade_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html#upgrade_domain)
        """

    async def __aenter__(self) -> "OpenSearchServiceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html#OpenSearchService.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opensearch/client.html)
        """
