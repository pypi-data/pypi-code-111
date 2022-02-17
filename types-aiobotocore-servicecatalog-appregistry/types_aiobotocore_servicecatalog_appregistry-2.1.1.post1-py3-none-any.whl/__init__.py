"""
Main interface for servicecatalog-appregistry service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_servicecatalog_appregistry import (
        AppRegistryClient,
        Client,
        ListApplicationsPaginator,
        ListAssociatedAttributeGroupsPaginator,
        ListAssociatedResourcesPaginator,
        ListAttributeGroupsPaginator,
    )

    session = get_session()
    async with session.create_client("servicecatalog-appregistry") as client:
        client: AppRegistryClient
        ...


    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_associated_attribute_groups_paginator: ListAssociatedAttributeGroupsPaginator = client.get_paginator("list_associated_attribute_groups")
    list_associated_resources_paginator: ListAssociatedResourcesPaginator = client.get_paginator("list_associated_resources")
    list_attribute_groups_paginator: ListAttributeGroupsPaginator = client.get_paginator("list_attribute_groups")
    ```
"""
from .client import AppRegistryClient
from .paginator import (
    ListApplicationsPaginator,
    ListAssociatedAttributeGroupsPaginator,
    ListAssociatedResourcesPaginator,
    ListAttributeGroupsPaginator,
)

Client = AppRegistryClient


__all__ = (
    "AppRegistryClient",
    "Client",
    "ListApplicationsPaginator",
    "ListAssociatedAttributeGroupsPaginator",
    "ListAssociatedResourcesPaginator",
    "ListAttributeGroupsPaginator",
)
