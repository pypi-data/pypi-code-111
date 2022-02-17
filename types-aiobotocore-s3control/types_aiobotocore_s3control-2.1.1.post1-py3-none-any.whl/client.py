"""
Type annotations for s3control service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_s3control.client import S3ControlClient

    session = get_session()
    async with session.create_client("s3control") as client:
        client: S3ControlClient
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import BucketCannedACLType, JobStatusType, RequestedJobStatusType
from .paginator import ListAccessPointsForObjectLambdaPaginator
from .type_defs import (
    CreateAccessPointForObjectLambdaResultTypeDef,
    CreateAccessPointResultTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketResultTypeDef,
    CreateJobResultTypeDef,
    CreateMultiRegionAccessPointInputTypeDef,
    CreateMultiRegionAccessPointResultTypeDef,
    DeleteMultiRegionAccessPointInputTypeDef,
    DeleteMultiRegionAccessPointResultTypeDef,
    DescribeJobResultTypeDef,
    DescribeMultiRegionAccessPointOperationResultTypeDef,
    GetAccessPointConfigurationForObjectLambdaResultTypeDef,
    GetAccessPointForObjectLambdaResultTypeDef,
    GetAccessPointPolicyForObjectLambdaResultTypeDef,
    GetAccessPointPolicyResultTypeDef,
    GetAccessPointPolicyStatusForObjectLambdaResultTypeDef,
    GetAccessPointPolicyStatusResultTypeDef,
    GetAccessPointResultTypeDef,
    GetBucketLifecycleConfigurationResultTypeDef,
    GetBucketPolicyResultTypeDef,
    GetBucketResultTypeDef,
    GetBucketTaggingResultTypeDef,
    GetJobTaggingResultTypeDef,
    GetMultiRegionAccessPointPolicyResultTypeDef,
    GetMultiRegionAccessPointPolicyStatusResultTypeDef,
    GetMultiRegionAccessPointResultTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    GetStorageLensConfigurationResultTypeDef,
    GetStorageLensConfigurationTaggingResultTypeDef,
    JobManifestTypeDef,
    JobOperationTypeDef,
    JobReportTypeDef,
    LifecycleConfigurationTypeDef,
    ListAccessPointsForObjectLambdaResultTypeDef,
    ListAccessPointsResultTypeDef,
    ListJobsResultTypeDef,
    ListMultiRegionAccessPointsResultTypeDef,
    ListRegionalBucketsResultTypeDef,
    ListStorageLensConfigurationsResultTypeDef,
    ObjectLambdaConfigurationTypeDef,
    PublicAccessBlockConfigurationTypeDef,
    PutMultiRegionAccessPointPolicyInputTypeDef,
    PutMultiRegionAccessPointPolicyResultTypeDef,
    S3TagTypeDef,
    StorageLensConfigurationTypeDef,
    StorageLensTagTypeDef,
    TaggingTypeDef,
    UpdateJobPriorityResultTypeDef,
    UpdateJobStatusResultTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("S3ControlClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    BucketAlreadyExists: Type[BotocoreClientError]
    BucketAlreadyOwnedByYou: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    JobStatusException: Type[BotocoreClientError]
    NoSuchPublicAccessBlockConfiguration: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class S3ControlClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        S3ControlClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#can_paginate)
        """

    async def create_access_point(
        self,
        *,
        AccountId: str,
        Name: str,
        Bucket: str,
        VpcConfiguration: "VpcConfigurationTypeDef" = ...,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef" = ...
    ) -> CreateAccessPointResultTypeDef:
        """
        Creates an access point and associates it with the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_access_point)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#create_access_point)
        """

    async def create_access_point_for_object_lambda(
        self, *, AccountId: str, Name: str, Configuration: "ObjectLambdaConfigurationTypeDef"
    ) -> CreateAccessPointForObjectLambdaResultTypeDef:
        """
        Creates an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_access_point_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#create_access_point_for_object_lambda)
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
        OutpostId: str = ...
    ) -> CreateBucketResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#create_bucket)
        """

    async def create_job(
        self,
        *,
        AccountId: str,
        Operation: "JobOperationTypeDef",
        Report: "JobReportTypeDef",
        ClientRequestToken: str,
        Manifest: "JobManifestTypeDef",
        Priority: int,
        RoleArn: str,
        ConfirmationRequired: bool = ...,
        Description: str = ...,
        Tags: Sequence["S3TagTypeDef"] = ...
    ) -> CreateJobResultTypeDef:
        """
        You can use S3 Batch Operations to perform large-scale batch actions on Amazon
        S3 objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_job)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#create_job)
        """

    async def create_multi_region_access_point(
        self,
        *,
        AccountId: str,
        ClientToken: str,
        Details: "CreateMultiRegionAccessPointInputTypeDef"
    ) -> CreateMultiRegionAccessPointResultTypeDef:
        """
        Creates a Multi-Region Access Point and associates it with the specified
        buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_multi_region_access_point)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#create_multi_region_access_point)
        """

    async def delete_access_point(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_access_point)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_access_point)
        """

    async def delete_access_point_for_object_lambda(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the specified Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_access_point_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_access_point_for_object_lambda)
        """

    async def delete_access_point_policy(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the access point policy for the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_access_point_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_access_point_policy)
        """

    async def delete_access_point_policy_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> None:
        """
        Removes the resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_access_point_policy_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_access_point_policy_for_object_lambda)
        """

    async def delete_bucket(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_bucket)
        """

    async def delete_bucket_lifecycle_configuration(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_bucket_lifecycle_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_bucket_lifecycle_configuration)
        """

    async def delete_bucket_policy(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_bucket_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_bucket_policy)
        """

    async def delete_bucket_tagging(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_bucket_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_bucket_tagging)
        """

    async def delete_job_tagging(self, *, AccountId: str, JobId: str) -> Dict[str, Any]:
        """
        Removes the entire tag set from the specified S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_job_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_job_tagging)
        """

    async def delete_multi_region_access_point(
        self,
        *,
        AccountId: str,
        ClientToken: str,
        Details: "DeleteMultiRegionAccessPointInputTypeDef"
    ) -> DeleteMultiRegionAccessPointResultTypeDef:
        """
        Deletes a Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_multi_region_access_point)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_multi_region_access_point)
        """

    async def delete_public_access_block(self, *, AccountId: str) -> None:
        """
        Removes the `PublicAccessBlock` configuration for an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_public_access_block)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_public_access_block)
        """

    async def delete_storage_lens_configuration(self, *, ConfigId: str, AccountId: str) -> None:
        """
        Deletes the Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_storage_lens_configuration)
        """

    async def delete_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str
    ) -> Dict[str, Any]:
        """
        Deletes the Amazon S3 Storage Lens configuration tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#delete_storage_lens_configuration_tagging)
        """

    async def describe_job(self, *, AccountId: str, JobId: str) -> DescribeJobResultTypeDef:
        """
        Retrieves the configuration parameters and status for a Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.describe_job)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#describe_job)
        """

    async def describe_multi_region_access_point_operation(
        self, *, AccountId: str, RequestTokenARN: str
    ) -> DescribeMultiRegionAccessPointOperationResultTypeDef:
        """
        Retrieves the status of an asynchronous request to manage a Multi-Region Access
        Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.describe_multi_region_access_point_operation)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#describe_multi_region_access_point_operation)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#generate_presigned_url)
        """

    async def get_access_point(self, *, AccountId: str, Name: str) -> GetAccessPointResultTypeDef:
        """
        Returns configuration information about the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_access_point)
        """

    async def get_access_point_configuration_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointConfigurationForObjectLambdaResultTypeDef:
        """
        Returns configuration for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_configuration_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_access_point_configuration_for_object_lambda)
        """

    async def get_access_point_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointForObjectLambdaResultTypeDef:
        """
        Returns configuration information about the specified Object Lambda Access Point
        The following actions are related to `GetAccessPointForObjectLambda`  *
        `CreateAccessPointForObjectLambda
        <https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.htm...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_access_point_for_object_lambda)
        """

    async def get_access_point_policy(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyResultTypeDef:
        """
        Returns the access point policy associated with the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_access_point_policy)
        """

    async def get_access_point_policy_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyForObjectLambdaResultTypeDef:
        """
        Returns the resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_policy_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_access_point_policy_for_object_lambda)
        """

    async def get_access_point_policy_status(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusResultTypeDef:
        """
        Indicates whether the specified access point currently has a policy that allows
        public access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_access_point_policy_status)
        """

    async def get_access_point_policy_status_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusForObjectLambdaResultTypeDef:
        """
        Returns the status of the resource policy associated with an Object Lambda
        Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_access_point_policy_status_for_object_lambda)
        """

    async def get_bucket(self, *, AccountId: str, Bucket: str) -> GetBucketResultTypeDef:
        """
        Gets an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_bucket)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_bucket)
        """

    async def get_bucket_lifecycle_configuration(
        self, *, AccountId: str, Bucket: str
    ) -> GetBucketLifecycleConfigurationResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_bucket_lifecycle_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_bucket_lifecycle_configuration)
        """

    async def get_bucket_policy(
        self, *, AccountId: str, Bucket: str
    ) -> GetBucketPolicyResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_bucket_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_bucket_policy)
        """

    async def get_bucket_tagging(
        self, *, AccountId: str, Bucket: str
    ) -> GetBucketTaggingResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_bucket_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_bucket_tagging)
        """

    async def get_job_tagging(self, *, AccountId: str, JobId: str) -> GetJobTaggingResultTypeDef:
        """
        Returns the tags on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_job_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_job_tagging)
        """

    async def get_multi_region_access_point(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointResultTypeDef:
        """
        Returns configuration information about the specified Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_multi_region_access_point)
        """

    async def get_multi_region_access_point_policy(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointPolicyResultTypeDef:
        """
        Returns the access control policy of the specified Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_multi_region_access_point_policy)
        """

    async def get_multi_region_access_point_policy_status(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointPolicyStatusResultTypeDef:
        """
        Indicates whether the specified Multi-Region Access Point has an access control
        policy that allows public access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point_policy_status)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_multi_region_access_point_policy_status)
        """

    async def get_public_access_block(self, *, AccountId: str) -> GetPublicAccessBlockOutputTypeDef:
        """
        Retrieves the `PublicAccessBlock` configuration for an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_public_access_block)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_public_access_block)
        """

    async def get_storage_lens_configuration(
        self, *, ConfigId: str, AccountId: str
    ) -> GetStorageLensConfigurationResultTypeDef:
        """
        Gets the Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_storage_lens_configuration)
        """

    async def get_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str
    ) -> GetStorageLensConfigurationTaggingResultTypeDef:
        """
        Gets the tags of Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_storage_lens_configuration_tagging)
        """

    async def list_access_points(
        self, *, AccountId: str, Bucket: str = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> ListAccessPointsResultTypeDef:
        """
        Returns a list of the access points currently associated with the specified
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_access_points)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#list_access_points)
        """

    async def list_access_points_for_object_lambda(
        self, *, AccountId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListAccessPointsForObjectLambdaResultTypeDef:
        """
        Returns a list of the access points associated with the Object Lambda Access
        Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_access_points_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#list_access_points_for_object_lambda)
        """

    async def list_jobs(
        self,
        *,
        AccountId: str,
        JobStatuses: Sequence[JobStatusType] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListJobsResultTypeDef:
        """
        Lists current S3 Batch Operations jobs and jobs that have ended within the last
        30 days for the Amazon Web Services account making the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_jobs)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#list_jobs)
        """

    async def list_multi_region_access_points(
        self, *, AccountId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMultiRegionAccessPointsResultTypeDef:
        """
        Returns a list of the Multi-Region Access Points currently associated with the
        specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_multi_region_access_points)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#list_multi_region_access_points)
        """

    async def list_regional_buckets(
        self, *, AccountId: str, NextToken: str = ..., MaxResults: int = ..., OutpostId: str = ...
    ) -> ListRegionalBucketsResultTypeDef:
        """
        Returns a list of all Outposts buckets in an Outpost that are owned by the
        authenticated sender of the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_regional_buckets)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#list_regional_buckets)
        """

    async def list_storage_lens_configurations(
        self, *, AccountId: str, NextToken: str = ...
    ) -> ListStorageLensConfigurationsResultTypeDef:
        """
        Gets a list of Amazon S3 Storage Lens configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.list_storage_lens_configurations)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#list_storage_lens_configurations)
        """

    async def put_access_point_configuration_for_object_lambda(
        self, *, AccountId: str, Name: str, Configuration: "ObjectLambdaConfigurationTypeDef"
    ) -> None:
        """
        Replaces configuration for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_access_point_configuration_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_access_point_configuration_for_object_lambda)
        """

    async def put_access_point_policy(self, *, AccountId: str, Name: str, Policy: str) -> None:
        """
        Associates an access policy with the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_access_point_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_access_point_policy)
        """

    async def put_access_point_policy_for_object_lambda(
        self, *, AccountId: str, Name: str, Policy: str
    ) -> None:
        """
        Creates or replaces resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_access_point_policy_for_object_lambda)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_access_point_policy_for_object_lambda)
        """

    async def put_bucket_lifecycle_configuration(
        self,
        *,
        AccountId: str,
        Bucket: str,
        LifecycleConfiguration: "LifecycleConfigurationTypeDef" = ...
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_bucket_lifecycle_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_bucket_lifecycle_configuration)
        """

    async def put_bucket_policy(
        self, *, AccountId: str, Bucket: str, Policy: str, ConfirmRemoveSelfBucketAccess: bool = ...
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_bucket_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_bucket_policy)
        """

    async def put_bucket_tagging(
        self, *, AccountId: str, Bucket: str, Tagging: "TaggingTypeDef"
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_bucket_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_bucket_tagging)
        """

    async def put_job_tagging(
        self, *, AccountId: str, JobId: str, Tags: Sequence["S3TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Sets the supplied tag-set on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_job_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_job_tagging)
        """

    async def put_multi_region_access_point_policy(
        self,
        *,
        AccountId: str,
        ClientToken: str,
        Details: "PutMultiRegionAccessPointPolicyInputTypeDef"
    ) -> PutMultiRegionAccessPointPolicyResultTypeDef:
        """
        Associates an access control policy with the specified Multi-Region Access
        Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_multi_region_access_point_policy)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_multi_region_access_point_policy)
        """

    async def put_public_access_block(
        self,
        *,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef",
        AccountId: str
    ) -> None:
        """
        Creates or modifies the `PublicAccessBlock` configuration for an Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_public_access_block)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_public_access_block)
        """

    async def put_storage_lens_configuration(
        self,
        *,
        ConfigId: str,
        AccountId: str,
        StorageLensConfiguration: "StorageLensConfigurationTypeDef",
        Tags: Sequence["StorageLensTagTypeDef"] = ...
    ) -> None:
        """
        Puts an Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_storage_lens_configuration)
        """

    async def put_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str, Tags: Sequence["StorageLensTagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Put or replace tags on an existing Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration_tagging)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#put_storage_lens_configuration_tagging)
        """

    async def update_job_priority(
        self, *, AccountId: str, JobId: str, Priority: int
    ) -> UpdateJobPriorityResultTypeDef:
        """
        Updates an existing S3 Batch Operations job's priority.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.update_job_priority)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#update_job_priority)
        """

    async def update_job_status(
        self,
        *,
        AccountId: str,
        JobId: str,
        RequestedJobStatus: RequestedJobStatusType,
        StatusUpdateReason: str = ...
    ) -> UpdateJobStatusResultTypeDef:
        """
        Updates the status for the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.update_job_status)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#update_job_status)
        """

    def get_paginator(
        self, operation_name: Literal["list_access_points_for_object_lambda"]
    ) -> ListAccessPointsForObjectLambdaPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html#get_paginator)
        """

    async def __aenter__(self) -> "S3ControlClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/client.html)
        """
