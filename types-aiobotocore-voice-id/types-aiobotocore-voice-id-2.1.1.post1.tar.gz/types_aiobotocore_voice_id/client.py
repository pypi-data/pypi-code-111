"""
Type annotations for voice-id service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_voice_id.client import VoiceIDClient

    session = get_session()
    async with session.create_client("voice-id") as client:
        client: VoiceIDClient
    ```
"""
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import FraudsterRegistrationJobStatusType, SpeakerEnrollmentJobStatusType
from .type_defs import (
    CreateDomainResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeFraudsterRegistrationJobResponseTypeDef,
    DescribeFraudsterResponseTypeDef,
    DescribeSpeakerEnrollmentJobResponseTypeDef,
    DescribeSpeakerResponseTypeDef,
    EnrollmentConfigTypeDef,
    EvaluateSessionResponseTypeDef,
    InputDataConfigTypeDef,
    ListDomainsResponseTypeDef,
    ListFraudsterRegistrationJobsResponseTypeDef,
    ListSpeakerEnrollmentJobsResponseTypeDef,
    ListSpeakersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OptOutSpeakerResponseTypeDef,
    OutputDataConfigTypeDef,
    RegistrationConfigTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    StartFraudsterRegistrationJobResponseTypeDef,
    StartSpeakerEnrollmentJobResponseTypeDef,
    TagTypeDef,
    UpdateDomainResponseTypeDef,
)

__all__ = ("VoiceIDClient",)


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


class VoiceIDClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        VoiceIDClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#can_paginate)
        """

    async def create_domain(
        self,
        *,
        Name: str,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef",
        ClientToken: str = ...,
        Description: str = ...,
        Tags: Sequence["TagTypeDef"] = ...
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a domain that contains all Amazon Connect Voice ID data, such as
        speakers, fraudsters, customer audio, and voiceprints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.create_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#create_domain)
        """

    async def delete_domain(self, *, DomainId: str) -> None:
        """
        Deletes the specified domain from the Amazon Connect Voice ID system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.delete_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#delete_domain)
        """

    async def delete_fraudster(self, *, DomainId: str, FraudsterId: str) -> None:
        """
        Deletes the specified fraudster from the Amazon Connect Voice ID system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.delete_fraudster)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#delete_fraudster)
        """

    async def delete_speaker(self, *, DomainId: str, SpeakerId: str) -> None:
        """
        Deletes the specified speaker from the Amazon Connect Voice ID system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.delete_speaker)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#delete_speaker)
        """

    async def describe_domain(self, *, DomainId: str) -> DescribeDomainResponseTypeDef:
        """
        Describes the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.describe_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#describe_domain)
        """

    async def describe_fraudster(
        self, *, DomainId: str, FraudsterId: str
    ) -> DescribeFraudsterResponseTypeDef:
        """
        Describes the specified fraudster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.describe_fraudster)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#describe_fraudster)
        """

    async def describe_fraudster_registration_job(
        self, *, DomainId: str, JobId: str
    ) -> DescribeFraudsterRegistrationJobResponseTypeDef:
        """
        Describes the specified fraudster registration job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.describe_fraudster_registration_job)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#describe_fraudster_registration_job)
        """

    async def describe_speaker(
        self, *, DomainId: str, SpeakerId: str
    ) -> DescribeSpeakerResponseTypeDef:
        """
        Describes the specified speaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.describe_speaker)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#describe_speaker)
        """

    async def describe_speaker_enrollment_job(
        self, *, DomainId: str, JobId: str
    ) -> DescribeSpeakerEnrollmentJobResponseTypeDef:
        """
        Describes the specified speaker enrollment job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.describe_speaker_enrollment_job)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#describe_speaker_enrollment_job)
        """

    async def evaluate_session(
        self, *, DomainId: str, SessionNameOrId: str
    ) -> EvaluateSessionResponseTypeDef:
        """
        Evaluates a specified session based on audio data accumulated during a streaming
        Amazon Connect Voice ID call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.evaluate_session)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#evaluate_session)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#generate_presigned_url)
        """

    async def list_domains(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListDomainsResponseTypeDef:
        """
        Lists all the domains in the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.list_domains)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#list_domains)
        """

    async def list_fraudster_registration_jobs(
        self,
        *,
        DomainId: str,
        JobStatus: FraudsterRegistrationJobStatusType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListFraudsterRegistrationJobsResponseTypeDef:
        """
        Lists all the fraudster registration jobs in the domain with the given
        `JobStatus`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.list_fraudster_registration_jobs)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#list_fraudster_registration_jobs)
        """

    async def list_speaker_enrollment_jobs(
        self,
        *,
        DomainId: str,
        JobStatus: SpeakerEnrollmentJobStatusType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListSpeakerEnrollmentJobsResponseTypeDef:
        """
        Lists all the speaker enrollment jobs in the domain with the specified
        `JobStatus`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.list_speaker_enrollment_jobs)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#list_speaker_enrollment_jobs)
        """

    async def list_speakers(
        self, *, DomainId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListSpeakersResponseTypeDef:
        """
        Lists all speakers in a specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.list_speakers)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#list_speakers)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a specified Voice ID resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#list_tags_for_resource)
        """

    async def opt_out_speaker(
        self, *, DomainId: str, SpeakerId: str
    ) -> OptOutSpeakerResponseTypeDef:
        """
        Opts out a speaker from Voice ID system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.opt_out_speaker)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#opt_out_speaker)
        """

    async def start_fraudster_registration_job(
        self,
        *,
        DataAccessRoleArn: str,
        DomainId: str,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        ClientToken: str = ...,
        JobName: str = ...,
        RegistrationConfig: "RegistrationConfigTypeDef" = ...
    ) -> StartFraudsterRegistrationJobResponseTypeDef:
        """
        Starts a new batch fraudster registration job using provided details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.start_fraudster_registration_job)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#start_fraudster_registration_job)
        """

    async def start_speaker_enrollment_job(
        self,
        *,
        DataAccessRoleArn: str,
        DomainId: str,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        ClientToken: str = ...,
        EnrollmentConfig: "EnrollmentConfigTypeDef" = ...,
        JobName: str = ...
    ) -> StartSpeakerEnrollmentJobResponseTypeDef:
        """
        Starts a new batch speaker enrollment job using specified details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.start_speaker_enrollment_job)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#start_speaker_enrollment_job)
        """

    async def tag_resource(
        self, *, ResourceArn: str, Tags: Sequence["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Tags an Amazon Connect Voice ID resource with the provided list of tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.tag_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes specified tags from a specified Amazon Connect Voice ID resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.untag_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#untag_resource)
        """

    async def update_domain(
        self,
        *,
        DomainId: str,
        Name: str,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef",
        Description: str = ...
    ) -> UpdateDomainResponseTypeDef:
        """
        Updates the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client.update_domain)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html#update_domain)
        """

    async def __aenter__(self) -> "VoiceIDClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html#VoiceID.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_voice_id/client.html)
        """
