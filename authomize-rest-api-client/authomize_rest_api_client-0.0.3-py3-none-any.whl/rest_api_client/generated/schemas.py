# generated by datamodel-codegen:
#   filename:  openapi.json
#   timestamp: 2022-02-17T11:08:03+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AccessTypes(Enum):
    Unknown = 'Unknown'
    All = 'All'
    Owner = 'Owner'
    Read = 'Read'
    ReadMetadata = 'ReadMetadata'
    Write = 'Write'
    Create = 'Create'
    Delete = 'Delete'
    Execute = 'Execute'
    Enable = 'Enable'
    Assign = 'Assign'
    Restore = 'Restore'
    Import = 'Import'
    Export = 'Export'
    Get = 'Get'
    Set = 'Set'
    Update = 'Update'
    Cancel = 'Cancel'
    Use = 'Use'
    AllowUse = 'AllowUse'
    List = 'List'
    Administrative = 'Administrative'
    Delegate = 'Delegate'
    Join = 'Join'
    Invite = 'Invite'
    Leave = 'Leave'
    Share = 'Share'


class AssetTypes(Enum):
    Resource = 'Resource'
    File = 'File'
    Folder = 'Folder'
    Drive = 'Drive'
    Site = 'Site'
    Application = 'Application'
    Package = 'Package'
    Project = 'Project'
    Cluster = 'Cluster'
    Dataset = 'Dataset'
    Subscription = 'Subscription'
    Table = 'Table'
    TableRecord = 'TableRecord'
    Disk = 'Disk'
    Image = 'Image'
    Instance = 'Instance'
    Snapshot = 'Snapshot'
    Service = 'Service'
    Topic = 'Topic'
    Bucket = 'Bucket'
    BillingAccount = 'BillingAccount'
    Device = 'Device'
    Calendar = 'Calendar'
    Policy = 'Policy'
    GitRepository = 'GitRepository'
    Network = 'Network'
    Vpc = 'Vpc'
    NetworkInterface = 'NetworkInterface'
    VirtualMachine = 'VirtualMachine'
    NetworkSecurityGroup = 'NetworkSecurityGroup'
    Ticket = 'Ticket'
    NetworkSubnet = 'NetworkSubnet'
    NetworkAcl = 'NetworkAcl'
    RouteTable = 'RouteTable'
    NetworkAddress = 'NetworkAddress'
    Secret = 'Secret'
    Storage = 'Storage'
    Workspace = 'Workspace'
    SharedLink = 'SharedLink'
    Collection = 'Collection'
    Database = 'Database'


class AssetsInheritance(BaseModel):
    fromId: str = Field(..., title='Fromid')
    toId: str = Field(..., title='Toid')


class AvailableConnectorId(Enum):
    restApiImport = 'restApiImport'


class ConnectorStatus(Enum):
    initializing = 'initializing'
    archived = 'archived'
    enabled = 'enabled'
    disabled = 'disabled'
    installable = 'installable'
    validating = 'validating'
    failure = 'failure'


class ExportResponse(BaseModel):
    exportId: str = Field(..., title='Exportid')
    exportUrl: str = Field(..., title='Exporturl')


class IdentitiesInheritance(BaseModel):
    fromId: str = Field(..., title='Fromid')
    toId: str = Field(..., title='Toid')


class IdentityTypes(Enum):
    Identity = 'Identity'
    User = 'User'
    Group = 'Group'
    EntitlementProxy = 'EntitlementProxy'
    AccessKey = 'AccessKey'
    ServiceAccount = 'ServiceAccount'
    Alias = 'Alias'
    Domain = 'Domain'
    Organization = 'Organization'
    TaskPerformer = 'TaskPerformer'


class IsAliveResponse(BaseModel):
    isAlive: bool = Field(..., title='Isalive')


class MeResponse(BaseModel):
    version: str = Field(..., title='Version')
    id: str = Field(..., title='Id')
    tenant: str = Field(..., title='Tenant')


class NewRestApiConnectorSchema(BaseModel):
    config: Optional[Dict[str, Any]] = Field(None, title='Config')
    serviceId: Optional[str] = Field(None, title='Serviceid')


class RestApiConnectorSchema(BaseModel):
    config: Optional[Dict[str, Any]] = Field(None, title='Config')
    serviceId: Optional[str] = Field(None, title='Serviceid')
    id: str = Field(..., title='Id')
    createdAt: Optional[str] = Field(None, title='Createdat')
    lastSyncedAt: Optional[str] = Field(None, title='Lastsyncedat')
    lastError: Optional[str] = Field(None, title='Lasterror')
    modifiedAt: Optional[str] = Field(None, title='Modifiedat')
    status: Optional[ConnectorStatus] = 'disabled'
    serviceType: str = Field(..., title='Servicetype')
    availableConnectorId: Optional[AvailableConnectorId] = 'restApiImport'
    actorType: Optional[str] = Field(None, title='Actortype')
    actorId: Optional[str] = Field(None, title='Actorid')


class ServiceDescription(BaseModel):
    name: str = Field(..., title='Name')
    icon: Optional[str] = Field(None, title='Icon')


class SubmitResponse(BaseModel):
    acceptedTimestamp: datetime = Field(..., title='Acceptedtimestamp')


class TransactionStateType(Enum):
    Applying = 'Applying'
    Complete = 'Complete'
    Failed = 'Failed'
    Ingest = 'Ingest'
    IngestChunk = 'IngestChunk'
    PostProcess = 'PostProcess'
    Queue = 'Queue'


class UserStatus(Enum):
    Staged = 'Staged'
    Enabled = 'Enabled'
    Disabled = 'Disabled'
    Suspended = 'Suspended'
    Deleted = 'Deleted'


class ValidationError(BaseModel):
    loc: List[str] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class AuthomizeArangoStoresModelsPagination(BaseModel):
    total: int = Field(..., title='Total')
    limit: int = Field(..., title='Limit')
    skip: int = Field(..., title='Skip')


class AuthomizeClientsSchemasPluginsServicePluginsServicePagination(BaseModel):
    limit: Optional[int] = Field(-1, title='Limit')
    skip: Optional[int] = Field(0, title='Skip')
    total: Optional[int] = Field(-1, title='Total')


class AccessDescription(BaseModel):
    fromIdentityId: str = Field(..., title='Fromidentityid')
    toAssetId: str = Field(..., title='Toassetid')
    accessType: AccessTypes
    accessName: Optional[str] = Field(None, title='Accessname')


class AssetDescription(BaseModel):
    id: str = Field(..., title='Id')
    name: str = Field(..., title='Name')
    type: AssetTypes
    description: Optional[str] = Field(None, title='Description')
    href: Optional[str] = Field(None, title='Href')
    createdAt: Optional[datetime] = Field(None, title='Createdat')
    service: Optional[str] = Field(None, title='Service')


class BundleTransactionSchema(BaseModel):
    connectorId: str = Field(..., title='Connectorid')
    transactionCreatedAt: Optional[datetime] = Field(None, title='Transactioncreatedat')
    warnings: Optional[List[str]] = Field(None, title='Warnings')
    validations: Optional[Dict[str, Any]] = Field(None, title='Validations')
    id: str = Field(..., title='Id')
    state: TransactionStateType


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class IdentityDescription(BaseModel):
    id: str = Field(..., title='Id')
    name: str = Field(..., title='Name')
    type: IdentityTypes
    userType: Optional[str] = Field(None, title='Usertype')
    email: Optional[str] = Field(None, title='Email')
    manager: Optional[str] = Field(None, title='Manager')
    title: Optional[str] = Field(None, title='Title')
    description: Optional[str] = Field(None, title='Description')
    href: Optional[str] = Field(None, title='Href')
    createdAt: Optional[datetime] = Field(None, title='Createdat')
    terminationDate: Optional[datetime] = Field(None, title='Terminationdate')
    isExternal: Optional[bool] = Field(None, title='Isexternal')
    hasTwoFactorAuthenticationEnabled: Optional[bool] = Field(
        None, title='Hastwofactorauthenticationenabled'
    )
    firstName: Optional[str] = Field(None, title='Firstname')
    lastName: Optional[str] = Field(None, title='Lastname')
    userName: Optional[str] = Field(None, title='Username')
    status: Optional[UserStatus] = None
    service: Optional[str] = Field(None, title='Service')


class ItemsBundleSchema(BaseModel):
    services: Optional[List[ServiceDescription]] = Field(None, title='Services')
    identities: List[IdentityDescription] = Field(..., title='Identities')
    assets: List[AssetDescription] = Field(..., title='Assets')
    inheritanceIdentities: List[IdentitiesInheritance] = Field(..., title='Inheritanceidentities')
    inheritanceAssets: List[AssetsInheritance] = Field(..., title='Inheritanceassets')
    access: List[AccessDescription] = Field(..., title='Access')


class RestApiConnectorListSchema(BaseModel):
    pagination: AuthomizeClientsSchemasPluginsServicePluginsServicePagination
    data: List[RestApiConnectorSchema] = Field(..., title='Data')


class TransactionPaginatedSearchSchema(BaseModel):
    data: List[BundleTransactionSchema] = Field(..., title='Data')
    pagination: AuthomizeArangoStoresModelsPagination
