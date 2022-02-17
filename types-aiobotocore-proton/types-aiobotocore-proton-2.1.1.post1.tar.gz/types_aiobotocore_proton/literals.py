"""
Type annotations for proton service literal definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_proton/literals.html)

Usage::

    ```python
    from types_aiobotocore_proton.literals import DeploymentStatusType

    data: DeploymentStatusType = "CANCELLED"
    ```
"""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DeploymentStatusType",
    "DeploymentUpdateTypeType",
    "EnvironmentAccountConnectionRequesterAccountTypeType",
    "EnvironmentAccountConnectionStatusType",
    "EnvironmentDeployedWaiterName",
    "EnvironmentTemplateVersionRegisteredWaiterName",
    "ListEnvironmentAccountConnectionsPaginatorName",
    "ListEnvironmentOutputsPaginatorName",
    "ListEnvironmentProvisionedResourcesPaginatorName",
    "ListEnvironmentTemplateVersionsPaginatorName",
    "ListEnvironmentTemplatesPaginatorName",
    "ListEnvironmentsPaginatorName",
    "ListRepositoriesPaginatorName",
    "ListRepositorySyncDefinitionsPaginatorName",
    "ListServiceInstanceOutputsPaginatorName",
    "ListServiceInstanceProvisionedResourcesPaginatorName",
    "ListServiceInstancesPaginatorName",
    "ListServicePipelineOutputsPaginatorName",
    "ListServicePipelineProvisionedResourcesPaginatorName",
    "ListServiceTemplateVersionsPaginatorName",
    "ListServiceTemplatesPaginatorName",
    "ListServicesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ProvisionedResourceEngineType",
    "ProvisioningType",
    "RepositoryProviderType",
    "RepositorySyncStatusType",
    "ResourceDeploymentStatusType",
    "ResourceSyncStatusType",
    "ServiceCreatedWaiterName",
    "ServiceDeletedWaiterName",
    "ServiceInstanceDeployedWaiterName",
    "ServicePipelineDeployedWaiterName",
    "ServiceStatusType",
    "ServiceTemplateVersionRegisteredWaiterName",
    "ServiceUpdatedWaiterName",
    "SyncTypeType",
    "TemplateTypeType",
    "TemplateVersionStatusType",
    "ServiceName",
    "PaginatorName",
    "WaiterName",
)


DeploymentStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "FAILED",
    "IN_PROGRESS",
    "SUCCEEDED",
]
DeploymentUpdateTypeType = Literal["CURRENT_VERSION", "MAJOR_VERSION", "MINOR_VERSION", "NONE"]
EnvironmentAccountConnectionRequesterAccountTypeType = Literal[
    "ENVIRONMENT_ACCOUNT", "MANAGEMENT_ACCOUNT"
]
EnvironmentAccountConnectionStatusType = Literal["CONNECTED", "PENDING", "REJECTED"]
EnvironmentDeployedWaiterName = Literal["environment_deployed"]
EnvironmentTemplateVersionRegisteredWaiterName = Literal["environment_template_version_registered"]
ListEnvironmentAccountConnectionsPaginatorName = Literal["list_environment_account_connections"]
ListEnvironmentOutputsPaginatorName = Literal["list_environment_outputs"]
ListEnvironmentProvisionedResourcesPaginatorName = Literal["list_environment_provisioned_resources"]
ListEnvironmentTemplateVersionsPaginatorName = Literal["list_environment_template_versions"]
ListEnvironmentTemplatesPaginatorName = Literal["list_environment_templates"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
ListRepositoriesPaginatorName = Literal["list_repositories"]
ListRepositorySyncDefinitionsPaginatorName = Literal["list_repository_sync_definitions"]
ListServiceInstanceOutputsPaginatorName = Literal["list_service_instance_outputs"]
ListServiceInstanceProvisionedResourcesPaginatorName = Literal[
    "list_service_instance_provisioned_resources"
]
ListServiceInstancesPaginatorName = Literal["list_service_instances"]
ListServicePipelineOutputsPaginatorName = Literal["list_service_pipeline_outputs"]
ListServicePipelineProvisionedResourcesPaginatorName = Literal[
    "list_service_pipeline_provisioned_resources"
]
ListServiceTemplateVersionsPaginatorName = Literal["list_service_template_versions"]
ListServiceTemplatesPaginatorName = Literal["list_service_templates"]
ListServicesPaginatorName = Literal["list_services"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ProvisionedResourceEngineType = Literal["CLOUDFORMATION", "TERRAFORM"]
ProvisioningType = Literal["CUSTOMER_MANAGED"]
RepositoryProviderType = Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"]
RepositorySyncStatusType = Literal["FAILED", "INITIATED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
ResourceDeploymentStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ResourceSyncStatusType = Literal["FAILED", "INITIATED", "IN_PROGRESS", "SUCCEEDED"]
ServiceCreatedWaiterName = Literal["service_created"]
ServiceDeletedWaiterName = Literal["service_deleted"]
ServiceInstanceDeployedWaiterName = Literal["service_instance_deployed"]
ServicePipelineDeployedWaiterName = Literal["service_pipeline_deployed"]
ServiceStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_FAILED_CLEANUP_COMPLETE",
    "CREATE_FAILED_CLEANUP_FAILED",
    "CREATE_FAILED_CLEANUP_IN_PROGRESS",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE_CLEANUP_FAILED",
    "UPDATE_FAILED",
    "UPDATE_FAILED_CLEANUP_COMPLETE",
    "UPDATE_FAILED_CLEANUP_FAILED",
    "UPDATE_FAILED_CLEANUP_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
]
ServiceTemplateVersionRegisteredWaiterName = Literal["service_template_version_registered"]
ServiceUpdatedWaiterName = Literal["service_updated"]
SyncTypeType = Literal["TEMPLATE_SYNC"]
TemplateTypeType = Literal["ENVIRONMENT", "SERVICE"]
TemplateVersionStatusType = Literal[
    "DRAFT", "PUBLISHED", "REGISTRATION_FAILED", "REGISTRATION_IN_PROGRESS"
]
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
    "list_environment_account_connections",
    "list_environment_outputs",
    "list_environment_provisioned_resources",
    "list_environment_template_versions",
    "list_environment_templates",
    "list_environments",
    "list_repositories",
    "list_repository_sync_definitions",
    "list_service_instance_outputs",
    "list_service_instance_provisioned_resources",
    "list_service_instances",
    "list_service_pipeline_outputs",
    "list_service_pipeline_provisioned_resources",
    "list_service_template_versions",
    "list_service_templates",
    "list_services",
    "list_tags_for_resource",
]
WaiterName = Literal[
    "environment_deployed",
    "environment_template_version_registered",
    "service_created",
    "service_deleted",
    "service_instance_deployed",
    "service_pipeline_deployed",
    "service_template_version_registered",
    "service_updated",
]
