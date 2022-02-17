from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Accommodation import Accommodation


class CampingPitch(Accommodation):
    """A [[CampingPitch]] is an individual place for overnight stay in the outdoors, typically"
     "being part of a larger camping site, or [[Campground]]. In British English a campsite,"
     "or campground, is an area, usually divided into a number of pitches, where people can"
     "camp overnight using tents or camper vans or caravans; this British English use of the"
     "word is synonymous with the American English expression campground. In American English"
     "the term campsite generally means an area where an individual, family, group, or military"
     "unit can pitch a tent or park a camper; a campground may contain many campsites. (Source:"
     "Wikipedia see [https://en.wikipedia.org/wiki/Campsite](https://en.wikipedia.org/wiki/Campsite))."
     "See also the dedicated [document on the use of schema.org for marking up hotels and other"
     "forms of accommodations](/docs/hotels.html).

    See: https://schema.org/CampingPitch
    Model depth: 4
    """
    type_: str = Field("CampingPitch", alias='@type')
    

