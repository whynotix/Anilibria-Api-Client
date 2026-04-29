from pydantic import BaseModel as PreBaseModel, AwareDatetime, ConfigDict
from typing import List


class BaseModel(PreBaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class OtpModel(BaseModel):
    code: str | None = None
    user_id: int | None = None
    device_id: str | None = None
    expired_at: AwareDatetime | None = None


class AgeRatingsModel(BaseModel):
    value: str | None = None
    label: str | None = None
    is_adult: bool | None = None
    description: str | None = None


class TypesModel(BaseModel):
    value: str | None = None
    description: str | None = None


class NameModel(BaseModel):
    main: str | None = None
    english: str | None = None
    alternative: str | None = None


class SeasonModel(BaseModel):
    value: str | None = None
    description: str | None = None


class PrePosterModel(BaseModel):
    preview: str | None = None
    thumbnail: str | None = None


class PosterModel(PrePosterModel):
    optimized: PrePosterModel | None = None


class PreImageModel(BaseModel):
    preview: str | None = None
    thumbnail: str | None = None


class ImageModel(PreImageModel):
    optimized: PreImageModel | None = None


class PublishDayModel(BaseModel):
    value: str | int | None = None
    description: str | None = None


class GenresModel(BaseModel):
    id: int | None = None
    name: str | None = None
    image: ImageModel | None = None
    total_releases: int | None = None


class EndingOpeningModel(BaseModel):
    start: int | None = None
    stop: int | None = None


class LinksModel(BaseModel):
    previous: str | None = None
    next: str | None = None


class PrePaginationModel(BaseModel):
    total: int | None = None
    count: int | None = None
    per_page: int | None = None
    current_page: int | None = None
    total_pages: int | None = None
    links: LinksModel | None = None


class PaginationModel(BaseModel):
    pagination: PrePaginationModel | None = None


class MetaModel(BaseModel):
    meta: PaginationModel | None = None


class PrePreviewModel(BaseModel):
    preview: str | None = None
    thumbnail: str | None = None


class PreviewModel(PrePreviewModel):
    optimized: PrePreviewModel | None = None


class EpisodeModel(BaseModel):
    id: str | None = None
    name: str | None = None
    ordinal: int | float | None = None
    ending: EndingOpeningModel | None = None
    opening: EndingOpeningModel | None = None
    preview: PreviewModel | None = None
    hls_480: str | None = None
    hls_720: str | None = None
    hls_1080: str | None = None
    duration: int | None = None
    rutube_id: str | None = None
    youtube_id: str | None = None
    updated_at: AwareDatetime | None = None
    sort_order: int | None = None
    release_id: int | None = None
    name_english: str | None = None


class ReleaseModel(BaseModel):
    id: int | None = None
    type: TypesModel | None = None
    year: int | None = None
    name: NameModel | None = None
    alias: str | None = None
    season: SeasonModel | None = None
    poster: PosterModel | None = None
    fresh_at: AwareDatetime | None = None
    created_at: AwareDatetime | None = None
    updated_at: AwareDatetime | None = None
    is_ongoing: bool | None = None
    age_rating: AgeRatingsModel | None = None
    publish_day: PublishDayModel | None = None
    description: str | None = None
    notification: str | None = None
    episodes_total: int | None = None
    external_player: str | None = None
    is_in_production: bool | None = None
    is_blocked_by_geo: bool | None = None
    is_blocked_by_copyrights: bool | None = None
    added_in_users_favorites: int | None = None
    average_duration_of_episode: int | None = None
    added_in_planned_collection: int | None = None
    added_in_watched_collection: int | None = None
    added_in_watching_collection: int | None = None
    added_in_postponed_collection: int | None = None
    added_in_abandoned_collection: int | None = None
    genres: List[GenresModel] | None = None
    episodes: List[EpisodeModel] | None = None


class SortingModel(BaseModel):
    value: str | None = None
    label: str | None = None
    description: str | None = None


class PreAvatarModel(BaseModel):
    preview: str | None = None
    thumbnail: str | None = None


class AvatarModel(PreAvatarModel):
    optimized: PreAvatarModel | None = None


class TorrentsStatsModel(BaseModel):
    passkey: str | None = None
    uploaded: int | None = None
    downloaded: int | None = None


class ReleaseEpisodeModel(EpisodeModel):
    release: ReleaseModel


class HistoryModel(BaseModel):
    id: int | None = None
    time: int | float | None = None
    user_id: int | None = None
    is_watched: bool | None = None
    updated_at: AwareDatetime | None = None
    release_episode_id: str | None = None
    release_episode: ReleaseEpisodeModel
