"""
Type annotations for lexv2-models service literal definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lexv2_models/literals.html)

Usage::

    ```python
    from types_aiobotocore_lexv2_models.literals import AggregatedUtterancesFilterNameType

    data: AggregatedUtterancesFilterNameType = "Utterance"
    ```
"""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AggregatedUtterancesFilterNameType",
    "AggregatedUtterancesFilterOperatorType",
    "AggregatedUtterancesSortAttributeType",
    "AssociatedTranscriptFilterNameType",
    "BotAliasAvailableWaiterName",
    "BotAliasStatusType",
    "BotAvailableWaiterName",
    "BotExportCompletedWaiterName",
    "BotFilterNameType",
    "BotFilterOperatorType",
    "BotImportCompletedWaiterName",
    "BotLocaleBuiltWaiterName",
    "BotLocaleCreatedWaiterName",
    "BotLocaleExpressTestingAvailableWaiterName",
    "BotLocaleFilterNameType",
    "BotLocaleFilterOperatorType",
    "BotLocaleSortAttributeType",
    "BotLocaleStatusType",
    "BotRecommendationStatusType",
    "BotSortAttributeType",
    "BotStatusType",
    "BotVersionAvailableWaiterName",
    "BotVersionSortAttributeType",
    "BuiltInIntentSortAttributeType",
    "BuiltInSlotTypeSortAttributeType",
    "EffectType",
    "ExportFilterNameType",
    "ExportFilterOperatorType",
    "ExportSortAttributeType",
    "ExportStatusType",
    "ImportExportFileFormatType",
    "ImportFilterNameType",
    "ImportFilterOperatorType",
    "ImportSortAttributeType",
    "ImportStatusType",
    "IntentFilterNameType",
    "IntentFilterOperatorType",
    "IntentSortAttributeType",
    "MergeStrategyType",
    "ObfuscationSettingTypeType",
    "SearchOrderType",
    "SlotConstraintType",
    "SlotFilterNameType",
    "SlotFilterOperatorType",
    "SlotSortAttributeType",
    "SlotTypeCategoryType",
    "SlotTypeFilterNameType",
    "SlotTypeFilterOperatorType",
    "SlotTypeSortAttributeType",
    "SlotValueResolutionStrategyType",
    "SortOrderType",
    "TimeDimensionType",
    "TranscriptFormatType",
    "VoiceEngineType",
    "ServiceName",
    "WaiterName",
)


AggregatedUtterancesFilterNameType = Literal["Utterance"]
AggregatedUtterancesFilterOperatorType = Literal["CO", "EQ"]
AggregatedUtterancesSortAttributeType = Literal["HitCount", "MissedCount"]
AssociatedTranscriptFilterNameType = Literal["IntentId", "SlotTypeId"]
BotAliasAvailableWaiterName = Literal["bot_alias_available"]
BotAliasStatusType = Literal["Available", "Creating", "Deleting", "Failed"]
BotAvailableWaiterName = Literal["bot_available"]
BotExportCompletedWaiterName = Literal["bot_export_completed"]
BotFilterNameType = Literal["BotName"]
BotFilterOperatorType = Literal["CO", "EQ"]
BotImportCompletedWaiterName = Literal["bot_import_completed"]
BotLocaleBuiltWaiterName = Literal["bot_locale_built"]
BotLocaleCreatedWaiterName = Literal["bot_locale_created"]
BotLocaleExpressTestingAvailableWaiterName = Literal["bot_locale_express_testing_available"]
BotLocaleFilterNameType = Literal["BotLocaleName"]
BotLocaleFilterOperatorType = Literal["CO", "EQ"]
BotLocaleSortAttributeType = Literal["BotLocaleName"]
BotLocaleStatusType = Literal[
    "Building",
    "Built",
    "Creating",
    "Deleting",
    "Failed",
    "Importing",
    "NotBuilt",
    "Processing",
    "ReadyExpressTesting",
]
BotRecommendationStatusType = Literal[
    "Available", "Deleted", "Deleting", "Downloading", "Failed", "Processing", "Updating"
]
BotSortAttributeType = Literal["BotName"]
BotStatusType = Literal[
    "Available", "Creating", "Deleting", "Failed", "Importing", "Inactive", "Versioning"
]
BotVersionAvailableWaiterName = Literal["bot_version_available"]
BotVersionSortAttributeType = Literal["BotVersion"]
BuiltInIntentSortAttributeType = Literal["IntentSignature"]
BuiltInSlotTypeSortAttributeType = Literal["SlotTypeSignature"]
EffectType = Literal["Allow", "Deny"]
ExportFilterNameType = Literal["ExportResourceType"]
ExportFilterOperatorType = Literal["CO", "EQ"]
ExportSortAttributeType = Literal["LastUpdatedDateTime"]
ExportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
ImportExportFileFormatType = Literal["LexJson"]
ImportFilterNameType = Literal["ImportResourceType"]
ImportFilterOperatorType = Literal["CO", "EQ"]
ImportSortAttributeType = Literal["LastUpdatedDateTime"]
ImportStatusType = Literal["Completed", "Deleting", "Failed", "InProgress"]
IntentFilterNameType = Literal["IntentName"]
IntentFilterOperatorType = Literal["CO", "EQ"]
IntentSortAttributeType = Literal["IntentName", "LastUpdatedDateTime"]
MergeStrategyType = Literal["Append", "FailOnConflict", "Overwrite"]
ObfuscationSettingTypeType = Literal["DefaultObfuscation", "None"]
SearchOrderType = Literal["Ascending", "Descending"]
SlotConstraintType = Literal["Optional", "Required"]
SlotFilterNameType = Literal["SlotName"]
SlotFilterOperatorType = Literal["CO", "EQ"]
SlotSortAttributeType = Literal["LastUpdatedDateTime", "SlotName"]
SlotTypeCategoryType = Literal["Custom", "Extended", "ExternalGrammar"]
SlotTypeFilterNameType = Literal["ExternalSourceType", "SlotTypeName"]
SlotTypeFilterOperatorType = Literal["CO", "EQ"]
SlotTypeSortAttributeType = Literal["LastUpdatedDateTime", "SlotTypeName"]
SlotValueResolutionStrategyType = Literal["OriginalValue", "TopResolution"]
SortOrderType = Literal["Ascending", "Descending"]
TimeDimensionType = Literal["Days", "Hours", "Weeks"]
TranscriptFormatType = Literal["Lex"]
VoiceEngineType = Literal["neural", "standard"]
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
WaiterName = Literal[
    "bot_alias_available",
    "bot_available",
    "bot_export_completed",
    "bot_import_completed",
    "bot_locale_built",
    "bot_locale_created",
    "bot_locale_express_testing_available",
    "bot_version_available",
]
