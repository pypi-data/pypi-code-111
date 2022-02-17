"""
Type annotations for s3 service ServiceResource

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_s3.service_resource import S3ServiceResource
    import types_aiobotocore_s3.service_resource as s3_resources

    session = get_session()
    async with session.resource("s3") as resource:
        resource: S3ServiceResource

        my_bucket: s3_resources.Bucket = resource.Bucket(...)
        my_bucket_acl: s3_resources.BucketAcl = resource.BucketAcl(...)
        my_bucket_cors: s3_resources.BucketCors = resource.BucketCors(...)
        my_bucket_lifecycle: s3_resources.BucketLifecycle = resource.BucketLifecycle(...)
        my_bucket_lifecycle_configuration: s3_resources.BucketLifecycleConfiguration = resource.BucketLifecycleConfiguration(...)
        my_bucket_logging: s3_resources.BucketLogging = resource.BucketLogging(...)
        my_bucket_notification: s3_resources.BucketNotification = resource.BucketNotification(...)
        my_bucket_policy: s3_resources.BucketPolicy = resource.BucketPolicy(...)
        my_bucket_request_payment: s3_resources.BucketRequestPayment = resource.BucketRequestPayment(...)
        my_bucket_tagging: s3_resources.BucketTagging = resource.BucketTagging(...)
        my_bucket_versioning: s3_resources.BucketVersioning = resource.BucketVersioning(...)
        my_bucket_website: s3_resources.BucketWebsite = resource.BucketWebsite(...)
        my_multipart_upload: s3_resources.MultipartUpload = resource.MultipartUpload(...)
        my_multipart_upload_part: s3_resources.MultipartUploadPart = resource.MultipartUploadPart(...)
        my_object: s3_resources.Object = resource.Object(...)
        my_object_acl: s3_resources.ObjectAcl = resource.ObjectAcl(...)
        my_object_summary: s3_resources.ObjectSummary = resource.ObjectSummary(...)
        my_object_version: s3_resources.ObjectVersion = resource.ObjectVersion(...)
```
"""
import sys
from datetime import datetime
from typing import IO, Any, Callable, Dict, Iterator, List, Mapping, Sequence, Union

from boto3.resources.base import ResourceMeta
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.response import StreamingBody

from .client import S3Client
from .literals import (
    ArchiveStatusType,
    BucketCannedACLType,
    BucketVersioningStatusType,
    MetadataDirectiveType,
    MFADeleteStatusType,
    ObjectCannedACLType,
    ObjectLockLegalHoldStatusType,
    ObjectLockModeType,
    ObjectOwnershipType,
    ObjectStorageClassType,
    PayerType,
    ReplicationStatusType,
    ServerSideEncryptionType,
    StorageClassType,
    TaggingDirectiveType,
)
from .type_defs import (
    AbortMultipartUploadOutputTypeDef,
    AccessControlPolicyTypeDef,
    BucketLifecycleConfigurationTypeDef,
    BucketLoggingStatusTypeDef,
    CompletedMultipartUploadTypeDef,
    CopyObjectOutputTypeDef,
    CopySourceTypeDef,
    CORSConfigurationTypeDef,
    CORSRuleTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketOutputTypeDef,
    DeleteObjectOutputTypeDef,
    DeleteObjectsOutputTypeDef,
    DeleteTypeDef,
    ErrorDocumentResponseMetadataTypeDef,
    GetObjectOutputTypeDef,
    GrantTypeDef,
    HeadObjectOutputTypeDef,
    IndexDocumentResponseMetadataTypeDef,
    InitiatorResponseMetadataTypeDef,
    LambdaFunctionConfigurationTypeDef,
    LifecycleConfigurationTypeDef,
    LifecycleRuleTypeDef,
    LoggingEnabledResponseMetadataTypeDef,
    NotificationConfigurationTypeDef,
    OwnerResponseMetadataTypeDef,
    PutObjectAclOutputTypeDef,
    PutObjectOutputTypeDef,
    QueueConfigurationTypeDef,
    RedirectAllRequestsToResponseMetadataTypeDef,
    RequestPaymentConfigurationTypeDef,
    RestoreObjectOutputTypeDef,
    RestoreRequestTypeDef,
    RoutingRuleTypeDef,
    RuleTypeDef,
    TaggingTypeDef,
    TagTypeDef,
    TopicConfigurationTypeDef,
    UploadPartCopyOutputTypeDef,
    UploadPartOutputTypeDef,
    VersioningConfigurationTypeDef,
    WebsiteConfigurationTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "S3ServiceResource",
    "Bucket",
    "BucketAcl",
    "BucketCors",
    "BucketLifecycle",
    "BucketLifecycleConfiguration",
    "BucketLogging",
    "BucketNotification",
    "BucketPolicy",
    "BucketRequestPayment",
    "BucketTagging",
    "BucketVersioning",
    "BucketWebsite",
    "MultipartUpload",
    "MultipartUploadPart",
    "Object",
    "ObjectAcl",
    "ObjectSummary",
    "ObjectVersion",
    "ServiceResourceBucketsCollection",
    "BucketMultipartUploadsCollection",
    "BucketObjectVersionsCollection",
    "BucketObjectsCollection",
    "MultipartUploadPartsCollection",
)


class ServiceResourceBucketsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#serviceresourcebucketscollection)
    """

    async def all(self) -> "ServiceResourceBucketsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#serviceresourcebucketscollection)
        """

    async def filter(self) -> "ServiceResourceBucketsCollection":  # type: ignore
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#serviceresourcebucketscollection)
        """

    async def limit(self, count: int) -> "ServiceResourceBucketsCollection":
        """
        Return at most this many Buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#serviceresourcebucketscollection)
        """

    async def page_size(self, count: int) -> "ServiceResourceBucketsCollection":
        """
        Fetch at most this many Buckets per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#serviceresourcebucketscollection)
        """

    async def pages(self) -> Iterator[List["Bucket"]]:
        """
        A generator which yields pages of Buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#serviceresourcebucketscollection)
        """

    async def __iter__(self) -> Iterator["Bucket"]:
        """
        A generator which yields Buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#serviceresourcebucketscollection)
        """


class BucketMultipartUploadsCollection(ResourceCollection):
    async def all(self) -> "BucketMultipartUploadsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    async def filter(  # type: ignore
        self,
        *,
        Delimiter: str = ...,
        EncodingType: Literal["url"] = ...,
        KeyMarker: str = ...,
        MaxUploads: int = ...,
        Prefix: str = ...,
        UploadIdMarker: str = ...,
        ExpectedBucketOwner: str = ...
    ) -> "BucketMultipartUploadsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def limit(self, count: int) -> "BucketMultipartUploadsCollection":
        """
        Return at most this many MultipartUploads.
        """

    async def page_size(self, count: int) -> "BucketMultipartUploadsCollection":
        """
        Fetch at most this many MultipartUploads per service request.
        """

    async def pages(self) -> Iterator[List["MultipartUpload"]]:
        """
        A generator which yields pages of MultipartUploads.
        """

    async def __iter__(self) -> Iterator["MultipartUpload"]:
        """
        A generator which yields MultipartUploads.
        """


class BucketObjectVersionsCollection(ResourceCollection):
    async def all(self) -> "BucketObjectVersionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    async def filter(  # type: ignore
        self,
        *,
        Delimiter: str = ...,
        EncodingType: Literal["url"] = ...,
        KeyMarker: str = ...,
        MaxKeys: int = ...,
        Prefix: str = ...,
        VersionIdMarker: str = ...,
        ExpectedBucketOwner: str = ...
    ) -> "BucketObjectVersionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...
    ) -> List[DeleteObjectsOutputTypeDef]:
        """
        Batch method.
        """

    async def limit(self, count: int) -> "BucketObjectVersionsCollection":
        """
        Return at most this many ObjectVersions.
        """

    async def page_size(self, count: int) -> "BucketObjectVersionsCollection":
        """
        Fetch at most this many ObjectVersions per service request.
        """

    async def pages(self) -> Iterator[List["ObjectVersion"]]:
        """
        A generator which yields pages of ObjectVersions.
        """

    async def __iter__(self) -> Iterator["ObjectVersion"]:
        """
        A generator which yields ObjectVersions.
        """


class BucketObjectsCollection(ResourceCollection):
    async def all(self) -> "BucketObjectsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    async def filter(  # type: ignore
        self,
        *,
        Delimiter: str = ...,
        EncodingType: Literal["url"] = ...,
        Marker: str = ...,
        MaxKeys: int = ...,
        Prefix: str = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...
    ) -> "BucketObjectsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...
    ) -> List[DeleteObjectsOutputTypeDef]:
        """
        Batch method.
        """

    async def limit(self, count: int) -> "BucketObjectsCollection":
        """
        Return at most this many ObjectSummarys.
        """

    async def page_size(self, count: int) -> "BucketObjectsCollection":
        """
        Fetch at most this many ObjectSummarys per service request.
        """

    async def pages(self) -> Iterator[List["ObjectSummary"]]:
        """
        A generator which yields pages of ObjectSummarys.
        """

    async def __iter__(self) -> Iterator["ObjectSummary"]:
        """
        A generator which yields ObjectSummarys.
        """


class MultipartUploadPartsCollection(ResourceCollection):
    async def all(self) -> "MultipartUploadPartsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    async def filter(  # type: ignore
        self,
        *,
        MaxParts: int = ...,
        PartNumberMarker: int = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...
    ) -> "MultipartUploadPartsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def limit(self, count: int) -> "MultipartUploadPartsCollection":
        """
        Return at most this many MultipartUploadParts.
        """

    async def page_size(self, count: int) -> "MultipartUploadPartsCollection":
        """
        Fetch at most this many MultipartUploadParts per service request.
        """

    async def pages(self) -> Iterator[List["MultipartUploadPart"]]:
        """
        A generator which yields pages of MultipartUploadParts.
        """

    async def __iter__(self) -> Iterator["MultipartUploadPart"]:
        """
        A generator which yields MultipartUploadParts.
        """


class BucketAcl(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketAcl)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketacl)
    """

    owner: OwnerResponseMetadataTypeDef
    grants: List["GrantTypeDef"]
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketaclbucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketaclget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_acl` to update the attributes of the
        BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketaclload-method)
        """

    async def put(
        self,
        *,
        ACL: BucketCannedACLType = ...,
        AccessControlPolicy: "AccessControlPolicyTypeDef" = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWrite: str = ...,
        GrantWriteACP: str = ...,
        ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Sets the permissions on an existing bucket using access control lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketaclput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_acl` to update the attributes of the
        BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketaclreload-method)
        """


_BucketAcl = BucketAcl


class BucketCors(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketCors)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcors)
    """

    cors_rules: List["CORSRuleTypeDef"]
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcorsbucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        Deletes the `cors` configuration information set for the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcorsdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcorsget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_cors` to update the attributes of the
        BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcorsload-method)
        """

    async def put(
        self, *, CORSConfiguration: "CORSConfigurationTypeDef", ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Sets the `cors` configuration for your bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcorsput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_cors` to update the attributes of the
        BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcorsreload-method)
        """


_BucketCors = BucketCors


class BucketLifecycle(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycle)
    """

    rules: List["RuleTypeDef"]
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecyclebucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        Deletes the lifecycle configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycledelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle` to update the attributes of the
        BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleload-method)
        """

    async def put(
        self,
        *,
        LifecycleConfiguration: "LifecycleConfigurationTypeDef" = ...,
        ExpectedBucketOwner: str = ...
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle` to update the attributes of the
        BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecyclereload-method)
        """


_BucketLifecycle = BucketLifecycle


class BucketLifecycleConfiguration(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleconfiguration)
    """

    rules: List["LifecycleRuleTypeDef"]
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleconfigurationbucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        Deletes the lifecycle configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleconfigurationdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleconfigurationget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle_configuration` to update the
        attributes of the BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleconfigurationload-method)
        """

    async def put(
        self,
        *,
        LifecycleConfiguration: "BucketLifecycleConfigurationTypeDef" = ...,
        ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Creates a new lifecycle configuration for the bucket or replaces an existing
        lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleconfigurationput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle_configuration` to update the
        attributes of the BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleconfigurationreload-method)
        """


_BucketLifecycleConfiguration = BucketLifecycleConfiguration


class BucketLogging(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLogging)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlogging)
    """

    logging_enabled: LoggingEnabledResponseMetadataTypeDef
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketloggingbucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketloggingget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_logging` to update the attributes of the
        BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketloggingload-method)
        """

    async def put(
        self, *, BucketLoggingStatus: "BucketLoggingStatusTypeDef", ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Set the logging parameters for a bucket and to specify permissions for who can
        view and modify the logging parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketloggingput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_logging` to update the attributes of the
        BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketloggingreload-method)
        """


_BucketLogging = BucketLogging


class BucketNotification(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketNotification)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketnotification)
    """

    topic_configurations: List["TopicConfigurationTypeDef"]
    queue_configurations: List["QueueConfigurationTypeDef"]
    lambda_function_configurations: List["LambdaFunctionConfigurationTypeDef"]
    event_bridge_configuration: Dict[str, Any]
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketnotificationbucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketnotificationget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_notification_configuration` to update the
        attributes of the BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketnotificationload-method)
        """

    async def put(
        self,
        *,
        NotificationConfiguration: "NotificationConfigurationTypeDef",
        ExpectedBucketOwner: str = ...,
        SkipDestinationValidation: bool = ...
    ) -> None:
        """
        Enables notifications of specified events for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketnotificationput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_notification_configuration` to update the
        attributes of the BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketnotificationreload-method)
        """


_BucketNotification = BucketNotification


class BucketPolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketpolicy)
    """

    policy: str
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketpolicybucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        This implementation of the DELETE action uses the policy subresource to delete
        the policy of a specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketpolicydelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketpolicyget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_policy` to update the attributes of the
        BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketpolicyload-method)
        """

    async def put(
        self,
        *,
        Policy: str,
        ConfirmRemoveSelfBucketAccess: bool = ...,
        ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Applies an Amazon S3 bucket policy to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketpolicyput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_policy` to update the attributes of the
        BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketpolicyreload-method)
        """


_BucketPolicy = BucketPolicy


class BucketRequestPayment(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketrequestpayment)
    """

    payer: PayerType
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketrequestpaymentbucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketrequestpaymentget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_request_payment` to update the attributes
        of the BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketrequestpaymentload-method)
        """

    async def put(
        self,
        *,
        RequestPaymentConfiguration: "RequestPaymentConfigurationTypeDef",
        ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Sets the request payment configuration for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketrequestpaymentput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_request_payment` to update the attributes
        of the BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketrequestpaymentreload-method)
        """


_BucketRequestPayment = BucketRequestPayment


class BucketTagging(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketTagging)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#buckettagging)
    """

    tag_set: List["TagTypeDef"]
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#buckettaggingbucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        Deletes the tags from the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#buckettaggingdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#buckettaggingget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_tagging` to update the attributes of the
        BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#buckettaggingload-method)
        """

    async def put(self, *, Tagging: "TaggingTypeDef", ExpectedBucketOwner: str = ...) -> None:
        """
        Sets the tags for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#buckettaggingput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_tagging` to update the attributes of the
        BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#buckettaggingreload-method)
        """


_BucketTagging = BucketTagging


class BucketVersioning(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioning)
    """

    status: BucketVersioningStatusType
    mfa_delete: MFADeleteStatusType
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioningbucket-method)
        """

    async def enable(
        self,
        *,
        VersioningConfiguration: "VersioningConfigurationTypeDef",
        MFA: str = ...,
        ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Sets the versioning state of an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.enable)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioningenable-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioningget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_versioning` to update the attributes of the
        BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioningload-method)
        """

    async def put(
        self,
        *,
        VersioningConfiguration: "VersioningConfigurationTypeDef",
        MFA: str = ...,
        ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Sets the versioning state of an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioningput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_versioning` to update the attributes of the
        BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioningreload-method)
        """

    async def suspend(
        self,
        *,
        VersioningConfiguration: "VersioningConfigurationTypeDef",
        MFA: str = ...,
        ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Sets the versioning state of an existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.suspend)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioningsuspend-method)
        """


_BucketVersioning = BucketVersioning


class BucketWebsite(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwebsite)
    """

    redirect_all_requests_to: RedirectAllRequestsToResponseMetadataTypeDef
    index_document: IndexDocumentResponseMetadataTypeDef
    error_document: ErrorDocumentResponseMetadataTypeDef
    routing_rules: List["RoutingRuleTypeDef"]
    bucket_name: str

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwebsitebucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        This action removes the website configuration for a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwebsitedelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwebsiteget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_website` to update the attributes of the
        BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwebsiteload-method)
        """

    async def put(
        self, *, WebsiteConfiguration: "WebsiteConfigurationTypeDef", ExpectedBucketOwner: str = ...
    ) -> None:
        """
        Sets the configuration of the website that is specified in the `website`
        subresource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwebsiteput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_website` to update the attributes of the
        BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwebsitereload-method)
        """


_BucketWebsite = BucketWebsite


class MultipartUploadPart(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadpart)
    """

    last_modified: datetime
    e_tag: str
    size: int
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    async def MultipartUpload(self) -> "_MultipartUpload":
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUploadPart.MultipartUpload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadpartmultipartupload-method)
        """

    async def copy_from(
        self,
        *,
        CopySource: str,
        CopySourceIfMatch: str = ...,
        CopySourceIfModifiedSince: Union[datetime, str] = ...,
        CopySourceIfNoneMatch: str = ...,
        CopySourceIfUnmodifiedSince: Union[datetime, str] = ...,
        CopySourceRange: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        CopySourceSSECustomerAlgorithm: str = ...,
        CopySourceSSECustomerKey: str = ...,
        CopySourceSSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...,
        ExpectedSourceBucketOwner: str = ...
    ) -> UploadPartCopyOutputTypeDef:
        """
        Uploads a part by copying data from an existing object as data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUploadPart.copy_from)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadpartcopy_from-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUploadPart.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadpartget_available_subresources-method)
        """

    async def upload(
        self,
        *,
        Body: Union[bytes, IO[bytes], StreamingBody] = ...,
        ContentLength: int = ...,
        ContentMD5: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...
    ) -> UploadPartOutputTypeDef:
        """
        Uploads a part in a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUploadPart.upload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadpartupload-method)
        """


_MultipartUploadPart = MultipartUploadPart


class ObjectAcl(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectacl)
    """

    owner: OwnerResponseMetadataTypeDef
    grants: List["GrantTypeDef"]
    request_charged: Literal["requester"]
    bucket_name: str
    object_key: str

    async def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.Object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectaclobject-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectaclget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_object_acl` to update the attributes of the
        ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectaclload-method)
        """

    async def put(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        AccessControlPolicy: "AccessControlPolicyTypeDef" = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWrite: str = ...,
        GrantWriteACP: str = ...,
        RequestPayer: Literal["requester"] = ...,
        VersionId: str = ...,
        ExpectedBucketOwner: str = ...
    ) -> PutObjectAclOutputTypeDef:
        """
        Uses the `acl` subresource to set the access control list (ACL) permissions for
        a new or existing object in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectaclput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_object_acl` to update the attributes of the
        ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectaclreload-method)
        """


_ObjectAcl = ObjectAcl


class ObjectVersion(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectversion)
    """

    e_tag: str
    size: int
    storage_class: Literal["STANDARD"]
    key: str
    version_id: str
    is_latest: bool
    last_modified: datetime
    owner: OwnerResponseMetadataTypeDef
    bucket_name: str
    object_key: str
    id: str

    async def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.Object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectversionobject-method)
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes the null version (if there is one) of an object and inserts a delete
        marker, which becomes the latest version of the object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectversiondelete-method)
        """

    async def get(
        self,
        *,
        IfMatch: str = ...,
        IfModifiedSince: Union[datetime, str] = ...,
        IfNoneMatch: str = ...,
        IfUnmodifiedSince: Union[datetime, str] = ...,
        Range: str = ...,
        ResponseCacheControl: str = ...,
        ResponseContentDisposition: str = ...,
        ResponseContentEncoding: str = ...,
        ResponseContentLanguage: str = ...,
        ResponseContentType: str = ...,
        ResponseExpires: Union[datetime, str] = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        PartNumber: int = ...,
        ExpectedBucketOwner: str = ...
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves objects from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.get)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectversionget-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectversionget_available_subresources-method)
        """

    async def head(
        self,
        *,
        IfMatch: str = ...,
        IfModifiedSince: Union[datetime, str] = ...,
        IfNoneMatch: str = ...,
        IfUnmodifiedSince: Union[datetime, str] = ...,
        Range: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        PartNumber: int = ...,
        ExpectedBucketOwner: str = ...
    ) -> HeadObjectOutputTypeDef:
        """
        The HEAD action retrieves metadata from an object without returning the object
        itself.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.head)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectversionhead-method)
        """


_ObjectVersion = ObjectVersion


class MultipartUpload(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartupload)
    """

    upload_id: str
    key: str
    initiated: datetime
    storage_class: StorageClassType
    owner: OwnerResponseMetadataTypeDef
    initiator: InitiatorResponseMetadataTypeDef
    bucket_name: str
    object_key: str
    id: str
    parts: MultipartUploadPartsCollection

    async def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.Object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadobject-method)
        """

    async def Part(self, part_number: str) -> _MultipartUploadPart:
        """
        Creates a MultipartUploadPart resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.Part)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadpart-method)
        """

    async def abort(
        self, *, RequestPayer: Literal["requester"] = ..., ExpectedBucketOwner: str = ...
    ) -> AbortMultipartUploadOutputTypeDef:
        """
        This action aborts a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.abort)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadabort-method)
        """

    async def complete(
        self,
        *,
        MultipartUpload: "CompletedMultipartUploadTypeDef" = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...
    ) -> "_Object":
        """
        Completes a multipart upload by assembling previously uploaded parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.complete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadcomplete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#multipartuploadget_available_subresources-method)
        """


_MultipartUpload = MultipartUpload


class Object(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Object)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#object)
    """

    delete_marker: bool
    accept_ranges: str
    expiration: str
    restore: str
    archive_status: ArchiveStatusType
    last_modified: datetime
    content_length: int
    e_tag: str
    missing_meta: int
    version_id: str
    cache_control: str
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    expires: datetime
    website_redirect_location: str
    server_side_encryption: ServerSideEncryptionType
    metadata: Dict[str, str]
    sse_customer_algorithm: str
    sse_customer_key_md5: str
    ssekms_key_id: str
    bucket_key_enabled: bool
    storage_class: StorageClassType
    request_charged: Literal["requester"]
    replication_status: ReplicationStatusType
    parts_count: int
    object_lock_mode: ObjectLockModeType
    object_lock_retain_until_date: datetime
    object_lock_legal_hold_status: ObjectLockLegalHoldStatusType
    bucket_name: str
    key: str

    async def Acl(self) -> _ObjectAcl:
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.Acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectacl-method)
        """

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectbucket-method)
        """

    async def MultipartUpload(self, id: str) -> _MultipartUpload:
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.MultipartUpload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectmultipartupload-method)
        """

    async def Version(self, id: str) -> _ObjectVersion:
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.Version)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectversion-method)
        """

    async def copy(
        self,
        CopySource: "CopySourceTypeDef",
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Copy an object from one S3 location to this object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.copy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectcopy-method)
        """

    async def copy_from(
        self,
        *,
        CopySource: str,
        ACL: ObjectCannedACLType = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentType: str = ...,
        CopySourceIfMatch: str = ...,
        CopySourceIfModifiedSince: Union[datetime, str] = ...,
        CopySourceIfNoneMatch: str = ...,
        CopySourceIfUnmodifiedSince: Union[datetime, str] = ...,
        Expires: Union[datetime, str] = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        MetadataDirective: MetadataDirectiveType = ...,
        TaggingDirective: TaggingDirectiveType = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        CopySourceSSECustomerAlgorithm: str = ...,
        CopySourceSSECustomerKey: str = ...,
        CopySourceSSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: Union[datetime, str] = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
        ExpectedSourceBucketOwner: str = ...
    ) -> CopyObjectOutputTypeDef:
        """
        Creates a copy of an object that is already stored in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.copy_from)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectcopy_from-method)
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        VersionId: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes the null version (if there is one) of an object and inserts a delete
        marker, which becomes the latest version of the object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectdelete-method)
        """

    async def download_file(
        self,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Download an S3 object to a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.download_file)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectdownload_file-method)
        """

    async def download_fileobj(
        self,
        Fileobj: Union[IO[Any], StreamingBody],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Download this object from S3 to a file-like object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.download_fileobj)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectdownload_fileobj-method)
        """

    async def get(
        self,
        *,
        IfMatch: str = ...,
        IfModifiedSince: Union[datetime, str] = ...,
        IfNoneMatch: str = ...,
        IfUnmodifiedSince: Union[datetime, str] = ...,
        Range: str = ...,
        ResponseCacheControl: str = ...,
        ResponseContentDisposition: str = ...,
        ResponseContentEncoding: str = ...,
        ResponseContentLanguage: str = ...,
        ResponseContentType: str = ...,
        ResponseExpires: Union[datetime, str] = ...,
        VersionId: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        PartNumber: int = ...,
        ExpectedBucketOwner: str = ...
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves objects from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.get)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectget-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectget_available_subresources-method)
        """

    async def initiate_multipart_upload(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentType: str = ...,
        Expires: Union[datetime, str] = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: Union[datetime, str] = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...
    ) -> _MultipartUpload:
        """
        This action initiates a multipart upload and returns an upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.initiate_multipart_upload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectinitiate_multipart_upload-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.head_object` to update the attributes of the Object
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectload-method)
        """

    async def put(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        Body: Union[bytes, IO[bytes], StreamingBody] = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentLength: int = ...,
        ContentMD5: str = ...,
        ContentType: str = ...,
        Expires: Union[datetime, str] = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: Union[datetime, str] = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...
    ) -> PutObjectOutputTypeDef:
        """
        Adds an object to a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.head_object` to update the attributes of the Object
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.reload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectreload-method)
        """

    async def restore_object(
        self,
        *,
        VersionId: str = ...,
        RestoreRequest: "RestoreRequestTypeDef" = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...
    ) -> RestoreObjectOutputTypeDef:
        """
        Restores an archived copy of an object back into Amazon S3 This action is not
        supported by Amazon S3 on Outposts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.restore_object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectrestore_object-method)
        """

    async def upload_file(
        self,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Upload a file to an S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.upload_file)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectupload_file-method)
        """

    async def upload_fileobj(
        self,
        Fileobj: Union[IO[Any], StreamingBody],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Upload a file-like object to this object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.upload_fileobj)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectupload_fileobj-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this Object is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.wait_until_exists)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectwait_until_exists-method)
        """

    async def wait_until_not_exists(self) -> None:
        """
        Waits until this Object is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.wait_until_not_exists)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectwait_until_not_exists-method)
        """


_Object = Object


class ObjectSummary(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummary)
    """

    last_modified: datetime
    e_tag: str
    size: int
    storage_class: ObjectStorageClassType
    owner: OwnerResponseMetadataTypeDef
    bucket_name: str
    key: str

    async def Acl(self) -> _ObjectAcl:
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.Acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryacl-method)
        """

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummarybucket-method)
        """

    async def MultipartUpload(self, id: str) -> _MultipartUpload:
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.MultipartUpload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummarymultipartupload-method)
        """

    async def Object(self) -> _Object:
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.Object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryobject-method)
        """

    async def Version(self, id: str) -> _ObjectVersion:
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.Version)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryversion-method)
        """

    async def copy_from(
        self,
        *,
        CopySource: str,
        ACL: ObjectCannedACLType = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentType: str = ...,
        CopySourceIfMatch: str = ...,
        CopySourceIfModifiedSince: Union[datetime, str] = ...,
        CopySourceIfNoneMatch: str = ...,
        CopySourceIfUnmodifiedSince: Union[datetime, str] = ...,
        Expires: Union[datetime, str] = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        MetadataDirective: MetadataDirectiveType = ...,
        TaggingDirective: TaggingDirectiveType = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        CopySourceSSECustomerAlgorithm: str = ...,
        CopySourceSSECustomerKey: str = ...,
        CopySourceSSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: Union[datetime, str] = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
        ExpectedSourceBucketOwner: str = ...
    ) -> CopyObjectOutputTypeDef:
        """
        Creates a copy of an object that is already stored in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.copy_from)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummarycopy_from-method)
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        VersionId: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes the null version (if there is one) of an object and inserts a delete
        marker, which becomes the latest version of the object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummarydelete-method)
        """

    async def get(
        self,
        *,
        IfMatch: str = ...,
        IfModifiedSince: Union[datetime, str] = ...,
        IfNoneMatch: str = ...,
        IfUnmodifiedSince: Union[datetime, str] = ...,
        Range: str = ...,
        ResponseCacheControl: str = ...,
        ResponseContentDisposition: str = ...,
        ResponseContentEncoding: str = ...,
        ResponseContentLanguage: str = ...,
        ResponseContentType: str = ...,
        ResponseExpires: Union[datetime, str] = ...,
        VersionId: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        PartNumber: int = ...,
        ExpectedBucketOwner: str = ...
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves objects from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.get)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryget-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryget_available_subresources-method)
        """

    async def initiate_multipart_upload(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentType: str = ...,
        Expires: Union[datetime, str] = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: Union[datetime, str] = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...
    ) -> _MultipartUpload:
        """
        This action initiates a multipart upload and returns an upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.initiate_multipart_upload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryinitiate_multipart_upload-method)
        """

    async def load(self) -> None:
        """
        Calls s3.Client.head_object to update the attributes of the ObjectSummary
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryload-method)
        """

    async def put(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        Body: Union[bytes, IO[bytes], StreamingBody] = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentLength: int = ...,
        ContentMD5: str = ...,
        ContentType: str = ...,
        Expires: Union[datetime, str] = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: Union[datetime, str] = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...
    ) -> PutObjectOutputTypeDef:
        """
        Adds an object to a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.put)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryput-method)
        """

    async def restore_object(
        self,
        *,
        VersionId: str = ...,
        RestoreRequest: "RestoreRequestTypeDef" = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...
    ) -> RestoreObjectOutputTypeDef:
        """
        Restores an archived copy of an object back into Amazon S3 This action is not
        supported by Amazon S3 on Outposts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.restore_object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummaryrestore_object-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this ObjectSummary is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.wait_until_exists)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummarywait_until_exists-method)
        """

    async def wait_until_not_exists(self) -> None:
        """
        Waits until this ObjectSummary is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.wait_until_not_exists)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#objectsummarywait_until_not_exists-method)
        """


_ObjectSummary = ObjectSummary


class Bucket(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Bucket)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucket)
    """

    creation_date: datetime
    name: str
    multipart_uploads: BucketMultipartUploadsCollection
    object_versions: BucketObjectVersionsCollection
    objects: BucketObjectsCollection

    async def Acl(self) -> _BucketAcl:
        """
        Creates a BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Acl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketacl-method)
        """

    async def Cors(self) -> _BucketCors:
        """
        Creates a BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Cors)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcors-method)
        """

    async def Lifecycle(self) -> _BucketLifecycle:
        """
        Creates a BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Lifecycle)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycle-method)
        """

    async def LifecycleConfiguration(self) -> _BucketLifecycleConfiguration:
        """
        Creates a BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.LifecycleConfiguration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlifecycleconfiguration-method)
        """

    async def Logging(self) -> _BucketLogging:
        """
        Creates a BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Logging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketlogging-method)
        """

    async def Notification(self) -> _BucketNotification:
        """
        Creates a BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Notification)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketnotification-method)
        """

    async def Object(self, key: str) -> _Object:
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketobject-method)
        """

    async def Policy(self) -> _BucketPolicy:
        """
        Creates a BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketpolicy-method)
        """

    async def RequestPayment(self) -> _BucketRequestPayment:
        """
        Creates a BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.RequestPayment)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketrequestpayment-method)
        """

    async def Tagging(self) -> _BucketTagging:
        """
        Creates a BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#buckettagging-method)
        """

    async def Versioning(self) -> _BucketVersioning:
        """
        Creates a BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Versioning)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketversioning-method)
        """

    async def Website(self) -> _BucketWebsite:
        """
        Creates a BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Website)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwebsite-method)
        """

    async def copy(
        self,
        CopySource: "CopySourceTypeDef",
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Copy an object from one S3 location to an object in this bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.copy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcopy-method)
        """

    async def create(
        self,
        *,
        ACL: BucketCannedACLType = ...,
        CreateBucketConfiguration: "CreateBucketConfigurationTypeDef" = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWrite: str = ...,
        GrantWriteACP: str = ...,
        ObjectLockEnabledForBucket: bool = ...,
        ObjectOwnership: ObjectOwnershipType = ...
    ) -> CreateBucketOutputTypeDef:
        """
        Creates a new S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.create)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketcreate-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        Deletes the S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketdelete-method)
        """

    async def delete_objects(
        self,
        *,
        Delete: "DeleteTypeDef",
        MFA: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...
    ) -> DeleteObjectsOutputTypeDef:
        """
        This action enables you to delete multiple objects from a bucket using a single
        HTTP request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.delete_objects)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketdelete_objects-method)
        """

    async def download_file(
        self,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Download an S3 object to a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.download_file)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketdownload_file-method)
        """

    async def download_fileobj(
        self,
        Key: str,
        Fileobj: Union[IO[Any], StreamingBody],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Download an object from this bucket to a file-like-object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.download_fileobj)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketdownload_fileobj-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls s3.Client.list_buckets() to update the attributes of the Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.load)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketload-method)
        """

    async def put_object(
        self,
        *,
        Key: str,
        ACL: ObjectCannedACLType = ...,
        Body: Union[bytes, IO[bytes], StreamingBody] = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentLength: int = ...,
        ContentMD5: str = ...,
        ContentType: str = ...,
        Expires: Union[datetime, str] = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: Union[datetime, str] = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...
    ) -> _Object:
        """
        Adds an object to a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.put_object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketput_object-method)
        """

    async def upload_file(
        self,
        Filename: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Upload a file to an S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.upload_file)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketupload_file-method)
        """

    async def upload_fileobj(
        self,
        Fileobj: Union[IO[Any], StreamingBody],
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        """
        Upload a file-like object to this bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.upload_fileobj)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketupload_fileobj-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this Bucket is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.wait_until_exists)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwait_until_exists-method)
        """

    async def wait_until_not_exists(self) -> None:
        """
        Waits until this Bucket is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.wait_until_not_exists)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#bucketwait_until_not_exists-method)
        """


_Bucket = Bucket


class S3ResourceMeta(ResourceMeta):
    client: S3Client


class S3ServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html)
    """

    meta: "S3ResourceMeta"
    buckets: ServiceResourceBucketsCollection

    async def Bucket(self, name: str) -> _Bucket:
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucket-method)
        """

    async def BucketAcl(self, bucket_name: str) -> _BucketAcl:
        """
        Creates a BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketAcl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketacl-method)
        """

    async def BucketCors(self, bucket_name: str) -> _BucketCors:
        """
        Creates a BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketCors)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketcors-method)
        """

    async def BucketLifecycle(self, bucket_name: str) -> _BucketLifecycle:
        """
        Creates a BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketlifecycle-method)
        """

    async def BucketLifecycleConfiguration(self, bucket_name: str) -> _BucketLifecycleConfiguration:
        """
        Creates a BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketlifecycleconfiguration-method)
        """

    async def BucketLogging(self, bucket_name: str) -> _BucketLogging:
        """
        Creates a BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLogging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketlogging-method)
        """

    async def BucketNotification(self, bucket_name: str) -> _BucketNotification:
        """
        Creates a BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketNotification)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketnotification-method)
        """

    async def BucketPolicy(self, bucket_name: str) -> _BucketPolicy:
        """
        Creates a BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketpolicy-method)
        """

    async def BucketRequestPayment(self, bucket_name: str) -> _BucketRequestPayment:
        """
        Creates a BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketrequestpayment-method)
        """

    async def BucketTagging(self, bucket_name: str) -> _BucketTagging:
        """
        Creates a BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketTagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebuckettagging-method)
        """

    async def BucketVersioning(self, bucket_name: str) -> _BucketVersioning:
        """
        Creates a BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketversioning-method)
        """

    async def BucketWebsite(self, bucket_name: str) -> _BucketWebsite:
        """
        Creates a BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcebucketwebsite-method)
        """

    async def MultipartUpload(self, bucket_name: str, object_key: str, id: str) -> _MultipartUpload:
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcemultipartupload-method)
        """

    async def MultipartUploadPart(
        self, bucket_name: str, object_key: str, multipart_upload_id: str, part_number: str
    ) -> _MultipartUploadPart:
        """
        Creates a MultipartUploadPart resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcemultipartuploadpart-method)
        """

    async def Object(self, bucket_name: str, key: str) -> _Object:
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Object)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourceobject-method)
        """

    async def ObjectAcl(self, bucket_name: str, object_key: str) -> _ObjectAcl:
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourceobjectacl-method)
        """

    async def ObjectSummary(self, bucket_name: str, key: str) -> _ObjectSummary:
        """
        Creates a ObjectSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourceobjectsummary-method)
        """

    async def ObjectVersion(self, bucket_name: str, object_key: str, id: str) -> _ObjectVersion:
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourceobjectversion-method)
        """

    async def create_bucket(
        self,
        *,
        Bucket: str,
        ACL: BucketCannedACLType = ...,
        CreateBucketConfiguration: "CreateBucketConfigurationTypeDef" = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWrite: str = ...,
        GrantWriteACP: str = ...,
        ObjectLockEnabledForBucket: bool = ...,
        ObjectOwnership: ObjectOwnershipType = ...
    ) -> _Bucket:
        """
        Creates a new S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.create_bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourcecreate_bucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.get_available_subresources)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource.html#s3serviceresourceget_available_subresources-method)
        """
