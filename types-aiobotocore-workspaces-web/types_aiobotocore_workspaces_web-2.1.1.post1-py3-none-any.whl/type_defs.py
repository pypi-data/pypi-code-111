"""
Type annotations for workspaces-web service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_workspaces_web.type_defs import AssociateBrowserSettingsRequestRequestTypeDef

    data: AssociateBrowserSettingsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import EnabledTypeType, IdentityProviderTypeType, PortalStatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateBrowserSettingsRequestRequestTypeDef",
    "AssociateBrowserSettingsResponseTypeDef",
    "AssociateNetworkSettingsRequestRequestTypeDef",
    "AssociateNetworkSettingsResponseTypeDef",
    "AssociateTrustStoreRequestRequestTypeDef",
    "AssociateTrustStoreResponseTypeDef",
    "AssociateUserSettingsRequestRequestTypeDef",
    "AssociateUserSettingsResponseTypeDef",
    "BrowserSettingsSummaryTypeDef",
    "BrowserSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CreateBrowserSettingsRequestRequestTypeDef",
    "CreateBrowserSettingsResponseTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateNetworkSettingsRequestRequestTypeDef",
    "CreateNetworkSettingsResponseTypeDef",
    "CreatePortalRequestRequestTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateTrustStoreRequestRequestTypeDef",
    "CreateTrustStoreResponseTypeDef",
    "CreateUserSettingsRequestRequestTypeDef",
    "CreateUserSettingsResponseTypeDef",
    "DeleteBrowserSettingsRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteNetworkSettingsRequestRequestTypeDef",
    "DeletePortalRequestRequestTypeDef",
    "DeleteTrustStoreRequestRequestTypeDef",
    "DeleteUserSettingsRequestRequestTypeDef",
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    "DisassociateTrustStoreRequestRequestTypeDef",
    "DisassociateUserSettingsRequestRequestTypeDef",
    "GetBrowserSettingsRequestRequestTypeDef",
    "GetBrowserSettingsResponseTypeDef",
    "GetIdentityProviderRequestRequestTypeDef",
    "GetIdentityProviderResponseTypeDef",
    "GetNetworkSettingsRequestRequestTypeDef",
    "GetNetworkSettingsResponseTypeDef",
    "GetPortalRequestRequestTypeDef",
    "GetPortalResponseTypeDef",
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    "GetPortalServiceProviderMetadataResponseTypeDef",
    "GetTrustStoreCertificateRequestRequestTypeDef",
    "GetTrustStoreCertificateResponseTypeDef",
    "GetTrustStoreRequestRequestTypeDef",
    "GetTrustStoreResponseTypeDef",
    "GetUserSettingsRequestRequestTypeDef",
    "GetUserSettingsResponseTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IdentityProviderTypeDef",
    "ListBrowserSettingsRequestRequestTypeDef",
    "ListBrowserSettingsResponseTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListNetworkSettingsRequestRequestTypeDef",
    "ListNetworkSettingsResponseTypeDef",
    "ListPortalsRequestRequestTypeDef",
    "ListPortalsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrustStoreCertificatesRequestRequestTypeDef",
    "ListTrustStoreCertificatesResponseTypeDef",
    "ListTrustStoresRequestRequestTypeDef",
    "ListTrustStoresResponseTypeDef",
    "ListUserSettingsRequestRequestTypeDef",
    "ListUserSettingsResponseTypeDef",
    "NetworkSettingsSummaryTypeDef",
    "NetworkSettingsTypeDef",
    "PortalSummaryTypeDef",
    "PortalTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrustStoreSummaryTypeDef",
    "TrustStoreTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBrowserSettingsRequestRequestTypeDef",
    "UpdateBrowserSettingsResponseTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateNetworkSettingsRequestRequestTypeDef",
    "UpdateNetworkSettingsResponseTypeDef",
    "UpdatePortalRequestRequestTypeDef",
    "UpdatePortalResponseTypeDef",
    "UpdateTrustStoreRequestRequestTypeDef",
    "UpdateTrustStoreResponseTypeDef",
    "UpdateUserSettingsRequestRequestTypeDef",
    "UpdateUserSettingsResponseTypeDef",
    "UserSettingsSummaryTypeDef",
    "UserSettingsTypeDef",
)

AssociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
    },
)

AssociateBrowserSettingsResponseTypeDef = TypedDict(
    "AssociateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "AssociateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
    },
)

AssociateNetworkSettingsResponseTypeDef = TypedDict(
    "AssociateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateTrustStoreRequestRequestTypeDef = TypedDict(
    "AssociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
    },
)

AssociateTrustStoreResponseTypeDef = TypedDict(
    "AssociateTrustStoreResponseTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateUserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
    },
)

AssociateUserSettingsResponseTypeDef = TypedDict(
    "AssociateUserSettingsResponseTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BrowserSettingsSummaryTypeDef = TypedDict(
    "BrowserSettingsSummaryTypeDef",
    {
        "browserSettingsArn": str,
    },
    total=False,
)

_RequiredBrowserSettingsTypeDef = TypedDict(
    "_RequiredBrowserSettingsTypeDef",
    {
        "browserSettingsArn": str,
    },
)
_OptionalBrowserSettingsTypeDef = TypedDict(
    "_OptionalBrowserSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "browserPolicy": str,
    },
    total=False,
)


class BrowserSettingsTypeDef(_RequiredBrowserSettingsTypeDef, _OptionalBrowserSettingsTypeDef):
    pass


CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "issuer": str,
        "notValidAfter": datetime,
        "notValidBefore": datetime,
        "subject": str,
        "thumbprint": str,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "body": bytes,
        "issuer": str,
        "notValidAfter": datetime,
        "notValidBefore": datetime,
        "subject": str,
        "thumbprint": str,
    },
    total=False,
)

_RequiredCreateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBrowserSettingsRequestRequestTypeDef",
    {
        "browserPolicy": str,
    },
)
_OptionalCreateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBrowserSettingsRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Mapping[str, str],
        "clientToken": str,
        "customerManagedKey": str,
        "tags": Sequence["TagTypeDef"],
    },
    total=False,
)


class CreateBrowserSettingsRequestRequestTypeDef(
    _RequiredCreateBrowserSettingsRequestRequestTypeDef,
    _OptionalCreateBrowserSettingsRequestRequestTypeDef,
):
    pass


CreateBrowserSettingsResponseTypeDef = TypedDict(
    "CreateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderDetails": Mapping[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
        "portalArn": str,
    },
)
_OptionalCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIdentityProviderRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class CreateIdentityProviderRequestRequestTypeDef(
    _RequiredCreateIdentityProviderRequestRequestTypeDef,
    _OptionalCreateIdentityProviderRequestRequestTypeDef,
):
    pass


CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "identityProviderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkSettingsRequestRequestTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
)
_OptionalCreateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Sequence["TagTypeDef"],
    },
    total=False,
)


class CreateNetworkSettingsRequestRequestTypeDef(
    _RequiredCreateNetworkSettingsRequestRequestTypeDef,
    _OptionalCreateNetworkSettingsRequestRequestTypeDef,
):
    pass


CreateNetworkSettingsResponseTypeDef = TypedDict(
    "CreateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePortalRequestRequestTypeDef = TypedDict(
    "CreatePortalRequestRequestTypeDef",
    {
        "additionalEncryptionContext": Mapping[str, str],
        "clientToken": str,
        "customerManagedKey": str,
        "displayName": str,
        "tags": Sequence["TagTypeDef"],
    },
    total=False,
)

CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalArn": str,
        "portalEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrustStoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrustStoreRequestRequestTypeDef",
    {
        "certificateList": Sequence[Union[bytes, IO[bytes], StreamingBody]],
    },
)
_OptionalCreateTrustStoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrustStoreRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Sequence["TagTypeDef"],
    },
    total=False,
)


class CreateTrustStoreRequestRequestTypeDef(
    _RequiredCreateTrustStoreRequestRequestTypeDef, _OptionalCreateTrustStoreRequestRequestTypeDef
):
    pass


CreateTrustStoreResponseTypeDef = TypedDict(
    "CreateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserSettingsRequestRequestTypeDef",
    {
        "copyAllowed": EnabledTypeType,
        "downloadAllowed": EnabledTypeType,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
)
_OptionalCreateUserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Sequence["TagTypeDef"],
    },
    total=False,
)


class CreateUserSettingsRequestRequestTypeDef(
    _RequiredCreateUserSettingsRequestRequestTypeDef,
    _OptionalCreateUserSettingsRequestRequestTypeDef,
):
    pass


CreateUserSettingsResponseTypeDef = TypedDict(
    "CreateUserSettingsResponseTypeDef",
    {
        "userSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)

DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)

DeleteNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DeleteNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)

DeletePortalRequestRequestTypeDef = TypedDict(
    "DeletePortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DeleteTrustStoreRequestRequestTypeDef = TypedDict(
    "DeleteTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)

DeleteUserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)

DisassociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateTrustStoreRequestRequestTypeDef = TypedDict(
    "DisassociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateUserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetBrowserSettingsRequestRequestTypeDef = TypedDict(
    "GetBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)

GetBrowserSettingsResponseTypeDef = TypedDict(
    "GetBrowserSettingsResponseTypeDef",
    {
        "browserSettings": "BrowserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityProviderRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)

GetIdentityProviderResponseTypeDef = TypedDict(
    "GetIdentityProviderResponseTypeDef",
    {
        "identityProvider": "IdentityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkSettingsRequestRequestTypeDef = TypedDict(
    "GetNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)

GetNetworkSettingsResponseTypeDef = TypedDict(
    "GetNetworkSettingsResponseTypeDef",
    {
        "networkSettings": "NetworkSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortalRequestRequestTypeDef = TypedDict(
    "GetPortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetPortalResponseTypeDef = TypedDict(
    "GetPortalResponseTypeDef",
    {
        "portal": "PortalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortalServiceProviderMetadataRequestRequestTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetPortalServiceProviderMetadataResponseTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataResponseTypeDef",
    {
        "portalArn": str,
        "serviceProviderSamlMetadata": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrustStoreCertificateRequestRequestTypeDef = TypedDict(
    "GetTrustStoreCertificateRequestRequestTypeDef",
    {
        "thumbprint": str,
        "trustStoreArn": str,
    },
)

GetTrustStoreCertificateResponseTypeDef = TypedDict(
    "GetTrustStoreCertificateResponseTypeDef",
    {
        "certificate": "CertificateTypeDef",
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrustStoreRequestRequestTypeDef = TypedDict(
    "GetTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)

GetTrustStoreResponseTypeDef = TypedDict(
    "GetTrustStoreResponseTypeDef",
    {
        "trustStore": "TrustStoreTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserSettingsRequestRequestTypeDef = TypedDict(
    "GetUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)

GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef",
    {
        "userSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityProviderSummaryTypeDef = TypedDict(
    "IdentityProviderSummaryTypeDef",
    {
        "identityProviderArn": str,
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)

_RequiredIdentityProviderTypeDef = TypedDict(
    "_RequiredIdentityProviderTypeDef",
    {
        "identityProviderArn": str,
    },
)
_OptionalIdentityProviderTypeDef = TypedDict(
    "_OptionalIdentityProviderTypeDef",
    {
        "identityProviderDetails": Dict[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)


class IdentityProviderTypeDef(_RequiredIdentityProviderTypeDef, _OptionalIdentityProviderTypeDef):
    pass


ListBrowserSettingsRequestRequestTypeDef = TypedDict(
    "ListBrowserSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListBrowserSettingsResponseTypeDef = TypedDict(
    "ListBrowserSettingsResponseTypeDef",
    {
        "browserSettings": List["BrowserSettingsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_RequiredListIdentityProvidersRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
_OptionalListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_OptionalListIdentityProvidersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListIdentityProvidersRequestRequestTypeDef(
    _RequiredListIdentityProvidersRequestRequestTypeDef,
    _OptionalListIdentityProvidersRequestRequestTypeDef,
):
    pass


ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "identityProviders": List["IdentityProviderSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworkSettingsRequestRequestTypeDef = TypedDict(
    "ListNetworkSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListNetworkSettingsResponseTypeDef = TypedDict(
    "ListNetworkSettingsResponseTypeDef",
    {
        "networkSettings": List["NetworkSettingsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortalsRequestRequestTypeDef = TypedDict(
    "ListPortalsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {
        "nextToken": str,
        "portals": List["PortalSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrustStoreCertificatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTrustStoreCertificatesRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)
_OptionalListTrustStoreCertificatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTrustStoreCertificatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTrustStoreCertificatesRequestRequestTypeDef(
    _RequiredListTrustStoreCertificatesRequestRequestTypeDef,
    _OptionalListTrustStoreCertificatesRequestRequestTypeDef,
):
    pass


ListTrustStoreCertificatesResponseTypeDef = TypedDict(
    "ListTrustStoreCertificatesResponseTypeDef",
    {
        "certificateList": List["CertificateSummaryTypeDef"],
        "nextToken": str,
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrustStoresRequestRequestTypeDef = TypedDict(
    "ListTrustStoresRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTrustStoresResponseTypeDef = TypedDict(
    "ListTrustStoresResponseTypeDef",
    {
        "nextToken": str,
        "trustStores": List["TrustStoreSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserSettingsRequestRequestTypeDef = TypedDict(
    "ListUserSettingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListUserSettingsResponseTypeDef = TypedDict(
    "ListUserSettingsResponseTypeDef",
    {
        "nextToken": str,
        "userSettings": List["UserSettingsSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkSettingsSummaryTypeDef = TypedDict(
    "NetworkSettingsSummaryTypeDef",
    {
        "networkSettingsArn": str,
        "vpcId": str,
    },
    total=False,
)

_RequiredNetworkSettingsTypeDef = TypedDict(
    "_RequiredNetworkSettingsTypeDef",
    {
        "networkSettingsArn": str,
    },
)
_OptionalNetworkSettingsTypeDef = TypedDict(
    "_OptionalNetworkSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
    total=False,
)


class NetworkSettingsTypeDef(_RequiredNetworkSettingsTypeDef, _OptionalNetworkSettingsTypeDef):
    pass


PortalSummaryTypeDef = TypedDict(
    "PortalSummaryTypeDef",
    {
        "browserSettingsArn": str,
        "browserType": Literal["Chrome"],
        "creationDate": datetime,
        "displayName": str,
        "networkSettingsArn": str,
        "portalArn": str,
        "portalEndpoint": str,
        "portalStatus": PortalStatusType,
        "rendererType": Literal["AppStream"],
        "trustStoreArn": str,
        "userSettingsArn": str,
    },
    total=False,
)

PortalTypeDef = TypedDict(
    "PortalTypeDef",
    {
        "browserSettingsArn": str,
        "browserType": Literal["Chrome"],
        "creationDate": datetime,
        "displayName": str,
        "networkSettingsArn": str,
        "portalArn": str,
        "portalEndpoint": str,
        "portalStatus": PortalStatusType,
        "rendererType": Literal["AppStream"],
        "statusReason": str,
        "trustStoreArn": str,
        "userSettingsArn": str,
    },
    total=False,
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

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TrustStoreSummaryTypeDef = TypedDict(
    "TrustStoreSummaryTypeDef",
    {
        "trustStoreArn": str,
    },
    total=False,
)

TrustStoreTypeDef = TypedDict(
    "TrustStoreTypeDef",
    {
        "associatedPortalArns": List[str],
        "trustStoreArn": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)
_OptionalUpdateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBrowserSettingsRequestRequestTypeDef",
    {
        "browserPolicy": str,
        "clientToken": str,
    },
    total=False,
)


class UpdateBrowserSettingsRequestRequestTypeDef(
    _RequiredUpdateBrowserSettingsRequestRequestTypeDef,
    _OptionalUpdateBrowserSettingsRequestRequestTypeDef,
):
    pass


UpdateBrowserSettingsResponseTypeDef = TypedDict(
    "UpdateBrowserSettingsResponseTypeDef",
    {
        "browserSettings": "BrowserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)
_OptionalUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentityProviderRequestRequestTypeDef",
    {
        "clientToken": str,
        "identityProviderDetails": Mapping[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
    },
    total=False,
)


class UpdateIdentityProviderRequestRequestTypeDef(
    _RequiredUpdateIdentityProviderRequestRequestTypeDef,
    _OptionalUpdateIdentityProviderRequestRequestTypeDef,
):
    pass


UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "identityProvider": "IdentityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)
_OptionalUpdateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
    total=False,
)


class UpdateNetworkSettingsRequestRequestTypeDef(
    _RequiredUpdateNetworkSettingsRequestRequestTypeDef,
    _OptionalUpdateNetworkSettingsRequestRequestTypeDef,
):
    pass


UpdateNetworkSettingsResponseTypeDef = TypedDict(
    "UpdateNetworkSettingsResponseTypeDef",
    {
        "networkSettings": "NetworkSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePortalRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
_OptionalUpdatePortalRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePortalRequestRequestTypeDef",
    {
        "displayName": str,
    },
    total=False,
)


class UpdatePortalRequestRequestTypeDef(
    _RequiredUpdatePortalRequestRequestTypeDef, _OptionalUpdatePortalRequestRequestTypeDef
):
    pass


UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef",
    {
        "portal": "PortalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrustStoreRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)
_OptionalUpdateTrustStoreRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrustStoreRequestRequestTypeDef",
    {
        "certificatesToAdd": Sequence[Union[bytes, IO[bytes], StreamingBody]],
        "certificatesToDelete": Sequence[str],
        "clientToken": str,
    },
    total=False,
)


class UpdateTrustStoreRequestRequestTypeDef(
    _RequiredUpdateTrustStoreRequestRequestTypeDef, _OptionalUpdateTrustStoreRequestRequestTypeDef
):
    pass


UpdateTrustStoreResponseTypeDef = TypedDict(
    "UpdateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)
_OptionalUpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserSettingsRequestRequestTypeDef",
    {
        "clientToken": str,
        "copyAllowed": EnabledTypeType,
        "downloadAllowed": EnabledTypeType,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
    total=False,
)


class UpdateUserSettingsRequestRequestTypeDef(
    _RequiredUpdateUserSettingsRequestRequestTypeDef,
    _OptionalUpdateUserSettingsRequestRequestTypeDef,
):
    pass


UpdateUserSettingsResponseTypeDef = TypedDict(
    "UpdateUserSettingsResponseTypeDef",
    {
        "userSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserSettingsSummaryTypeDef = TypedDict(
    "UserSettingsSummaryTypeDef",
    {
        "copyAllowed": EnabledTypeType,
        "downloadAllowed": EnabledTypeType,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
        "userSettingsArn": str,
    },
    total=False,
)

_RequiredUserSettingsTypeDef = TypedDict(
    "_RequiredUserSettingsTypeDef",
    {
        "userSettingsArn": str,
    },
)
_OptionalUserSettingsTypeDef = TypedDict(
    "_OptionalUserSettingsTypeDef",
    {
        "associatedPortalArns": List[str],
        "copyAllowed": EnabledTypeType,
        "downloadAllowed": EnabledTypeType,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
    },
    total=False,
)


class UserSettingsTypeDef(_RequiredUserSettingsTypeDef, _OptionalUserSettingsTypeDef):
    pass
