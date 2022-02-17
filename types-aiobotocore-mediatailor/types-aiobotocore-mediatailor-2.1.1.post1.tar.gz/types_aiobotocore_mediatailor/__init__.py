"""
Main interface for mediatailor service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_mediatailor import (
        Client,
        GetChannelSchedulePaginator,
        ListAlertsPaginator,
        ListChannelsPaginator,
        ListPlaybackConfigurationsPaginator,
        ListPrefetchSchedulesPaginator,
        ListSourceLocationsPaginator,
        ListVodSourcesPaginator,
        MediaTailorClient,
    )

    session = get_session()
    async with session.create_client("mediatailor") as client:
        client: MediaTailorClient
        ...


    get_channel_schedule_paginator: GetChannelSchedulePaginator = client.get_paginator("get_channel_schedule")
    list_alerts_paginator: ListAlertsPaginator = client.get_paginator("list_alerts")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_playback_configurations_paginator: ListPlaybackConfigurationsPaginator = client.get_paginator("list_playback_configurations")
    list_prefetch_schedules_paginator: ListPrefetchSchedulesPaginator = client.get_paginator("list_prefetch_schedules")
    list_source_locations_paginator: ListSourceLocationsPaginator = client.get_paginator("list_source_locations")
    list_vod_sources_paginator: ListVodSourcesPaginator = client.get_paginator("list_vod_sources")
    ```
"""
from .client import MediaTailorClient
from .paginator import (
    GetChannelSchedulePaginator,
    ListAlertsPaginator,
    ListChannelsPaginator,
    ListPlaybackConfigurationsPaginator,
    ListPrefetchSchedulesPaginator,
    ListSourceLocationsPaginator,
    ListVodSourcesPaginator,
)

Client = MediaTailorClient


__all__ = (
    "Client",
    "GetChannelSchedulePaginator",
    "ListAlertsPaginator",
    "ListChannelsPaginator",
    "ListPlaybackConfigurationsPaginator",
    "ListPrefetchSchedulesPaginator",
    "ListSourceLocationsPaginator",
    "ListVodSourcesPaginator",
    "MediaTailorClient",
)
