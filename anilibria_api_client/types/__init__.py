"""Auto-generated public enum facade for AniLiberty OpenAPI.

DO NOT EDIT MANUALLY.
"""

from __future__ import annotations

from enum import Enum

from .codegen import openapi_models as _generated

_GENERATED_TYPE_EXPORTS = (

)

for _name in _GENERATED_TYPE_EXPORTS:
    globals()[_name] = getattr(_generated, _name)


class CollectionType(str, Enum):
    PLANNED = "PLANNED"
    WATCHED = "WATCHED"
    WATCHING = "WATCHING"
    POSTPONED = "POSTPONED"
    ABANDONED = "ABANDONED"


class ContentType(str, Enum):
    TV = "TV"
    ONA = "ONA"
    WEB = "WEB"
    OVA = "OVA"
    OAD = "OAD"
    MOVIE = "MOVIE"
    DORAMA = "DORAMA"
    SPECIAL = "SPECIAL"


class AgeRating(str, Enum):
    R0_PLUS = "R0_PLUS"
    R6_PLUS = "R6_PLUS"
    R12_PLUS = "R12_PLUS"
    R16_PLUS = "R16_PLUS"
    R18_PLUS = "R18_PLUS"


class Seasons(str, Enum):
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"


class SortType(str, Enum):
    FRESH_AT_DESC = "FRESH_AT_DESC"
    FRESH_AT_ASC = "FRESH_AT_ASC"
    RATING_DESC = "RATING_DESC"
    RATING_ASC = "RATING_ASC"
    YEAR_DESC = "YEAR_DESC"
    YEAR_ASC = "YEAR_ASC"


class PublishStatusesType(str, Enum):
    IS_ONGOING = "IS_ONGOING"
    IS_NOT_ONGOING = "IS_NOT_ONGOING"


class ProductionStatusesType(str, Enum):
    IS_IN_PRODUCTION = "IS_IN_PRODUCTION"
    IS_NOT_IN_PRODUCTION = "IS_NOT_IN_PRODUCTION"


__all__ = [
    "CollectionType",
    "ContentType",
    "AgeRating",
    "Seasons",
    "SortType",
    "PublishStatusesType",
    "ProductionStatusesType",
    *_GENERATED_TYPE_EXPORTS,
]
