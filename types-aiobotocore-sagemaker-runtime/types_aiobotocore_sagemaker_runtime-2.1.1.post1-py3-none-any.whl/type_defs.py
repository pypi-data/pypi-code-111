"""
Type annotations for sagemaker-runtime service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_runtime/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sagemaker_runtime.type_defs import InvokeEndpointAsyncInputRequestTypeDef

    data: InvokeEndpointAsyncInputRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "InvokeEndpointAsyncInputRequestTypeDef",
    "InvokeEndpointAsyncOutputTypeDef",
    "InvokeEndpointInputRequestTypeDef",
    "InvokeEndpointOutputTypeDef",
    "ResponseMetadataTypeDef",
)

_RequiredInvokeEndpointAsyncInputRequestTypeDef = TypedDict(
    "_RequiredInvokeEndpointAsyncInputRequestTypeDef",
    {
        "EndpointName": str,
        "InputLocation": str,
    },
)
_OptionalInvokeEndpointAsyncInputRequestTypeDef = TypedDict(
    "_OptionalInvokeEndpointAsyncInputRequestTypeDef",
    {
        "ContentType": str,
        "Accept": str,
        "CustomAttributes": str,
        "InferenceId": str,
        "RequestTTLSeconds": int,
    },
    total=False,
)


class InvokeEndpointAsyncInputRequestTypeDef(
    _RequiredInvokeEndpointAsyncInputRequestTypeDef, _OptionalInvokeEndpointAsyncInputRequestTypeDef
):
    pass


InvokeEndpointAsyncOutputTypeDef = TypedDict(
    "InvokeEndpointAsyncOutputTypeDef",
    {
        "InferenceId": str,
        "OutputLocation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInvokeEndpointInputRequestTypeDef = TypedDict(
    "_RequiredInvokeEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "Body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalInvokeEndpointInputRequestTypeDef = TypedDict(
    "_OptionalInvokeEndpointInputRequestTypeDef",
    {
        "ContentType": str,
        "Accept": str,
        "CustomAttributes": str,
        "TargetModel": str,
        "TargetVariant": str,
        "TargetContainerHostname": str,
        "InferenceId": str,
    },
    total=False,
)


class InvokeEndpointInputRequestTypeDef(
    _RequiredInvokeEndpointInputRequestTypeDef, _OptionalInvokeEndpointInputRequestTypeDef
):
    pass


InvokeEndpointOutputTypeDef = TypedDict(
    "InvokeEndpointOutputTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
