
from pydantic import AwareDatetime, ConfigDict
from pydantic import BaseModel as PreBaseModel

from anilibria_api_client.models.models import *


class BaseModel(PreBaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class OtpGetResponse(BaseModel):
    otp: OtpModel | None = None
    remaining_time: float | int | None = None


class OtpLoginResponse(BaseModel):
    token: str | None = None


class UsersAuthLoginResponse(BaseModel):
    token: str | None = None


class UsersAuthLogoutResponse(BaseModel):
    token: str | None = None


class UsersAuthSocialProviderLoginResponse(BaseModel):
    url: str | None = None
    state: str | None = None


class UsersAuthSocialAuthenticateResponse(BaseModel):
    token: str | None = None


class UsersMeCollectionsReferencesAgeRatingsResponse(BaseModel):
    age_ratings: list[AgeRatingsModel] | None = None


class UsersMeCollectionsReferencesTypesResponse(BaseModel):
    types: list[TypesModel] | None = None


class UsersMeCollectionsReferencesYearsResponse(BaseModel):
    years: list[int] | None = None


class UsersMeCollectionsIdsResponse(BaseModel):
    data: list[tuple[int, str]] | None = None


class UsersMeCollectionsReferencesGenresResponse(BaseModel):
    genres: list[GenresModel] | None = None


class UsersMeCollectionsReleasesResponse(MetaModel):
    data: list[ReleaseModel] | None = None


class UsersMeCollectionsResponse(BaseModel):
    data: list[tuple[int, str]] | None = None


class UsersMeFavoritesReferencesAgeRatingsResponse(BaseModel):
    data: list[AgeRatingsModel] | None = None


class UsersMeFavoritesReferencesGenresResponse(BaseModel):
    data: list[GenresModel] | None = None


class UsersMeFavoritesReferencesSortingResponse(BaseModel):
    data: list[SortingModel] | None = None


class UsersMeFavoritesReferencesTypesResponse(BaseModel):
    data: list[TypesModel] | None = None


class UsersMeFavoritesReferencesYearsResponse(BaseModel):
    years: list[int] | None = None


class UsersMeFavoritesIdsResponse(BaseModel):
    ids: list[int] | None = None


class UsersMeFavoritesReleasesResponse(MetaModel):
    data: list[ReleaseModel] | None = None


class UsersMeFavoritesResponse(MetaModel):
    data: list[int] | None = None


class UsersMeProfileResponse(BaseModel):
    id: int | None = None
    login: str | None = None
    email: str | None = None
    nickname: str | None = None
    avatar: AvatarModel | None = None
    torrents: TorrentsStatsModel | None = None
    is_banned: bool | None = None
    create_at: AwareDatetime | None = None
    is_with_ads: bool | None = None


class UsersMeViewsHistoryResponse(MetaModel):
    data: list[HistoryModel]


class UsersMeViewsTimecodesResponse(BaseModel):
    data: list[list[str | int | bool]] | None = None

    def get_episode_timecodes(self) -> list[dict]:
        """Вывод в удобном формате"""
        return [
            {
                "episode_id": item[0],
                "time_seconds": float(item[1]),
                "is_watched": bool(item[2]),
            }
            for item in self.data
        ]
