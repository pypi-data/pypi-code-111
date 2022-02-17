"""
Type annotations for medialive service client.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_medialive.client import MediaLiveClient

    session = get_session()
    async with session.create_client("medialive") as client:
        client: MediaLiveClient
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import ChannelClassType, InputTypeType, LogLevelType
from .paginator import (
    DescribeSchedulePaginator,
    ListChannelsPaginator,
    ListInputDevicesPaginator,
    ListInputDeviceTransfersPaginator,
    ListInputSecurityGroupsPaginator,
    ListInputsPaginator,
    ListMultiplexesPaginator,
    ListMultiplexProgramsPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
)
from .type_defs import (
    BatchDeleteResponseTypeDef,
    BatchScheduleActionCreateRequestTypeDef,
    BatchScheduleActionDeleteRequestTypeDef,
    BatchStartResponseTypeDef,
    BatchStopResponseTypeDef,
    BatchUpdateScheduleResponseTypeDef,
    CdiInputSpecificationTypeDef,
    CreateChannelResponseTypeDef,
    CreateInputResponseTypeDef,
    CreateInputSecurityGroupResponseTypeDef,
    CreateMultiplexProgramResponseTypeDef,
    CreateMultiplexResponseTypeDef,
    CreatePartnerInputResponseTypeDef,
    DeleteChannelResponseTypeDef,
    DeleteMultiplexProgramResponseTypeDef,
    DeleteMultiplexResponseTypeDef,
    DeleteReservationResponseTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeInputDeviceResponseTypeDef,
    DescribeInputDeviceThumbnailResponseTypeDef,
    DescribeInputResponseTypeDef,
    DescribeInputSecurityGroupResponseTypeDef,
    DescribeMultiplexProgramResponseTypeDef,
    DescribeMultiplexResponseTypeDef,
    DescribeOfferingResponseTypeDef,
    DescribeReservationResponseTypeDef,
    DescribeScheduleResponseTypeDef,
    EncoderSettingsTypeDef,
    InputAttachmentTypeDef,
    InputDestinationRequestTypeDef,
    InputDeviceConfigurableSettingsTypeDef,
    InputDeviceRequestTypeDef,
    InputDeviceSettingsTypeDef,
    InputSourceRequestTypeDef,
    InputSpecificationTypeDef,
    InputVpcRequestTypeDef,
    InputWhitelistRuleCidrTypeDef,
    ListChannelsResponseTypeDef,
    ListInputDevicesResponseTypeDef,
    ListInputDeviceTransfersResponseTypeDef,
    ListInputSecurityGroupsResponseTypeDef,
    ListInputsResponseTypeDef,
    ListMultiplexesResponseTypeDef,
    ListMultiplexProgramsResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MediaConnectFlowRequestTypeDef,
    MultiplexProgramSettingsTypeDef,
    MultiplexSettingsTypeDef,
    OutputDestinationTypeDef,
    PurchaseOfferingResponseTypeDef,
    StartChannelResponseTypeDef,
    StartMultiplexResponseTypeDef,
    StopChannelResponseTypeDef,
    StopMultiplexResponseTypeDef,
    UpdateChannelClassResponseTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateInputDeviceResponseTypeDef,
    UpdateInputResponseTypeDef,
    UpdateInputSecurityGroupResponseTypeDef,
    UpdateMultiplexProgramResponseTypeDef,
    UpdateMultiplexResponseTypeDef,
    UpdateReservationResponseTypeDef,
    VpcOutputSettingsTypeDef,
)
from .waiter import (
    ChannelCreatedWaiter,
    ChannelDeletedWaiter,
    ChannelRunningWaiter,
    ChannelStoppedWaiter,
    InputAttachedWaiter,
    InputDeletedWaiter,
    InputDetachedWaiter,
    MultiplexCreatedWaiter,
    MultiplexDeletedWaiter,
    MultiplexRunningWaiter,
    MultiplexStoppedWaiter,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaLiveClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadGatewayException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GatewayTimeoutException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]


class MediaLiveClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaLiveClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.exceptions)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#exceptions)
        """

    async def accept_input_device_transfer(self, *, InputDeviceId: str) -> Dict[str, Any]:
        """
        Accept an incoming input device transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.accept_input_device_transfer)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#accept_input_device_transfer)
        """

    async def batch_delete(
        self,
        *,
        ChannelIds: Sequence[str] = ...,
        InputIds: Sequence[str] = ...,
        InputSecurityGroupIds: Sequence[str] = ...,
        MultiplexIds: Sequence[str] = ...
    ) -> BatchDeleteResponseTypeDef:
        """
        Starts delete of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.batch_delete)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#batch_delete)
        """

    async def batch_start(
        self, *, ChannelIds: Sequence[str] = ..., MultiplexIds: Sequence[str] = ...
    ) -> BatchStartResponseTypeDef:
        """
        Starts existing resources See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/BatchStart).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.batch_start)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#batch_start)
        """

    async def batch_stop(
        self, *, ChannelIds: Sequence[str] = ..., MultiplexIds: Sequence[str] = ...
    ) -> BatchStopResponseTypeDef:
        """
        Stops running resources See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/BatchStop).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.batch_stop)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#batch_stop)
        """

    async def batch_update_schedule(
        self,
        *,
        ChannelId: str,
        Creates: "BatchScheduleActionCreateRequestTypeDef" = ...,
        Deletes: "BatchScheduleActionDeleteRequestTypeDef" = ...
    ) -> BatchUpdateScheduleResponseTypeDef:
        """
        Update a channel schedule See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/BatchUpdateSchedule).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.batch_update_schedule)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#batch_update_schedule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.can_paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#can_paginate)
        """

    async def cancel_input_device_transfer(self, *, InputDeviceId: str) -> Dict[str, Any]:
        """
        Cancel an input device transfer that you have requested.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.cancel_input_device_transfer)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#cancel_input_device_transfer)
        """

    async def claim_device(self, *, Id: str = ...) -> Dict[str, Any]:
        """
        Send a request to claim an AWS Elemental device that you have purchased from a
        third-party vendor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.claim_device)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#claim_device)
        """

    async def create_channel(
        self,
        *,
        CdiInputSpecification: "CdiInputSpecificationTypeDef" = ...,
        ChannelClass: ChannelClassType = ...,
        Destinations: Sequence["OutputDestinationTypeDef"] = ...,
        EncoderSettings: "EncoderSettingsTypeDef" = ...,
        InputAttachments: Sequence["InputAttachmentTypeDef"] = ...,
        InputSpecification: "InputSpecificationTypeDef" = ...,
        LogLevel: LogLevelType = ...,
        Name: str = ...,
        RequestId: str = ...,
        Reserved: str = ...,
        RoleArn: str = ...,
        Tags: Mapping[str, str] = ...,
        Vpc: "VpcOutputSettingsTypeDef" = ...
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a new channel See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/CreateChannel).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_channel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#create_channel)
        """

    async def create_input(
        self,
        *,
        Destinations: Sequence["InputDestinationRequestTypeDef"] = ...,
        InputDevices: Sequence["InputDeviceSettingsTypeDef"] = ...,
        InputSecurityGroups: Sequence[str] = ...,
        MediaConnectFlows: Sequence["MediaConnectFlowRequestTypeDef"] = ...,
        Name: str = ...,
        RequestId: str = ...,
        RoleArn: str = ...,
        Sources: Sequence["InputSourceRequestTypeDef"] = ...,
        Tags: Mapping[str, str] = ...,
        Type: InputTypeType = ...,
        Vpc: "InputVpcRequestTypeDef" = ...
    ) -> CreateInputResponseTypeDef:
        """
        Create an input See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/CreateInput).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_input)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#create_input)
        """

    async def create_input_security_group(
        self,
        *,
        Tags: Mapping[str, str] = ...,
        WhitelistRules: Sequence["InputWhitelistRuleCidrTypeDef"] = ...
    ) -> CreateInputSecurityGroupResponseTypeDef:
        """
        Creates a Input Security Group See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/CreateInputSecurityGroup).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_input_security_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#create_input_security_group)
        """

    async def create_multiplex(
        self,
        *,
        AvailabilityZones: Sequence[str],
        MultiplexSettings: "MultiplexSettingsTypeDef",
        Name: str,
        RequestId: str,
        Tags: Mapping[str, str] = ...
    ) -> CreateMultiplexResponseTypeDef:
        """
        Create a new multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_multiplex)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#create_multiplex)
        """

    async def create_multiplex_program(
        self,
        *,
        MultiplexId: str,
        MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef",
        ProgramName: str,
        RequestId: str
    ) -> CreateMultiplexProgramResponseTypeDef:
        """
        Create a new program in the multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_multiplex_program)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#create_multiplex_program)
        """

    async def create_partner_input(
        self, *, InputId: str, RequestId: str = ..., Tags: Mapping[str, str] = ...
    ) -> CreatePartnerInputResponseTypeDef:
        """
        Create a partner input See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/CreatePartnerInput).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_partner_input)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#create_partner_input)
        """

    async def create_tags(self, *, ResourceArn: str, Tags: Mapping[str, str] = ...) -> None:
        """
        Create tags for a resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/CreateTags).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_tags)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#create_tags)
        """

    async def delete_channel(self, *, ChannelId: str) -> DeleteChannelResponseTypeDef:
        """
        Starts deletion of channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_channel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#delete_channel)
        """

    async def delete_input(self, *, InputId: str) -> Dict[str, Any]:
        """
        Deletes the input end point See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DeleteInput).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_input)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#delete_input)
        """

    async def delete_input_security_group(self, *, InputSecurityGroupId: str) -> Dict[str, Any]:
        """
        Deletes an Input Security Group See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DeleteInputSecurityGroup).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_input_security_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#delete_input_security_group)
        """

    async def delete_multiplex(self, *, MultiplexId: str) -> DeleteMultiplexResponseTypeDef:
        """
        Delete a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_multiplex)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#delete_multiplex)
        """

    async def delete_multiplex_program(
        self, *, MultiplexId: str, ProgramName: str
    ) -> DeleteMultiplexProgramResponseTypeDef:
        """
        Delete a program from a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_multiplex_program)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#delete_multiplex_program)
        """

    async def delete_reservation(self, *, ReservationId: str) -> DeleteReservationResponseTypeDef:
        """
        Delete an expired reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_reservation)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#delete_reservation)
        """

    async def delete_schedule(self, *, ChannelId: str) -> Dict[str, Any]:
        """
        Delete all schedule actions on a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_schedule)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#delete_schedule)
        """

    async def delete_tags(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> None:
        """
        Removes tags for a resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DeleteTags).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_tags)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#delete_tags)
        """

    async def describe_channel(self, *, ChannelId: str) -> DescribeChannelResponseTypeDef:
        """
        Gets details about a channel See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeChannel).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_channel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_channel)
        """

    async def describe_input(self, *, InputId: str) -> DescribeInputResponseTypeDef:
        """
        Produces details about an input See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeInput).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_input)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_input)
        """

    async def describe_input_device(
        self, *, InputDeviceId: str
    ) -> DescribeInputDeviceResponseTypeDef:
        """
        Gets the details for the input device See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeInputDevice).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_input_device)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_input_device)
        """

    async def describe_input_device_thumbnail(
        self, *, InputDeviceId: str, Accept: Literal["image/jpeg"]
    ) -> DescribeInputDeviceThumbnailResponseTypeDef:
        """
        Get the latest thumbnail data for the input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_input_device_thumbnail)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_input_device_thumbnail)
        """

    async def describe_input_security_group(
        self, *, InputSecurityGroupId: str
    ) -> DescribeInputSecurityGroupResponseTypeDef:
        """
        Produces a summary of an Input Security Group See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeInputSecurityGroup).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_input_security_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_input_security_group)
        """

    async def describe_multiplex(self, *, MultiplexId: str) -> DescribeMultiplexResponseTypeDef:
        """
        Gets details about a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_multiplex)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_multiplex)
        """

    async def describe_multiplex_program(
        self, *, MultiplexId: str, ProgramName: str
    ) -> DescribeMultiplexProgramResponseTypeDef:
        """
        Get the details for a program in a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_multiplex_program)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_multiplex_program)
        """

    async def describe_offering(self, *, OfferingId: str) -> DescribeOfferingResponseTypeDef:
        """
        Get details for an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_offering)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_offering)
        """

    async def describe_reservation(
        self, *, ReservationId: str
    ) -> DescribeReservationResponseTypeDef:
        """
        Get details for a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_reservation)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_reservation)
        """

    async def describe_schedule(
        self, *, ChannelId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> DescribeScheduleResponseTypeDef:
        """
        Get a channel schedule See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeSchedule).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_schedule)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#describe_schedule)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#generate_presigned_url)
        """

    async def list_channels(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListChannelsResponseTypeDef:
        """
        Produces list of channels that have been created See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListChannels).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_channels)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_channels)
        """

    async def list_input_device_transfers(
        self, *, TransferType: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListInputDeviceTransfersResponseTypeDef:
        """
        List input devices that are currently being transferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_input_device_transfers)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_input_device_transfers)
        """

    async def list_input_devices(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListInputDevicesResponseTypeDef:
        """
        List input devices See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListInputDevices).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_input_devices)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_input_devices)
        """

    async def list_input_security_groups(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListInputSecurityGroupsResponseTypeDef:
        """
        Produces a list of Input Security Groups for an account See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListInputSecurityGroups).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_input_security_groups)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_input_security_groups)
        """

    async def list_inputs(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListInputsResponseTypeDef:
        """
        Produces list of inputs that have been created See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListInputs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_inputs)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_inputs)
        """

    async def list_multiplex_programs(
        self, *, MultiplexId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListMultiplexProgramsResponseTypeDef:
        """
        List the programs that currently exist for a specific multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_multiplex_programs)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_multiplex_programs)
        """

    async def list_multiplexes(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListMultiplexesResponseTypeDef:
        """
        Retrieve a list of the existing multiplexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_multiplexes)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_multiplexes)
        """

    async def list_offerings(
        self,
        *,
        ChannelClass: str = ...,
        ChannelConfiguration: str = ...,
        Codec: str = ...,
        Duration: str = ...,
        MaxResults: int = ...,
        MaximumBitrate: str = ...,
        MaximumFramerate: str = ...,
        NextToken: str = ...,
        Resolution: str = ...,
        ResourceType: str = ...,
        SpecialFeature: str = ...,
        VideoQuality: str = ...
    ) -> ListOfferingsResponseTypeDef:
        """
        List offerings available for purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_offerings)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_offerings)
        """

    async def list_reservations(
        self,
        *,
        ChannelClass: str = ...,
        Codec: str = ...,
        MaxResults: int = ...,
        MaximumBitrate: str = ...,
        MaximumFramerate: str = ...,
        NextToken: str = ...,
        Resolution: str = ...,
        ResourceType: str = ...,
        SpecialFeature: str = ...,
        VideoQuality: str = ...
    ) -> ListReservationsResponseTypeDef:
        """
        List purchased reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_reservations)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_reservations)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Produces list of tags that have been created for a resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListTagsForResource).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#list_tags_for_resource)
        """

    async def purchase_offering(
        self,
        *,
        Count: int,
        OfferingId: str,
        Name: str = ...,
        RequestId: str = ...,
        Start: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> PurchaseOfferingResponseTypeDef:
        """
        Purchase an offering and create a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.purchase_offering)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#purchase_offering)
        """

    async def reject_input_device_transfer(self, *, InputDeviceId: str) -> Dict[str, Any]:
        """
        Reject the transfer of the specified input device to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.reject_input_device_transfer)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#reject_input_device_transfer)
        """

    async def start_channel(self, *, ChannelId: str) -> StartChannelResponseTypeDef:
        """
        Starts an existing channel See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/StartChannel).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.start_channel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#start_channel)
        """

    async def start_multiplex(self, *, MultiplexId: str) -> StartMultiplexResponseTypeDef:
        """
        Start (run) the multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.start_multiplex)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#start_multiplex)
        """

    async def stop_channel(self, *, ChannelId: str) -> StopChannelResponseTypeDef:
        """
        Stops a running channel See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/StopChannel).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.stop_channel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#stop_channel)
        """

    async def stop_multiplex(self, *, MultiplexId: str) -> StopMultiplexResponseTypeDef:
        """
        Stops a running multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.stop_multiplex)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#stop_multiplex)
        """

    async def transfer_input_device(
        self,
        *,
        InputDeviceId: str,
        TargetCustomerId: str = ...,
        TargetRegion: str = ...,
        TransferMessage: str = ...
    ) -> Dict[str, Any]:
        """
        Start an input device transfer to another AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.transfer_input_device)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#transfer_input_device)
        """

    async def update_channel(
        self,
        *,
        ChannelId: str,
        CdiInputSpecification: "CdiInputSpecificationTypeDef" = ...,
        Destinations: Sequence["OutputDestinationTypeDef"] = ...,
        EncoderSettings: "EncoderSettingsTypeDef" = ...,
        InputAttachments: Sequence["InputAttachmentTypeDef"] = ...,
        InputSpecification: "InputSpecificationTypeDef" = ...,
        LogLevel: LogLevelType = ...,
        Name: str = ...,
        RoleArn: str = ...
    ) -> UpdateChannelResponseTypeDef:
        """
        Updates a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_channel)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#update_channel)
        """

    async def update_channel_class(
        self,
        *,
        ChannelClass: ChannelClassType,
        ChannelId: str,
        Destinations: Sequence["OutputDestinationTypeDef"] = ...
    ) -> UpdateChannelClassResponseTypeDef:
        """
        Changes the class of the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_channel_class)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#update_channel_class)
        """

    async def update_input(
        self,
        *,
        InputId: str,
        Destinations: Sequence["InputDestinationRequestTypeDef"] = ...,
        InputDevices: Sequence["InputDeviceRequestTypeDef"] = ...,
        InputSecurityGroups: Sequence[str] = ...,
        MediaConnectFlows: Sequence["MediaConnectFlowRequestTypeDef"] = ...,
        Name: str = ...,
        RoleArn: str = ...,
        Sources: Sequence["InputSourceRequestTypeDef"] = ...
    ) -> UpdateInputResponseTypeDef:
        """
        Updates an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_input)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#update_input)
        """

    async def update_input_device(
        self,
        *,
        InputDeviceId: str,
        HdDeviceSettings: "InputDeviceConfigurableSettingsTypeDef" = ...,
        Name: str = ...,
        UhdDeviceSettings: "InputDeviceConfigurableSettingsTypeDef" = ...
    ) -> UpdateInputDeviceResponseTypeDef:
        """
        Updates the parameters for the input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_input_device)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#update_input_device)
        """

    async def update_input_security_group(
        self,
        *,
        InputSecurityGroupId: str,
        Tags: Mapping[str, str] = ...,
        WhitelistRules: Sequence["InputWhitelistRuleCidrTypeDef"] = ...
    ) -> UpdateInputSecurityGroupResponseTypeDef:
        """
        Update an Input Security Group's Whilelists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_input_security_group)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#update_input_security_group)
        """

    async def update_multiplex(
        self,
        *,
        MultiplexId: str,
        MultiplexSettings: "MultiplexSettingsTypeDef" = ...,
        Name: str = ...
    ) -> UpdateMultiplexResponseTypeDef:
        """
        Updates a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_multiplex)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#update_multiplex)
        """

    async def update_multiplex_program(
        self,
        *,
        MultiplexId: str,
        ProgramName: str,
        MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef" = ...
    ) -> UpdateMultiplexProgramResponseTypeDef:
        """
        Update a program in a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_multiplex_program)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#update_multiplex_program)
        """

    async def update_reservation(
        self, *, ReservationId: str, Name: str = ...
    ) -> UpdateReservationResponseTypeDef:
        """
        Update reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_reservation)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#update_reservation)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_schedule"]
    ) -> DescribeSchedulePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_device_transfers"]
    ) -> ListInputDeviceTransfersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_devices"]
    ) -> ListInputDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_security_groups"]
    ) -> ListInputSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_inputs"]) -> ListInputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multiplex_programs"]
    ) -> ListMultiplexProgramsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multiplexes"]
    ) -> ListMultiplexesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_paginator)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["channel_created"]) -> ChannelCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["channel_deleted"]) -> ChannelDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["channel_running"]) -> ChannelRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["channel_stopped"]) -> ChannelStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["input_attached"]) -> InputAttachedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["input_deleted"]) -> InputDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["input_detached"]) -> InputDetachedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_created"]) -> MultiplexCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_deleted"]) -> MultiplexDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_running"]) -> MultiplexRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_stopped"]) -> MultiplexStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.get_waiter)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html#get_waiter)
        """

    async def __aenter__(self) -> "MediaLiveClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_medialive/client.html)
        """
