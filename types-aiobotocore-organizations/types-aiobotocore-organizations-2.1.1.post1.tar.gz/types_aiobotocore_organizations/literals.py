"""
Type annotations for organizations service literal definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_organizations/literals.html)

Usage::

    ```python
    from types_aiobotocore_organizations.literals import AccountJoinedMethodType

    data: AccountJoinedMethodType = "CREATED"
    ```
"""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountJoinedMethodType",
    "AccountStatusType",
    "ActionTypeType",
    "ChildTypeType",
    "CreateAccountFailureReasonType",
    "CreateAccountStateType",
    "EffectivePolicyTypeType",
    "HandshakePartyTypeType",
    "HandshakeResourceTypeType",
    "HandshakeStateType",
    "IAMUserAccessToBillingType",
    "ListAWSServiceAccessForOrganizationPaginatorName",
    "ListAccountsForParentPaginatorName",
    "ListAccountsPaginatorName",
    "ListChildrenPaginatorName",
    "ListCreateAccountStatusPaginatorName",
    "ListDelegatedAdministratorsPaginatorName",
    "ListDelegatedServicesForAccountPaginatorName",
    "ListHandshakesForAccountPaginatorName",
    "ListHandshakesForOrganizationPaginatorName",
    "ListOrganizationalUnitsForParentPaginatorName",
    "ListParentsPaginatorName",
    "ListPoliciesForTargetPaginatorName",
    "ListPoliciesPaginatorName",
    "ListRootsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTargetsForPolicyPaginatorName",
    "OrganizationFeatureSetType",
    "ParentTypeType",
    "PolicyTypeStatusType",
    "PolicyTypeType",
    "TargetTypeType",
    "ServiceName",
    "PaginatorName",
)


AccountJoinedMethodType = Literal["CREATED", "INVITED"]
AccountStatusType = Literal["ACTIVE", "SUSPENDED"]
ActionTypeType = Literal[
    "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE", "APPROVE_ALL_FEATURES", "ENABLE_ALL_FEATURES", "INVITE"
]
ChildTypeType = Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"]
CreateAccountFailureReasonType = Literal[
    "ACCOUNT_LIMIT_EXCEEDED",
    "CONCURRENT_ACCOUNT_MODIFICATION",
    "EMAIL_ALREADY_EXISTS",
    "FAILED_BUSINESS_VALIDATION",
    "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
    "INTERNAL_FAILURE",
    "INVALID_ADDRESS",
    "INVALID_EMAIL",
    "INVALID_IDENTITY_FOR_BUSINESS_VALIDATION",
    "MISSING_BUSINESS_VALIDATION",
    "MISSING_PAYMENT_INSTRUMENT",
    "PENDING_BUSINESS_VALIDATION",
    "UNKNOWN_BUSINESS_VALIDATION",
]
CreateAccountStateType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
EffectivePolicyTypeType = Literal["AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "TAG_POLICY"]
HandshakePartyTypeType = Literal["ACCOUNT", "EMAIL", "ORGANIZATION"]
HandshakeResourceTypeType = Literal[
    "ACCOUNT",
    "EMAIL",
    "MASTER_EMAIL",
    "MASTER_NAME",
    "NOTES",
    "ORGANIZATION",
    "ORGANIZATION_FEATURE_SET",
    "PARENT_HANDSHAKE",
]
HandshakeStateType = Literal["ACCEPTED", "CANCELED", "DECLINED", "EXPIRED", "OPEN", "REQUESTED"]
IAMUserAccessToBillingType = Literal["ALLOW", "DENY"]
ListAWSServiceAccessForOrganizationPaginatorName = Literal[
    "list_aws_service_access_for_organization"
]
ListAccountsForParentPaginatorName = Literal["list_accounts_for_parent"]
ListAccountsPaginatorName = Literal["list_accounts"]
ListChildrenPaginatorName = Literal["list_children"]
ListCreateAccountStatusPaginatorName = Literal["list_create_account_status"]
ListDelegatedAdministratorsPaginatorName = Literal["list_delegated_administrators"]
ListDelegatedServicesForAccountPaginatorName = Literal["list_delegated_services_for_account"]
ListHandshakesForAccountPaginatorName = Literal["list_handshakes_for_account"]
ListHandshakesForOrganizationPaginatorName = Literal["list_handshakes_for_organization"]
ListOrganizationalUnitsForParentPaginatorName = Literal["list_organizational_units_for_parent"]
ListParentsPaginatorName = Literal["list_parents"]
ListPoliciesForTargetPaginatorName = Literal["list_policies_for_target"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListRootsPaginatorName = Literal["list_roots"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTargetsForPolicyPaginatorName = Literal["list_targets_for_policy"]
OrganizationFeatureSetType = Literal["ALL", "CONSOLIDATED_BILLING"]
ParentTypeType = Literal["ORGANIZATIONAL_UNIT", "ROOT"]
PolicyTypeStatusType = Literal["ENABLED", "PENDING_DISABLE", "PENDING_ENABLE"]
PolicyTypeType = Literal[
    "AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "SERVICE_CONTROL_POLICY", "TAG_POLICY"
]
TargetTypeType = Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "alexaforbusiness",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "backup",
    "backup-gateway",
    "batch",
    "braket",
    "budgets",
    "ce",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecommit",
    "codedeploy",
    "codeguru-reviewer",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectparticipant",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "dax",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "drs",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "fsx",
    "gamelift",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "honeycode",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector2",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "machinelearning",
    "macie",
    "macie2",
    "managedblockchain",
    "marketplace-catalog",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhubstrategy",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "network-firewall",
    "networkmanager",
    "nimble",
    "opensearch",
    "opsworks",
    "opsworkscm",
    "organizations",
    "outposts",
    "panorama",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "polly",
    "pricing",
    "proton",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "rekognition",
    "resiliencehub",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-runtime",
    "savingsplans",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "support",
    "swf",
    "synthetics",
    "textract",
    "timestream-query",
    "timestream-write",
    "transcribe",
    "transfer",
    "translate",
    "voice-id",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-web",
    "xray",
]
PaginatorName = Literal[
    "list_accounts",
    "list_accounts_for_parent",
    "list_aws_service_access_for_organization",
    "list_children",
    "list_create_account_status",
    "list_delegated_administrators",
    "list_delegated_services_for_account",
    "list_handshakes_for_account",
    "list_handshakes_for_organization",
    "list_organizational_units_for_parent",
    "list_parents",
    "list_policies",
    "list_policies_for_target",
    "list_roots",
    "list_tags_for_resource",
    "list_targets_for_policy",
]
