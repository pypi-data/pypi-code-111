"""
Type annotations for rekognition service literal definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/literals.html)

Usage::

    ```python
    from types_aiobotocore_rekognition.literals import AttributeType

    data: AttributeType = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AttributeType",
    "BodyPartType",
    "CelebrityRecognitionSortByType",
    "ContentClassifierType",
    "ContentModerationSortByType",
    "DatasetStatusMessageCodeType",
    "DatasetStatusType",
    "DatasetTypeType",
    "DescribeProjectVersionsPaginatorName",
    "DescribeProjectsPaginatorName",
    "EmotionNameType",
    "FaceAttributesType",
    "FaceSearchSortByType",
    "GenderTypeType",
    "KnownGenderTypeType",
    "LabelDetectionSortByType",
    "LandmarkTypeType",
    "ListCollectionsPaginatorName",
    "ListDatasetEntriesPaginatorName",
    "ListDatasetLabelsPaginatorName",
    "ListFacesPaginatorName",
    "ListStreamProcessorsPaginatorName",
    "OrientationCorrectionType",
    "PersonTrackingSortByType",
    "ProjectStatusType",
    "ProjectVersionRunningWaiterName",
    "ProjectVersionStatusType",
    "ProjectVersionTrainingCompletedWaiterName",
    "ProtectiveEquipmentTypeType",
    "QualityFilterType",
    "ReasonType",
    "SegmentTypeType",
    "StreamProcessorStatusType",
    "TechnicalCueTypeType",
    "TextTypesType",
    "VideoColorRangeType",
    "VideoJobStatusType",
    "ServiceName",
    "PaginatorName",
    "WaiterName",
)


AttributeType = Literal["ALL", "DEFAULT"]
BodyPartType = Literal["FACE", "HEAD", "LEFT_HAND", "RIGHT_HAND"]
CelebrityRecognitionSortByType = Literal["ID", "TIMESTAMP"]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
ContentModerationSortByType = Literal["NAME", "TIMESTAMP"]
DatasetStatusMessageCodeType = Literal["CLIENT_ERROR", "SERVICE_ERROR", "SUCCESS"]
DatasetStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
DatasetTypeType = Literal["TEST", "TRAIN"]
DescribeProjectVersionsPaginatorName = Literal["describe_project_versions"]
DescribeProjectsPaginatorName = Literal["describe_projects"]
EmotionNameType = Literal[
    "ANGRY", "CALM", "CONFUSED", "DISGUSTED", "FEAR", "HAPPY", "SAD", "SURPRISED", "UNKNOWN"
]
FaceAttributesType = Literal["ALL", "DEFAULT"]
FaceSearchSortByType = Literal["INDEX", "TIMESTAMP"]
GenderTypeType = Literal["Female", "Male"]
KnownGenderTypeType = Literal["Female", "Male", "Nonbinary", "Unlisted"]
LabelDetectionSortByType = Literal["NAME", "TIMESTAMP"]
LandmarkTypeType = Literal[
    "chinBottom",
    "eyeLeft",
    "eyeRight",
    "leftEyeBrowLeft",
    "leftEyeBrowRight",
    "leftEyeBrowUp",
    "leftEyeDown",
    "leftEyeLeft",
    "leftEyeRight",
    "leftEyeUp",
    "leftPupil",
    "midJawlineLeft",
    "midJawlineRight",
    "mouthDown",
    "mouthLeft",
    "mouthRight",
    "mouthUp",
    "nose",
    "noseLeft",
    "noseRight",
    "rightEyeBrowLeft",
    "rightEyeBrowRight",
    "rightEyeBrowUp",
    "rightEyeDown",
    "rightEyeLeft",
    "rightEyeRight",
    "rightEyeUp",
    "rightPupil",
    "upperJawlineLeft",
    "upperJawlineRight",
]
ListCollectionsPaginatorName = Literal["list_collections"]
ListDatasetEntriesPaginatorName = Literal["list_dataset_entries"]
ListDatasetLabelsPaginatorName = Literal["list_dataset_labels"]
ListFacesPaginatorName = Literal["list_faces"]
ListStreamProcessorsPaginatorName = Literal["list_stream_processors"]
OrientationCorrectionType = Literal["ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"]
PersonTrackingSortByType = Literal["INDEX", "TIMESTAMP"]
ProjectStatusType = Literal["CREATED", "CREATING", "DELETING"]
ProjectVersionRunningWaiterName = Literal["project_version_running"]
ProjectVersionStatusType = Literal[
    "DELETING",
    "FAILED",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "TRAINING_COMPLETED",
    "TRAINING_FAILED",
    "TRAINING_IN_PROGRESS",
]
ProjectVersionTrainingCompletedWaiterName = Literal["project_version_training_completed"]
ProtectiveEquipmentTypeType = Literal["FACE_COVER", "HAND_COVER", "HEAD_COVER"]
QualityFilterType = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "NONE"]
ReasonType = Literal[
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "LOW_BRIGHTNESS",
    "LOW_CONFIDENCE",
    "LOW_FACE_QUALITY",
    "LOW_SHARPNESS",
    "SMALL_BOUNDING_BOX",
]
SegmentTypeType = Literal["SHOT", "TECHNICAL_CUE"]
StreamProcessorStatusType = Literal["FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING"]
TechnicalCueTypeType = Literal[
    "BlackFrames", "ColorBars", "Content", "EndCredits", "OpeningCredits", "Slate", "StudioLogo"
]
TextTypesType = Literal["LINE", "WORD"]
VideoColorRangeType = Literal["FULL", "LIMITED"]
VideoJobStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
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
    "describe_project_versions",
    "describe_projects",
    "list_collections",
    "list_dataset_entries",
    "list_dataset_labels",
    "list_faces",
    "list_stream_processors",
]
WaiterName = Literal["project_version_running", "project_version_training_completed"]
