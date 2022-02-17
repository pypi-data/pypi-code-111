from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from typing import List, Optional, Union
from datetime import time


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Schedule(Intangible):
    """A schedule defines a repeating time period used to describe a regularly occurring [[Event]]."
     "At a minimum a schedule will specify [[repeatFrequency]] which describes the interval"
     "between occurences of the event. Additional information can be provided to specify"
     "the schedule more precisely. This includes identifying the day(s) of the week or month"
     "when the recurring event will take place, in addition to its start and end time. Schedules"
     "may also have start and end dates to indicate when they are active, e.g. to define a limited"
     "calendar of events.

    See: https://schema.org/Schedule
    Model depth: 3
    """
    type_: str = Field("Schedule", alias='@type')
    exceptDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        default=None,
        description="Defines a [[Date]] or [[DateTime]] during which a scheduled [[Event]] will not take"
     "place. The property allows exceptions to a [[Schedule]] to be specified. If an exception"
     "is specified as a [[DateTime]] then only the event that would have started at that specific"
     "date and time should be excluded from the schedule. If an exception is specified as a [[Date]]"
     "then any event that is scheduled for that 24 hour period should be excluded from the schedule."
     "This allows a whole day to be excluded from the schedule without having to itemise every"
     "scheduled event.",
    )
    scheduleTimezone: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates the timezone for which the time(s) indicated in the [[Schedule]] are given."
     "The value provided should be among those listed in the IANA Time Zone Database.",
    )
    byDay: Optional[Union[List[Union[str, 'Text', 'DayOfWeek']], str, 'Text', 'DayOfWeek']] = Field(
        default=None,
        description="Defines the day(s) of the week on which a recurring [[Event]] takes place. May be specified"
     "using either [[DayOfWeek]], or alternatively [[Text]] conforming to iCal's syntax"
     "for byDay recurrence rules.",
    )
    byMonthDay: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Defines the day(s) of the month on which a recurring [[Event]] takes place. Specified"
     "as an [[Integer]] between 1-31.",
    )
    duration: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    repeatCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Defines the number of times a recurring [[Event]] will take place",
    )
    endTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', str]], ISO8601Date, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    endDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    repeatFrequency: Optional[Union[List[Union[str, 'Text', 'Duration']], str, 'Text', 'Duration']] = Field(
        default=None,
        description="Defines the frequency at which [[Event]]s will occur according to a schedule [[Schedule]]."
     "The intervals between events should be defined as a [[Duration]] of time.",
    )
    byMonthWeek: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Defines the week(s) of the month on which a recurring Event takes place. Specified as"
     "an Integer between 1-5. For clarity, byMonthWeek is best used in conjunction with byDay"
     "to indicate concepts like the first and third Mondays of a month.",
    )
    byMonth: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Defines the month(s) of the year on which a recurring [[Event]] takes place. Specified"
     "as an [[Integer]] between 1-12. January is 1.",
    )
    startDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    startTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', str]], ISO8601Date, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DayOfWeek import DayOfWeek
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Time import Time
