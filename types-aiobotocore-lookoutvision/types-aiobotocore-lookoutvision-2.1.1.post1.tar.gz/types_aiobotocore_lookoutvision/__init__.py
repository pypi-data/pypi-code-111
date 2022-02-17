"""
Main interface for lookoutvision service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_lookoutvision import (
        Client,
        ListDatasetEntriesPaginator,
        ListModelPackagingJobsPaginator,
        ListModelsPaginator,
        ListProjectsPaginator,
        LookoutforVisionClient,
    )

    session = get_session()
    async with session.create_client("lookoutvision") as client:
        client: LookoutforVisionClient
        ...


    list_dataset_entries_paginator: ListDatasetEntriesPaginator = client.get_paginator("list_dataset_entries")
    list_model_packaging_jobs_paginator: ListModelPackagingJobsPaginator = client.get_paginator("list_model_packaging_jobs")
    list_models_paginator: ListModelsPaginator = client.get_paginator("list_models")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from .client import LookoutforVisionClient
from .paginator import (
    ListDatasetEntriesPaginator,
    ListModelPackagingJobsPaginator,
    ListModelsPaginator,
    ListProjectsPaginator,
)

Client = LookoutforVisionClient


__all__ = (
    "Client",
    "ListDatasetEntriesPaginator",
    "ListModelPackagingJobsPaginator",
    "ListModelsPaginator",
    "ListProjectsPaginator",
    "LookoutforVisionClient",
)
