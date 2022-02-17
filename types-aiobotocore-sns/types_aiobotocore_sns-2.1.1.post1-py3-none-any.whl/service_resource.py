"""
Type annotations for sns service ServiceResource

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_sns.service_resource import SNSServiceResource
    import types_aiobotocore_sns.service_resource as sns_resources

    session = get_session()
    async with session.resource("sns") as resource:
        resource: SNSServiceResource

        my_platform_application: sns_resources.PlatformApplication = resource.PlatformApplication(...)
        my_platform_endpoint: sns_resources.PlatformEndpoint = resource.PlatformEndpoint(...)
        my_subscription: sns_resources.Subscription = resource.Subscription(...)
        my_topic: sns_resources.Topic = resource.Topic(...)
```
"""
from typing import Dict, Iterator, List, Mapping, Sequence

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import SNSClient
from .type_defs import MessageAttributeValueTypeDef, PublishResponseTypeDef, TagTypeDef

__all__ = (
    "SNSServiceResource",
    "PlatformApplication",
    "PlatformEndpoint",
    "Subscription",
    "Topic",
    "ServiceResourcePlatformApplicationsCollection",
    "ServiceResourceSubscriptionsCollection",
    "ServiceResourceTopicsCollection",
    "PlatformApplicationEndpointsCollection",
    "TopicSubscriptionsCollection",
)


class ServiceResourcePlatformApplicationsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.platform_applications)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourceplatformapplicationscollection)
    """

    async def all(self) -> "ServiceResourcePlatformApplicationsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.platform_applications)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourceplatformapplicationscollection)
        """

    async def filter(  # type: ignore
        self, *, NextToken: str = ...
    ) -> "ServiceResourcePlatformApplicationsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.platform_applications)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourceplatformapplicationscollection)
        """

    async def limit(self, count: int) -> "ServiceResourcePlatformApplicationsCollection":
        """
        Return at most this many PlatformApplications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.platform_applications)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourceplatformapplicationscollection)
        """

    async def page_size(self, count: int) -> "ServiceResourcePlatformApplicationsCollection":
        """
        Fetch at most this many PlatformApplications per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.platform_applications)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourceplatformapplicationscollection)
        """

    async def pages(self) -> Iterator[List["PlatformApplication"]]:
        """
        A generator which yields pages of PlatformApplications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.platform_applications)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourceplatformapplicationscollection)
        """

    async def __iter__(self) -> Iterator["PlatformApplication"]:
        """
        A generator which yields PlatformApplications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.platform_applications)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourceplatformapplicationscollection)
        """


class ServiceResourceSubscriptionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.subscriptions)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcesubscriptionscollection)
    """

    async def all(self) -> "ServiceResourceSubscriptionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.subscriptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcesubscriptionscollection)
        """

    async def filter(  # type: ignore
        self, *, NextToken: str = ...
    ) -> "ServiceResourceSubscriptionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.subscriptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcesubscriptionscollection)
        """

    async def limit(self, count: int) -> "ServiceResourceSubscriptionsCollection":
        """
        Return at most this many Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.subscriptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcesubscriptionscollection)
        """

    async def page_size(self, count: int) -> "ServiceResourceSubscriptionsCollection":
        """
        Fetch at most this many Subscriptions per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.subscriptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcesubscriptionscollection)
        """

    async def pages(self) -> Iterator[List["Subscription"]]:
        """
        A generator which yields pages of Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.subscriptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcesubscriptionscollection)
        """

    async def __iter__(self) -> Iterator["Subscription"]:
        """
        A generator which yields Subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.subscriptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcesubscriptionscollection)
        """


class ServiceResourceTopicsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.topics)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcetopicscollection)
    """

    async def all(self) -> "ServiceResourceTopicsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.topics)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcetopicscollection)
        """

    async def filter(  # type: ignore
        self, *, NextToken: str = ...
    ) -> "ServiceResourceTopicsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.topics)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcetopicscollection)
        """

    async def limit(self, count: int) -> "ServiceResourceTopicsCollection":
        """
        Return at most this many Topics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.topics)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcetopicscollection)
        """

    async def page_size(self, count: int) -> "ServiceResourceTopicsCollection":
        """
        Fetch at most this many Topics per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.topics)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcetopicscollection)
        """

    async def pages(self) -> Iterator[List["Topic"]]:
        """
        A generator which yields pages of Topics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.topics)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcetopicscollection)
        """

    async def __iter__(self) -> Iterator["Topic"]:
        """
        A generator which yields Topics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.topics)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#serviceresourcetopicscollection)
        """


class PlatformApplicationEndpointsCollection(ResourceCollection):
    async def all(self) -> "PlatformApplicationEndpointsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    async def filter(  # type: ignore
        self, *, NextToken: str = ...
    ) -> "PlatformApplicationEndpointsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def limit(self, count: int) -> "PlatformApplicationEndpointsCollection":
        """
        Return at most this many PlatformEndpoints.
        """

    async def page_size(self, count: int) -> "PlatformApplicationEndpointsCollection":
        """
        Fetch at most this many PlatformEndpoints per service request.
        """

    async def pages(self) -> Iterator[List["PlatformEndpoint"]]:
        """
        A generator which yields pages of PlatformEndpoints.
        """

    async def __iter__(self) -> Iterator["PlatformEndpoint"]:
        """
        A generator which yields PlatformEndpoints.
        """


class TopicSubscriptionsCollection(ResourceCollection):
    async def all(self) -> "TopicSubscriptionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    async def filter(  # type: ignore
        self, *, NextToken: str = ...
    ) -> "TopicSubscriptionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def limit(self, count: int) -> "TopicSubscriptionsCollection":
        """
        Return at most this many Subscriptions.
        """

    async def page_size(self, count: int) -> "TopicSubscriptionsCollection":
        """
        Fetch at most this many Subscriptions per service request.
        """

    async def pages(self) -> Iterator[List["Subscription"]]:
        """
        A generator which yields pages of Subscriptions.
        """

    async def __iter__(self) -> Iterator["Subscription"]:
        """
        A generator which yields Subscriptions.
        """


class PlatformEndpoint(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformendpoint)
    """

    attributes: Dict[str, str]
    arn: str

    async def delete(self) -> None:
        """
        Deletes the endpoint for a device and mobile app from Amazon SNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformendpointdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformendpointget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`SNS.Client.get_endpoint_attributes` to update the attributes of
        the PlatformEndpoint resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformendpointload-method)
        """

    async def publish(
        self,
        *,
        Message: str,
        TopicArn: str = ...,
        PhoneNumber: str = ...,
        Subject: str = ...,
        MessageStructure: str = ...,
        MessageAttributes: Mapping[str, "MessageAttributeValueTypeDef"] = ...,
        MessageDeduplicationId: str = ...,
        MessageGroupId: str = ...
    ) -> PublishResponseTypeDef:
        """
        Sends a message to an Amazon SNS topic, a text message (SMS message) directly to
        a phone number, or a message to a mobile platform endpoint (when you specify the
        `TargetArn` ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.publish)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformendpointpublish-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`SNS.Client.get_endpoint_attributes` to update the attributes of
        the PlatformEndpoint resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformendpointreload-method)
        """

    async def set_attributes(self, *, Attributes: Mapping[str, str]) -> None:
        """
        Sets the attributes for an endpoint for a device on one of the supported push
        notification services, such as GCM (Firebase Cloud Messaging) and APNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.set_attributes)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformendpointset_attributes-method)
        """


_PlatformEndpoint = PlatformEndpoint


class Subscription(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.Subscription)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#subscription)
    """

    attributes: Dict[str, str]
    arn: str

    async def delete(self) -> None:
        """
        Deletes a subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#subscriptiondelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#subscriptionget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`SNS.Client.get_subscription_attributes` to update the attributes
        of the Subscription resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#subscriptionload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`SNS.Client.get_subscription_attributes` to update the attributes
        of the Subscription resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#subscriptionreload-method)
        """

    async def set_attributes(self, *, AttributeName: str, AttributeValue: str = ...) -> None:
        """
        Allows a subscription owner to set an attribute of the subscription to a new
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.set_attributes)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#subscriptionset_attributes-method)
        """


_Subscription = Subscription


class PlatformApplication(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformapplication)
    """

    attributes: Dict[str, str]
    arn: str
    endpoints: PlatformApplicationEndpointsCollection

    async def create_platform_endpoint(
        self, *, Token: str, CustomUserData: str = ..., Attributes: Mapping[str, str] = ...
    ) -> _PlatformEndpoint:
        """
        Creates an endpoint for a device and mobile app on one of the supported push
        notification services, such as GCM (Firebase Cloud Messaging) and APNS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.create_platform_endpoint)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformapplicationcreate_platform_endpoint-method)
        """

    async def delete(self) -> None:
        """
        Deletes a platform application object for one of the supported push notification
        services, such as APNS and GCM (Firebase Cloud Messaging).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformapplicationdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformapplicationget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`SNS.Client.get_platform_application_attributes` to update the
        attributes of the PlatformApplication resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformapplicationload-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`SNS.Client.get_platform_application_attributes` to update the
        attributes of the PlatformApplication resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformapplicationreload-method)
        """

    async def set_attributes(self, *, Attributes: Mapping[str, str]) -> None:
        """
        Sets the attributes of the platform application object for the supported push
        notification services, such as APNS and GCM (Firebase Cloud Messaging).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.set_attributes)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#platformapplicationset_attributes-method)
        """


_PlatformApplication = PlatformApplication


class Topic(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.Topic)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topic)
    """

    attributes: Dict[str, str]
    arn: str
    subscriptions: TopicSubscriptionsCollection

    async def add_permission(
        self, *, Label: str, AWSAccountId: Sequence[str], ActionName: Sequence[str]
    ) -> None:
        """
        Adds a statement to a topic's access control policy, granting access for the
        specified Amazon Web Services accounts to the specified actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.add_permission)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicadd_permission-method)
        """

    async def confirm_subscription(
        self, *, Token: str, AuthenticateOnUnsubscribe: str = ...
    ) -> _Subscription:
        """
        Verifies an endpoint owner's intent to receive messages by validating the token
        sent to the endpoint by an earlier `Subscribe` action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.confirm_subscription)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicconfirm_subscription-method)
        """

    async def delete(self) -> None:
        """
        Deletes a topic and all its subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`SNS.Client.get_topic_attributes` to update the attributes of the
        Topic resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicload-method)
        """

    async def publish(
        self,
        *,
        Message: str,
        TargetArn: str = ...,
        PhoneNumber: str = ...,
        Subject: str = ...,
        MessageStructure: str = ...,
        MessageAttributes: Mapping[str, "MessageAttributeValueTypeDef"] = ...,
        MessageDeduplicationId: str = ...,
        MessageGroupId: str = ...
    ) -> PublishResponseTypeDef:
        """
        Sends a message to an Amazon SNS topic, a text message (SMS message) directly to
        a phone number, or a message to a mobile platform endpoint (when you specify the
        `TargetArn` ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.publish)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicpublish-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`SNS.Client.get_topic_attributes` to update the attributes of the
        Topic resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicreload-method)
        """

    async def remove_permission(self, *, Label: str) -> None:
        """
        Removes a statement from a topic's access control policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.remove_permission)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicremove_permission-method)
        """

    async def set_attributes(self, *, AttributeName: str, AttributeValue: str = ...) -> None:
        """
        Allows a topic owner to set an attribute of the topic to a new value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.set_attributes)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicset_attributes-method)
        """

    async def subscribe(
        self,
        *,
        Protocol: str,
        Endpoint: str = ...,
        Attributes: Mapping[str, str] = ...,
        ReturnSubscriptionArn: bool = ...
    ) -> _Subscription:
        """
        Subscribes an endpoint to an Amazon SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.subscribe)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#topicsubscribe-method)
        """


_Topic = Topic


class SNSResourceMeta(ResourceMeta):
    client: SNSClient


class SNSServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html)
    """

    meta: "SNSResourceMeta"
    platform_applications: ServiceResourcePlatformApplicationsCollection
    subscriptions: ServiceResourceSubscriptionsCollection
    topics: ServiceResourceTopicsCollection

    async def PlatformApplication(self, arn: str) -> _PlatformApplication:
        """
        Creates a PlatformApplication resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#snsserviceresourceplatformapplication-method)
        """

    async def PlatformEndpoint(self, arn: str) -> _PlatformEndpoint:
        """
        Creates a PlatformEndpoint resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#snsserviceresourceplatformendpoint-method)
        """

    async def Subscription(self, arn: str) -> _Subscription:
        """
        Creates a Subscription resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.Subscription)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#snsserviceresourcesubscription-method)
        """

    async def Topic(self, arn: str) -> _Topic:
        """
        Creates a Topic resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.Topic)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#snsserviceresourcetopic-method)
        """

    async def create_platform_application(
        self, *, Name: str, Platform: str, Attributes: Mapping[str, str]
    ) -> _PlatformApplication:
        """
        Creates a platform application object for one of the supported push notification
        services, such as APNS and GCM (Firebase Cloud Messaging), to which devices and
        mobile apps may register.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.create_platform_application)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#snsserviceresourcecreate_platform_application-method)
        """

    async def create_topic(
        self, *, Name: str, Attributes: Mapping[str, str] = ..., Tags: Sequence["TagTypeDef"] = ...
    ) -> _Topic:
        """
        Creates a topic to which notifications can be published.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.create_topic)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#snsserviceresourcecreate_topic-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sns/service_resource.html#snsserviceresourceget_available_subresources-method)
        """
