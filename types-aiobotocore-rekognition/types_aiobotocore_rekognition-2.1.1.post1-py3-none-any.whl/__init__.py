"""
Main interface for rekognition service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_rekognition import (
        Client,
        DescribeProjectVersionsPaginator,
        DescribeProjectsPaginator,
        ListCollectionsPaginator,
        ListDatasetEntriesPaginator,
        ListDatasetLabelsPaginator,
        ListFacesPaginator,
        ListStreamProcessorsPaginator,
        ProjectVersionRunningWaiter,
        ProjectVersionTrainingCompletedWaiter,
        RekognitionClient,
    )

    session = get_session()
    async with session.create_client("rekognition") as client:
        client: RekognitionClient
        ...


    project_version_running_waiter: ProjectVersionRunningWaiter = client.get_waiter("project_version_running")
    project_version_training_completed_waiter: ProjectVersionTrainingCompletedWaiter = client.get_waiter("project_version_training_completed")

    describe_project_versions_paginator: DescribeProjectVersionsPaginator = client.get_paginator("describe_project_versions")
    describe_projects_paginator: DescribeProjectsPaginator = client.get_paginator("describe_projects")
    list_collections_paginator: ListCollectionsPaginator = client.get_paginator("list_collections")
    list_dataset_entries_paginator: ListDatasetEntriesPaginator = client.get_paginator("list_dataset_entries")
    list_dataset_labels_paginator: ListDatasetLabelsPaginator = client.get_paginator("list_dataset_labels")
    list_faces_paginator: ListFacesPaginator = client.get_paginator("list_faces")
    list_stream_processors_paginator: ListStreamProcessorsPaginator = client.get_paginator("list_stream_processors")
    ```
"""
from .client import RekognitionClient
from .paginator import (
    DescribeProjectsPaginator,
    DescribeProjectVersionsPaginator,
    ListCollectionsPaginator,
    ListDatasetEntriesPaginator,
    ListDatasetLabelsPaginator,
    ListFacesPaginator,
    ListStreamProcessorsPaginator,
)
from .waiter import ProjectVersionRunningWaiter, ProjectVersionTrainingCompletedWaiter

Client = RekognitionClient


__all__ = (
    "Client",
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListDatasetEntriesPaginator",
    "ListDatasetLabelsPaginator",
    "ListFacesPaginator",
    "ListStreamProcessorsPaginator",
    "ProjectVersionRunningWaiter",
    "ProjectVersionTrainingCompletedWaiter",
    "RekognitionClient",
)
