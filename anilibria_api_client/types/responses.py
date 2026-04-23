"""Auto-generated public response model facade for AniLiberty OpenAPI.

DO NOT EDIT MANUALLY.
"""

from __future__ import annotations

from .codegen import openapi_models as _generated

_GENERATED_RESPONSE_EXPORTS = (
    "AccountsOtpGet",
    "AccountsOtpLogin",
    "AccountsOtpOtp",
    "AccountsUsersAuthLogin",
    "AccountsUsersAuthLogout",
    "AccountsUsersAuthSocialAuthenticate",
    "AccountsUsersAuthSocialLogin",
    "AccountsUsersMeFavoritesReferencesAgeRating",
    "AccountsUsersMeFavoritesReferencesGenre",
    "AccountsUsersMeFavoritesReferencesSorting1",
    "AccountsUsersMeFavoritesReferencesType",
    "AccountsUsersMeViewsHistory",
    "AccountsUsersUserView",
    "AdsBannersBanner",
    "AdsVastsVast",
    "AnimeCatalogReferencesAgeRating",
    "AnimeCatalogReferencesGenre",
    "AnimeCatalogReferencesProductionStatus",
    "AnimeCatalogReferencesPublishStatus",
    "AnimeCatalogReferencesSeason",
    "AnimeCatalogReferencesSorting1",
    "AnimeCatalogReferencesType",
    "AnimeCatalogReleasesResponse",
    "AnimeFranchiseRelease",
    "AnimeFranchisesFranchise",
    "AnimeGenreReleasesResponse",
    "AnimeGenresGenre",
    "AnimeRelease",
    "AnimeReleaseAgeRating",
    "AnimeReleaseEpisode",
    "AnimeReleaseEpisodeSkip",
    "AnimeReleaseInSchedule",
    "AnimeReleaseListResponse",
    "AnimeReleaseMember",
    "AnimeReleaseMemberRoleDetails",
    "AnimeReleaseMemberUser",
    "AnimeReleaseName",
    "AnimeReleasePublishDayDetails",
    "AnimeReleaseSeasonDetails",
    "AnimeReleaseTypeDetails",
    "AnimeScheduleNow",
    "AnimeScheduleWeek",
    "AnimeSponsorsSponsor",
    "AnimeTorrents",
    "AnimeTorrentsTorrent",
    "AnimeTorrentsTorrentCodec",
    "AnimeTorrentsTorrentColor",
    "AnimeTorrentsTorrentMember",
    "AnimeTorrentsTorrentMemberRole",
    "AnimeTorrentsTorrentQuality",
    "AnimeTorrentsTorrentType",
    "AppStatus",
    "Browser",
    "ComponentsImage",
    "Device",
    "Links",
    "Location",
    "MediaPromotions",
    "MediaPromotionsPromotion",
    "MediaVideos",
    "MediaVideosVideoContent",
    "MediaVideosVideoOrigin",
    "Pagination",
    "Request",
    "TeamsTeam",
    "TeamsTeamRole",
    "TeamsTeamUser",
    "TeamsTeamUserAccount",
    "Torrents",
    "UserCollectionAgeRatingsResponse1",
    "UserCollectionReleasesResponse",
    "UserCollectionTypesResponse1",
    "UsersUser",
    "UsersUserSession",
    "UtilsPaginationSchemesMeta"
)

for _name in _GENERATED_RESPONSE_EXPORTS:
    globals()[_name] = getattr(_generated, _name)


__all__ = list(_GENERATED_RESPONSE_EXPORTS)
