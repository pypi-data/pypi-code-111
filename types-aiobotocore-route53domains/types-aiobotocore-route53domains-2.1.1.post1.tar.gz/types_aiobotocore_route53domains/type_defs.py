"""
Type annotations for route53domains service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_route53domains/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_route53domains.type_defs import AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef

    data: AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ContactTypeType,
    CountryCodeType,
    DomainAvailabilityType,
    ExtraParamNameType,
    ListDomainsAttributeNameType,
    OperationStatusType,
    OperationTypeType,
    OperatorType,
    ReachabilityStatusType,
    SortOrderType,
    TransferableType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef",
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "BillingRecordTypeDef",
    "CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef",
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    "CheckDomainAvailabilityRequestRequestTypeDef",
    "CheckDomainAvailabilityResponseTypeDef",
    "CheckDomainTransferabilityRequestRequestTypeDef",
    "CheckDomainTransferabilityResponseTypeDef",
    "ContactDetailTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteTagsForDomainRequestRequestTypeDef",
    "DisableDomainAutoRenewRequestRequestTypeDef",
    "DisableDomainTransferLockRequestRequestTypeDef",
    "DisableDomainTransferLockResponseTypeDef",
    "DomainPriceTypeDef",
    "DomainSuggestionTypeDef",
    "DomainSummaryTypeDef",
    "DomainTransferabilityTypeDef",
    "EnableDomainAutoRenewRequestRequestTypeDef",
    "EnableDomainTransferLockRequestRequestTypeDef",
    "EnableDomainTransferLockResponseTypeDef",
    "ExtraParamTypeDef",
    "FilterConditionTypeDef",
    "GetContactReachabilityStatusRequestRequestTypeDef",
    "GetContactReachabilityStatusResponseTypeDef",
    "GetDomainDetailRequestRequestTypeDef",
    "GetDomainDetailResponseTypeDef",
    "GetDomainSuggestionsRequestRequestTypeDef",
    "GetDomainSuggestionsResponseTypeDef",
    "GetOperationDetailRequestRequestTypeDef",
    "GetOperationDetailResponseTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "ListOperationsResponseTypeDef",
    "ListPricesRequestRequestTypeDef",
    "ListPricesResponseTypeDef",
    "ListTagsForDomainRequestRequestTypeDef",
    "ListTagsForDomainResponseTypeDef",
    "NameserverTypeDef",
    "OperationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PriceWithCurrencyTypeDef",
    "RegisterDomainRequestRequestTypeDef",
    "RegisterDomainResponseTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "RenewDomainRequestRequestTypeDef",
    "RenewDomainResponseTypeDef",
    "ResendContactReachabilityEmailRequestRequestTypeDef",
    "ResendContactReachabilityEmailResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveDomainAuthCodeRequestRequestTypeDef",
    "RetrieveDomainAuthCodeResponseTypeDef",
    "SortConditionTypeDef",
    "TagTypeDef",
    "TransferDomainRequestRequestTypeDef",
    "TransferDomainResponseTypeDef",
    "TransferDomainToAnotherAwsAccountRequestRequestTypeDef",
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    "UpdateDomainContactPrivacyRequestRequestTypeDef",
    "UpdateDomainContactPrivacyResponseTypeDef",
    "UpdateDomainContactRequestRequestTypeDef",
    "UpdateDomainContactResponseTypeDef",
    "UpdateDomainNameserversRequestRequestTypeDef",
    "UpdateDomainNameserversResponseTypeDef",
    "UpdateTagsForDomainRequestRequestTypeDef",
    "ViewBillingRequestRequestTypeDef",
    "ViewBillingResponseTypeDef",
)

AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef = TypedDict(
    "AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef",
    {
        "DomainName": str,
        "Password": str,
    },
)

AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef = TypedDict(
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BillingRecordTypeDef = TypedDict(
    "BillingRecordTypeDef",
    {
        "DomainName": str,
        "Operation": OperationTypeType,
        "InvoiceId": str,
        "BillDate": datetime,
        "Price": float,
    },
    total=False,
)

CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef = TypedDict(
    "CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

CancelDomainTransferToAnotherAwsAccountResponseTypeDef = TypedDict(
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCheckDomainAvailabilityRequestRequestTypeDef = TypedDict(
    "_RequiredCheckDomainAvailabilityRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCheckDomainAvailabilityRequestRequestTypeDef = TypedDict(
    "_OptionalCheckDomainAvailabilityRequestRequestTypeDef",
    {
        "IdnLangCode": str,
    },
    total=False,
)


class CheckDomainAvailabilityRequestRequestTypeDef(
    _RequiredCheckDomainAvailabilityRequestRequestTypeDef,
    _OptionalCheckDomainAvailabilityRequestRequestTypeDef,
):
    pass


CheckDomainAvailabilityResponseTypeDef = TypedDict(
    "CheckDomainAvailabilityResponseTypeDef",
    {
        "Availability": DomainAvailabilityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCheckDomainTransferabilityRequestRequestTypeDef = TypedDict(
    "_RequiredCheckDomainTransferabilityRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCheckDomainTransferabilityRequestRequestTypeDef = TypedDict(
    "_OptionalCheckDomainTransferabilityRequestRequestTypeDef",
    {
        "AuthCode": str,
    },
    total=False,
)


class CheckDomainTransferabilityRequestRequestTypeDef(
    _RequiredCheckDomainTransferabilityRequestRequestTypeDef,
    _OptionalCheckDomainTransferabilityRequestRequestTypeDef,
):
    pass


CheckDomainTransferabilityResponseTypeDef = TypedDict(
    "CheckDomainTransferabilityResponseTypeDef",
    {
        "Transferability": "DomainTransferabilityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContactDetailTypeDef = TypedDict(
    "ContactDetailTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": ContactTypeType,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": CountryCodeType,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List["ExtraParamTypeDef"],
    },
    total=False,
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsForDomainRequestRequestTypeDef = TypedDict(
    "DeleteTagsForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "TagsToDelete": Sequence[str],
    },
)

DisableDomainAutoRenewRequestRequestTypeDef = TypedDict(
    "DisableDomainAutoRenewRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DisableDomainTransferLockRequestRequestTypeDef = TypedDict(
    "DisableDomainTransferLockRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DisableDomainTransferLockResponseTypeDef = TypedDict(
    "DisableDomainTransferLockResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainPriceTypeDef = TypedDict(
    "DomainPriceTypeDef",
    {
        "Name": str,
        "RegistrationPrice": "PriceWithCurrencyTypeDef",
        "TransferPrice": "PriceWithCurrencyTypeDef",
        "RenewalPrice": "PriceWithCurrencyTypeDef",
        "ChangeOwnershipPrice": "PriceWithCurrencyTypeDef",
        "RestorationPrice": "PriceWithCurrencyTypeDef",
    },
    total=False,
)

DomainSuggestionTypeDef = TypedDict(
    "DomainSuggestionTypeDef",
    {
        "DomainName": str,
        "Availability": str,
    },
    total=False,
)

_RequiredDomainSummaryTypeDef = TypedDict(
    "_RequiredDomainSummaryTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDomainSummaryTypeDef = TypedDict(
    "_OptionalDomainSummaryTypeDef",
    {
        "AutoRenew": bool,
        "TransferLock": bool,
        "Expiry": datetime,
    },
    total=False,
)


class DomainSummaryTypeDef(_RequiredDomainSummaryTypeDef, _OptionalDomainSummaryTypeDef):
    pass


DomainTransferabilityTypeDef = TypedDict(
    "DomainTransferabilityTypeDef",
    {
        "Transferable": TransferableType,
    },
    total=False,
)

EnableDomainAutoRenewRequestRequestTypeDef = TypedDict(
    "EnableDomainAutoRenewRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

EnableDomainTransferLockRequestRequestTypeDef = TypedDict(
    "EnableDomainTransferLockRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

EnableDomainTransferLockResponseTypeDef = TypedDict(
    "EnableDomainTransferLockResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExtraParamTypeDef = TypedDict(
    "ExtraParamTypeDef",
    {
        "Name": ExtraParamNameType,
        "Value": str,
    },
)

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Name": ListDomainsAttributeNameType,
        "Operator": OperatorType,
        "Values": Sequence[str],
    },
)

GetContactReachabilityStatusRequestRequestTypeDef = TypedDict(
    "GetContactReachabilityStatusRequestRequestTypeDef",
    {
        "domainName": str,
    },
    total=False,
)

GetContactReachabilityStatusResponseTypeDef = TypedDict(
    "GetContactReachabilityStatusResponseTypeDef",
    {
        "domainName": str,
        "status": ReachabilityStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainDetailRequestRequestTypeDef = TypedDict(
    "GetDomainDetailRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetDomainDetailResponseTypeDef = TypedDict(
    "GetDomainDetailResponseTypeDef",
    {
        "DomainName": str,
        "Nameservers": List["NameserverTypeDef"],
        "AutoRenew": bool,
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
        "AdminPrivacy": bool,
        "RegistrantPrivacy": bool,
        "TechPrivacy": bool,
        "RegistrarName": str,
        "WhoIsServer": str,
        "RegistrarUrl": str,
        "AbuseContactEmail": str,
        "AbuseContactPhone": str,
        "RegistryDomainId": str,
        "CreationDate": datetime,
        "UpdatedDate": datetime,
        "ExpirationDate": datetime,
        "Reseller": str,
        "DnsSec": str,
        "StatusList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainSuggestionsRequestRequestTypeDef = TypedDict(
    "GetDomainSuggestionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "SuggestionCount": int,
        "OnlyAvailable": bool,
    },
)

GetDomainSuggestionsResponseTypeDef = TypedDict(
    "GetDomainSuggestionsResponseTypeDef",
    {
        "SuggestionsList": List["DomainSuggestionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationDetailRequestRequestTypeDef = TypedDict(
    "GetOperationDetailRequestRequestTypeDef",
    {
        "OperationId": str,
    },
)

GetOperationDetailResponseTypeDef = TypedDict(
    "GetOperationDetailResponseTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatusType,
        "Message": str,
        "DomainName": str,
        "Type": OperationTypeType,
        "SubmittedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "FilterConditions": Sequence["FilterConditionTypeDef"],
        "SortCondition": "SortConditionTypeDef",
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List["DomainSummaryTypeDef"],
        "NextPageMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOperationsRequestRequestTypeDef = TypedDict(
    "ListOperationsRequestRequestTypeDef",
    {
        "SubmittedSince": Union[datetime, str],
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "Operations": List["OperationSummaryTypeDef"],
        "NextPageMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPricesRequestRequestTypeDef = TypedDict(
    "ListPricesRequestRequestTypeDef",
    {
        "Tld": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListPricesResponseTypeDef = TypedDict(
    "ListPricesResponseTypeDef",
    {
        "Prices": List["DomainPriceTypeDef"],
        "NextPageMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForDomainRequestRequestTypeDef = TypedDict(
    "ListTagsForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

ListTagsForDomainResponseTypeDef = TypedDict(
    "ListTagsForDomainResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNameserverTypeDef = TypedDict(
    "_RequiredNameserverTypeDef",
    {
        "Name": str,
    },
)
_OptionalNameserverTypeDef = TypedDict(
    "_OptionalNameserverTypeDef",
    {
        "GlueIps": List[str],
    },
    total=False,
)


class NameserverTypeDef(_RequiredNameserverTypeDef, _OptionalNameserverTypeDef):
    pass


OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatusType,
        "Type": OperationTypeType,
        "SubmittedDate": datetime,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PriceWithCurrencyTypeDef = TypedDict(
    "PriceWithCurrencyTypeDef",
    {
        "Price": float,
        "Currency": str,
    },
)

_RequiredRegisterDomainRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DurationInYears": int,
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
    },
)
_OptionalRegisterDomainRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterDomainRequestRequestTypeDef",
    {
        "IdnLangCode": str,
        "AutoRenew": bool,
        "PrivacyProtectAdminContact": bool,
        "PrivacyProtectRegistrantContact": bool,
        "PrivacyProtectTechContact": bool,
    },
    total=False,
)


class RegisterDomainRequestRequestTypeDef(
    _RequiredRegisterDomainRequestRequestTypeDef, _OptionalRegisterDomainRequestRequestTypeDef
):
    pass


RegisterDomainResponseTypeDef = TypedDict(
    "RegisterDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef = TypedDict(
    "RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

RejectDomainTransferFromAnotherAwsAccountResponseTypeDef = TypedDict(
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRenewDomainRequestRequestTypeDef = TypedDict(
    "_RequiredRenewDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "CurrentExpiryYear": int,
    },
)
_OptionalRenewDomainRequestRequestTypeDef = TypedDict(
    "_OptionalRenewDomainRequestRequestTypeDef",
    {
        "DurationInYears": int,
    },
    total=False,
)


class RenewDomainRequestRequestTypeDef(
    _RequiredRenewDomainRequestRequestTypeDef, _OptionalRenewDomainRequestRequestTypeDef
):
    pass


RenewDomainResponseTypeDef = TypedDict(
    "RenewDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResendContactReachabilityEmailRequestRequestTypeDef = TypedDict(
    "ResendContactReachabilityEmailRequestRequestTypeDef",
    {
        "domainName": str,
    },
    total=False,
)

ResendContactReachabilityEmailResponseTypeDef = TypedDict(
    "ResendContactReachabilityEmailResponseTypeDef",
    {
        "domainName": str,
        "emailAddress": str,
        "isAlreadyVerified": bool,
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

RetrieveDomainAuthCodeRequestRequestTypeDef = TypedDict(
    "RetrieveDomainAuthCodeRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

RetrieveDomainAuthCodeResponseTypeDef = TypedDict(
    "RetrieveDomainAuthCodeResponseTypeDef",
    {
        "AuthCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SortConditionTypeDef = TypedDict(
    "SortConditionTypeDef",
    {
        "Name": ListDomainsAttributeNameType,
        "SortOrder": SortOrderType,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredTransferDomainRequestRequestTypeDef = TypedDict(
    "_RequiredTransferDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DurationInYears": int,
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
    },
)
_OptionalTransferDomainRequestRequestTypeDef = TypedDict(
    "_OptionalTransferDomainRequestRequestTypeDef",
    {
        "IdnLangCode": str,
        "Nameservers": Sequence["NameserverTypeDef"],
        "AuthCode": str,
        "AutoRenew": bool,
        "PrivacyProtectAdminContact": bool,
        "PrivacyProtectRegistrantContact": bool,
        "PrivacyProtectTechContact": bool,
    },
    total=False,
)


class TransferDomainRequestRequestTypeDef(
    _RequiredTransferDomainRequestRequestTypeDef, _OptionalTransferDomainRequestRequestTypeDef
):
    pass


TransferDomainResponseTypeDef = TypedDict(
    "TransferDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransferDomainToAnotherAwsAccountRequestRequestTypeDef = TypedDict(
    "TransferDomainToAnotherAwsAccountRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccountId": str,
    },
)

TransferDomainToAnotherAwsAccountResponseTypeDef = TypedDict(
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "Password": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainContactPrivacyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainContactPrivacyRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainContactPrivacyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainContactPrivacyRequestRequestTypeDef",
    {
        "AdminPrivacy": bool,
        "RegistrantPrivacy": bool,
        "TechPrivacy": bool,
    },
    total=False,
)


class UpdateDomainContactPrivacyRequestRequestTypeDef(
    _RequiredUpdateDomainContactPrivacyRequestRequestTypeDef,
    _OptionalUpdateDomainContactPrivacyRequestRequestTypeDef,
):
    pass


UpdateDomainContactPrivacyResponseTypeDef = TypedDict(
    "UpdateDomainContactPrivacyResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainContactRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainContactRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainContactRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainContactRequestRequestTypeDef",
    {
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
    },
    total=False,
)


class UpdateDomainContactRequestRequestTypeDef(
    _RequiredUpdateDomainContactRequestRequestTypeDef,
    _OptionalUpdateDomainContactRequestRequestTypeDef,
):
    pass


UpdateDomainContactResponseTypeDef = TypedDict(
    "UpdateDomainContactResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainNameserversRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainNameserversRequestRequestTypeDef",
    {
        "DomainName": str,
        "Nameservers": Sequence["NameserverTypeDef"],
    },
)
_OptionalUpdateDomainNameserversRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainNameserversRequestRequestTypeDef",
    {
        "FIAuthKey": str,
    },
    total=False,
)


class UpdateDomainNameserversRequestRequestTypeDef(
    _RequiredUpdateDomainNameserversRequestRequestTypeDef,
    _OptionalUpdateDomainNameserversRequestRequestTypeDef,
):
    pass


UpdateDomainNameserversResponseTypeDef = TypedDict(
    "UpdateDomainNameserversResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTagsForDomainRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTagsForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateTagsForDomainRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTagsForDomainRequestRequestTypeDef",
    {
        "TagsToUpdate": Sequence["TagTypeDef"],
    },
    total=False,
)


class UpdateTagsForDomainRequestRequestTypeDef(
    _RequiredUpdateTagsForDomainRequestRequestTypeDef,
    _OptionalUpdateTagsForDomainRequestRequestTypeDef,
):
    pass


ViewBillingRequestRequestTypeDef = TypedDict(
    "ViewBillingRequestRequestTypeDef",
    {
        "Start": Union[datetime, str],
        "End": Union[datetime, str],
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ViewBillingResponseTypeDef = TypedDict(
    "ViewBillingResponseTypeDef",
    {
        "NextPageMarker": str,
        "BillingRecords": List["BillingRecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
