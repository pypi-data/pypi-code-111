"""
Type annotations for opsworks service ServiceResource

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_opsworks.service_resource import OpsWorksServiceResource
    import types_aiobotocore_opsworks.service_resource as opsworks_resources

    session = get_session()
    async with session.resource("opsworks") as resource:
        resource: OpsWorksServiceResource

        my_layer: opsworks_resources.Layer = resource.Layer(...)
        my_stack: opsworks_resources.Stack = resource.Stack(...)
        my_stack_summary: opsworks_resources.StackSummary = resource.StackSummary(...)
```
"""
import sys
from typing import Dict, Iterator, List, Mapping, Sequence

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import OpsWorksClient
from .literals import LayerAttributesKeysType, LayerTypeType, RootDeviceTypeType
from .type_defs import (
    ChefConfigurationResponseMetadataTypeDef,
    ChefConfigurationTypeDef,
    CloudWatchLogsConfigurationResponseMetadataTypeDef,
    CloudWatchLogsConfigurationTypeDef,
    InstancesCountResponseMetadataTypeDef,
    LifecycleEventConfigurationResponseMetadataTypeDef,
    LifecycleEventConfigurationTypeDef,
    RecipesResponseMetadataTypeDef,
    RecipesTypeDef,
    SourceResponseMetadataTypeDef,
    SourceTypeDef,
    StackConfigurationManagerResponseMetadataTypeDef,
    StackConfigurationManagerTypeDef,
    VolumeConfigurationTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "OpsWorksServiceResource",
    "Layer",
    "Stack",
    "StackSummary",
    "ServiceResourceStacksCollection",
    "StackLayersCollection",
)


class ServiceResourceStacksCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#serviceresourcestackscollection)
    """

    async def all(self) -> "ServiceResourceStacksCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#serviceresourcestackscollection)
        """

    async def filter(  # type: ignore
        self, *, StackIds: Sequence[str] = ...
    ) -> "ServiceResourceStacksCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#serviceresourcestackscollection)
        """

    async def limit(self, count: int) -> "ServiceResourceStacksCollection":
        """
        Return at most this many Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#serviceresourcestackscollection)
        """

    async def page_size(self, count: int) -> "ServiceResourceStacksCollection":
        """
        Fetch at most this many Stacks per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#serviceresourcestackscollection)
        """

    async def pages(self) -> Iterator[List["Stack"]]:
        """
        A generator which yields pages of Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#serviceresourcestackscollection)
        """

    async def __iter__(self) -> Iterator["Stack"]:
        """
        A generator which yields Stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.stacks)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#serviceresourcestackscollection)
        """


class StackLayersCollection(ResourceCollection):
    async def all(self) -> "StackLayersCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    async def filter(  # type: ignore
        self, *, StackId: str = ..., LayerIds: Sequence[str] = ...
    ) -> "StackLayersCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def limit(self, count: int) -> "StackLayersCollection":
        """
        Return at most this many Layers.
        """

    async def page_size(self, count: int) -> "StackLayersCollection":
        """
        Fetch at most this many Layers per service request.
        """

    async def pages(self) -> Iterator[List["Layer"]]:
        """
        A generator which yields pages of Layers.
        """

    async def __iter__(self) -> Iterator["Layer"]:
        """
        A generator which yields Layers.
        """


class Layer(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#layer)
    """

    arn: str
    stack_id: str
    layer_id: str
    type: LayerTypeType
    name: str
    shortname: str
    attributes: Dict[LayerAttributesKeysType, str]
    cloud_watch_logs_configuration: CloudWatchLogsConfigurationResponseMetadataTypeDef
    custom_instance_profile_arn: str
    custom_json: str
    custom_security_group_ids: List[str]
    default_security_group_names: List[str]
    packages: List[str]
    volume_configurations: List["VolumeConfigurationTypeDef"]
    enable_auto_healing: bool
    auto_assign_elastic_ips: bool
    auto_assign_public_ips: bool
    default_recipes: RecipesResponseMetadataTypeDef
    custom_recipes: RecipesResponseMetadataTypeDef
    created_at: str
    install_updates_on_boot: bool
    use_ebs_optimized_instances: bool
    lifecycle_event_configuration: LifecycleEventConfigurationResponseMetadataTypeDef
    id: str
    stack: "Stack"

    async def delete(self) -> None:
        """
        Deletes a specified layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#layerdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#layerget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_layers` to update the attributes of the
        Layer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#layerload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_layers` to update the attributes of the
        Layer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Layer.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#layerreload-method)
        """


_Layer = Layer


class StackSummary(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stacksummary)
    """

    name: str
    arn: str
    layers_count: int
    apps_count: int
    instances_count: InstancesCountResponseMetadataTypeDef
    stack_id: str

    async def Stack(self) -> "_Stack":
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.Stack)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stacksummarystack-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stacksummaryget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_stack_summary` to update the attributes
        of the StackSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stacksummaryload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_stack_summary` to update the attributes
        of the StackSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.StackSummary.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stacksummaryreload-method)
        """


_StackSummary = StackSummary


class Stack(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stack)
    """

    stack_id: str
    name: str
    arn: str
    region: str
    vpc_id: str
    attributes: Dict[Literal["Color"], str]
    service_role_arn: str
    default_instance_profile_arn: str
    default_os: str
    hostname_theme: str
    default_availability_zone: str
    default_subnet_id: str
    custom_json: str
    configuration_manager: StackConfigurationManagerResponseMetadataTypeDef
    chef_configuration: ChefConfigurationResponseMetadataTypeDef
    use_custom_cookbooks: bool
    use_opsworks_security_groups: bool
    custom_cookbooks_source: SourceResponseMetadataTypeDef
    default_ssh_key_name: str
    created_at: str
    default_root_device_type: RootDeviceTypeType
    agent_version: str
    id: str
    layers: StackLayersCollection

    async def Summary(self) -> _StackSummary:
        """
        Creates a StackSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.Summary)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stacksummary-method)
        """

    async def create_layer(
        self,
        *,
        Type: LayerTypeType,
        Name: str,
        Shortname: str,
        Attributes: Mapping[LayerAttributesKeysType, str] = ...,
        CloudWatchLogsConfiguration: "CloudWatchLogsConfigurationTypeDef" = ...,
        CustomInstanceProfileArn: str = ...,
        CustomJson: str = ...,
        CustomSecurityGroupIds: Sequence[str] = ...,
        Packages: Sequence[str] = ...,
        VolumeConfigurations: Sequence["VolumeConfigurationTypeDef"] = ...,
        EnableAutoHealing: bool = ...,
        AutoAssignElasticIps: bool = ...,
        AutoAssignPublicIps: bool = ...,
        CustomRecipes: "RecipesTypeDef" = ...,
        InstallUpdatesOnBoot: bool = ...,
        UseEbsOptimizedInstances: bool = ...,
        LifecycleEventConfiguration: "LifecycleEventConfigurationTypeDef" = ...
    ) -> _Layer:
        """
        Creates a layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.create_layer)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stackcreate_layer-method)
        """

    async def delete(self) -> None:
        """
        Deletes a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stackdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stackget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_stacks` to update the attributes of the
        Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stackload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`OpsWorks.Client.describe_stacks` to update the attributes of the
        Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Stack.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#stackreload-method)
        """


_Stack = Stack


class OpsWorksResourceMeta(ResourceMeta):
    client: OpsWorksClient


class OpsWorksServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html)
    """

    meta: "OpsWorksResourceMeta"
    stacks: ServiceResourceStacksCollection

    async def Layer(self, id: str) -> _Layer:
        """
        Creates a Layer resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Layer)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#opsworksserviceresourcelayer-method)
        """

    async def Stack(self, id: str) -> _Stack:
        """
        Creates a Stack resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.Stack)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#opsworksserviceresourcestack-method)
        """

    async def StackSummary(self, stack_id: str) -> _StackSummary:
        """
        Creates a StackSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.StackSummary)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#opsworksserviceresourcestacksummary-method)
        """

    async def create_stack(
        self,
        *,
        Name: str,
        Region: str,
        ServiceRoleArn: str,
        DefaultInstanceProfileArn: str,
        VpcId: str = ...,
        Attributes: Mapping[Literal["Color"], str] = ...,
        DefaultOs: str = ...,
        HostnameTheme: str = ...,
        DefaultAvailabilityZone: str = ...,
        DefaultSubnetId: str = ...,
        CustomJson: str = ...,
        ConfigurationManager: "StackConfigurationManagerTypeDef" = ...,
        ChefConfiguration: "ChefConfigurationTypeDef" = ...,
        UseCustomCookbooks: bool = ...,
        UseOpsworksSecurityGroups: bool = ...,
        CustomCookbooksSource: "SourceTypeDef" = ...,
        DefaultSshKeyName: str = ...,
        DefaultRootDeviceType: RootDeviceTypeType = ...,
        AgentVersion: str = ...
    ) -> _Stack:
        """
        Creates a new stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.create_stack)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#opsworksserviceresourcecreate_stack-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.ServiceResource.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_opsworks/service_resource.html#opsworksserviceresourceget_available_subresources-method)
        """
