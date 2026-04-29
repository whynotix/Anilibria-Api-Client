"""
This code is legacy
Last edited in 0.2.2 version
"""

from enum import Enum

from pydantic import BaseModel


class CollectionType(Enum):
    """Типы коллекций"""

    PLANNED = "PLANNED"
    WATCHED = "WATCHED"
    WATCHING = "WATCHING"
    POSTPONED = "POSTPONED"
    ABANDONED = "ABANDONED"


class ContentType(Enum):
    """Типы контента"""

    TV = "TV"
    ONA = "ONA"
    WEB = "WEB"
    OVA = "OVA"
    OAD = "OAD"
    MOVIE = "MOVIE"
    DORAMA = "DORAMA"
    SPECIAL = "SPECIAL"


class AgeRating(Enum):
    """Возрастные рейтинги"""

    R0_PLUS = "R0_PLUS"
    R6_PLUS = "R6_PLUS"
    R12_PLUS = "R12_PLUS"
    R16_PLUS = "R16_PLUS"
    R18_PLUS = "R18_PLUS"


class Seasons(Enum):
    """Сезоны"""

    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"


class SortType(Enum):
    """Тип сортировки"""

    FRESH_AT_DESC = "FRESH_AT_DESC"
    FRESH_AT_ASC = "FRESH_AT_ASC"
    RATING_DESC = "RATING_DESC"
    RATING_ASC = "RATING_ASC"
    YEAR_DESC = "YEAR_DESC"
    YEAR_ASC = "YEAR_ASC"


class PublishStatusesType(Enum):
    """Статус аниме (онгоинг)"""

    IS_ONGOING = "IS_ONGOING"
    IS_NOT_ONGOING = "IS_NOT_ONGOING"


class ProductionStatusesType(Enum):
    """Статус аниме (в озвучке)"""

    IS_IN_PRODUCTION = "IS_IN_PRODUCTION"
    IS_NOT_IN_PRODUCTION = "IS_NOT_IN_PRODUCTION"


class TimeCode(BaseModel):
    """
    Класс для работы с этими методами:

    accounts.users_me_views_timecodes_update
    """

    time: int
    is_watched: bool
    release_episode_id: str


class Release(BaseModel):
    """
    Класс для работы с этими методами:

    anime.catalog_releases_get

    anime.catalog_releases_post
    """

    page: int | None = None
    limit: int | None = None
    genres: str | None = None
    types: list[ContentType] | None = None
    seasons: list[Seasons] | None = None
    from_year: int | None = None
    to_year: int | None = None
    search: str | None = None
    sorting: SortType | None = None
    age_ratings: list[AgeRating] | None = None
    publish_statuses: list[PublishStatusesType] | None = None
    production_statuses: list[ProductionStatusesType] | None = None
    include: str | None = None
    exclude: str | None = None


class ReleaseCollection(BaseModel):
    """
    Класс для работы с этими методами

    users_me_collections_releases_get

    users_me_collections_releases_post
    """

    type_of_collection: CollectionType
    page: int | None = None
    limit: int | None = None
    genres: str | None = None
    types: list[ContentType] | None = None
    years: str | None = None
    search: str | None = None
    age_ratings: list[AgeRating] | None = None
    include: str | None = None
    exclude: str | None = None


"""Legacy code end"""
