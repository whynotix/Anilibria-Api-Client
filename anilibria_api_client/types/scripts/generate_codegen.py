from __future__ import annotations

import ast
import copy
import json
import keyword
import re
import shutil
import sys
from pathlib import Path
from textwrap import dedent

from datamodel_code_generator import DataModelType, InputFileType, PythonVersion, generate # type: ignore


ROOT_DIR = Path(__file__).resolve().parents[3]
TYPES_DIR = ROOT_DIR / "anilibria_api_client" / "types"
SCHEMA_PATH = TYPES_DIR / "schema" / "anilibria-v1.openapi.json"
CODEGEN_DIR = TYPES_DIR / "codegen"
OPENAPI_MODELS_PATH = CODEGEN_DIR / "openapi_models.py"
METHODS_DIR = CODEGEN_DIR / "methods"
TEMP_DIR = TYPES_DIR / "schema" / ".tmp"

PUBLIC_ENUMS_PATH = TYPES_DIR / "__init__.py"
PUBLIC_MODELS_PATH = TYPES_DIR / "models.py"
PUBLIC_RESPONSES_PATH = TYPES_DIR / "responses.py"
PACKAGE_MODELS_SHIM = ROOT_DIR / "anilibria_api_client" / "models.py"
PACKAGE_RESPONSES_SHIM = ROOT_DIR / "anilibria_api_client" / "responses.py"
PACKAGE_RESPONSE_MODELS_SHIM = ROOT_DIR / "anilibria_api_client" / "response_models.py"

TITLE_OVERRIDES = {
    "enums.accounts.users.user.collection.type": "CollectionType",
    "enums.anime.releases.release.type": "ContentType",
    "enums.anime.releases.release.ageRating": "AgeRating",
    "enums.anime.releases.release.season": "Seasons",
    "enums.anime.catalog.filter.sorting": "SortType",
    "enums.anime.catalog.filter.publishStatus": "PublishStatusesType",
    "enums.anime.catalog.filter.productionStatus": "ProductionStatusesType",
    "enums.accounts.users.user.social.type": "UserSocialType",
    "enums.accounts.users.user.favorite.filter.sorting": "UserFavoriteFilterSorting",
    "enums.ads.banner.placement": "AdsBannerPlacement",
    "enums.ads.statistics.event.type": "AdsStatisticsEventType",
    "enums.anime.releases.release.member.role": "AnimeReleaseMemberRole",
    "enums.anime.releases.release.publishDay": "AnimeReleasePublishDay",
    "enums.anime.torrents.torrent.codec": "TorrentCodec",
    "enums.anime.torrents.torrent.color": "TorrentColor",
    "enums.anime.torrents.torrent.quality": "TorrentQuality",
    "enums.anime.torrents.torrent.type": "TorrentType",
    "enums.anime.torrents.torrentMember.role": "TorrentMemberRole",
    "enums.media.videos.video.origin.type": "VideoOriginType",
    "models.anime.releases.v1.release": "AnimeRelease",
    "models.anime.releases.v1.release.ageRating": "AnimeReleaseAgeRating",
    "models.anime.releases.v1.release.episode": "AnimeReleaseEpisode",
    "models.anime.releases.v1.release.episode.skip": "AnimeReleaseEpisodeSkip",
    "models.anime.releases.v1.release.member": "AnimeReleaseMember",
    "models.anime.releases.v1.release.member.role": "AnimeReleaseMemberRoleDetails",
    "models.anime.releases.v1.release.member.user": "AnimeReleaseMemberUser",
    "models.anime.releases.v1.release.name": "AnimeReleaseName",
    "models.anime.releases.v1.release.publishDay": "AnimeReleasePublishDayDetails",
    "models.anime.releases.v1.release.season": "AnimeReleaseSeasonDetails",
    "models.anime.releases.v1.release.type": "AnimeReleaseTypeDetails",
    "models.anime.franchises.v1.franchise.release": "AnimeFranchiseRelease",
    "models.anime.schedule.v1.releaseInSchedule": "AnimeReleaseInSchedule",
    "responses.api.v1.anime.catalog.releases": "AnimeCatalogReleasesResponse",
    "responses.api.v1.anime.genres.releases": "AnimeGenreReleasesResponse",
    "responses.api.v1.anime.releases.episode": "AnimeEpisodeResponse",
    "responses.api.v1.anime.releases.episode.timecode": "AnimeEpisodeTimecodeResponse",
    "responses.api.v1.anime.releases.latest": "AnimeLatestReleasesResponse",
    "responses.api.v1.anime.releases.list": "AnimeReleaseListResponse",
    "responses.api.v1.anime.releases.random": "AnimeRandomReleasesResponse",
    "responses.api.v1.anime.releases.recommended": "AnimeRecommendedReleasesResponse",
    "responses.api.v1.anime.releases.release": "AnimeReleaseResponse",
    "responses.api.v1.anime.releases.release.episodes.timecodes": "AnimeReleaseEpisodeTimecodesResponse",
    "responses.api.v1.anime.releases.release.members": "AnimeReleaseMembersResponse",
    "responses.api.v1.anime.torrents.releaseTorrents": "AnimeReleaseTorrentsResponse",
    "responses.api.v1.app.search.releases": "AppSearchReleasesResponse",
    "responses.api.v1.accounts.users.me.collections.ids": "UserCollectionIdsResponse",
    "responses.api.v1.accounts.users.me.collections.ids.item": "UserCollectionIdItem",
    "responses.api.v1.accounts.users.me.collections.references.ageRatings": "UserCollectionAgeRatingsResponse",
    "responses.api.v1.accounts.users.me.collections.references.genres": "UserCollectionGenresResponse",
    "responses.api.v1.accounts.users.me.collections.references.types": "UserCollectionTypesResponse",
    "responses.api.v1.accounts.users.me.collections.references.years": "UserCollectionYearsResponse",
    "responses.v1.accounts.users.collections.releases": "UserCollectionReleasesResponse",
    "responses.v1.accounts.users.me.collections.delete": "UserCollectionsDeleteResponse",
    "responses.v1.accounts.users.me.collections.update": "UserCollectionsUpdateResponse",
    "responses.v1.accounts.users.me.favorites.releases": "UserFavoriteReleasesResponse",
    "responses.v1.accounts.users.me.views.timecodes": "UserViewTimecodesResponse",
    "responses.v1.accounts.users.me.views.timecodes.item": "UserViewTimecode",
    "responses.v1.anime.franchises.byRelease": "AnimeFranchisesByReleaseResponse",
}

LEGACY_ENUM_NAMES = {
    "CollectionType",
    "ContentType",
    "AgeRating",
    "Seasons",
    "SortType",
    "PublishStatusesType",
    "ProductionStatusesType",
}
LEGACY_MODEL_NAMES = {"TimeCode", "Release", "ReleaseCollection"}
IGNORED_TOKENS = {"api", "commons", "enums", "http", "models", "responses", "schemas", "v1", "v2"}
TOKEN_PATTERN = re.compile(r"[^0-9A-Za-z]+")
SCHEMA_REF_PATTERN = re.compile(r"^#/components/schemas/(?P<name>.+)$")
PARAMETER_REF_PATTERN = re.compile(r"^#/components/parameters/(?P<name>.+)$")
GROUP_CONFIG = {
    "accounts": {"class_name": "GeneratedAccountsMethod", "path_prefix": "/accounts/"},
    "ads": {"class_name": "GeneratedAdsMethod", "path_prefix": "/media/"},
    "anime": {"class_name": "GeneratedAnimeMethod", "path_prefix": "/anime/"},
    "app": {"class_name": "GeneratedAppMethod", "path_prefix": "/app/"},
    "media": {"class_name": "GeneratedMediaMethod", "path_prefix": "/media/"},
    "teams": {"class_name": "GeneratedTeamsMethod", "path_prefix": "/teams/"},
}


def to_pascal_case(value: str) -> str:
    parts = [part for part in TOKEN_PATTERN.split(value) if part]
    if not parts:
        return "Model"
    words: list[str] = []
    for part in parts:
        if part.isupper():
            words.append(part.title())
        else:
            words.append(part[0].upper() + part[1:])
    return "".join(words)


def make_title(component_name: str, used_titles: set[str]) -> str:
    if component_name in TITLE_OVERRIDES:
        title = TITLE_OVERRIDES[component_name]
    else:
        tokens = [
            token
            for token in re.split(r"[._-]+", component_name)
            if token and token not in IGNORED_TOKENS
        ]
        title = "".join(to_pascal_case(token) for token in tokens) or "GeneratedModel"

    if title[0].isdigit():
        title = f"Model{title}"

    if title not in used_titles:
        used_titles.add(title)
        return title

    suffix_tokens = [token for token in re.split(r"[._-]+", component_name) if token]
    for size in range(1, len(suffix_tokens) + 1):
        candidate = title + "".join(to_pascal_case(token) for token in suffix_tokens[-size:])
        if candidate not in used_titles:
            used_titles.add(candidate)
            return candidate
    raise RuntimeError(f"Failed to build unique title for component: {component_name}")


def rewrite_refs(node: object, ref_map: dict[str, str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str) and value in ref_map:
                node[key] = ref_map[value]
            else:
                rewrite_refs(value, ref_map)
    elif isinstance(node, list):
        for item in node:
            rewrite_refs(item, ref_map)


def transform_schema(schema: dict) -> tuple[dict, dict[str, str]]:
    transformed = copy.deepcopy(schema)
    used_titles: set[str] = set()
    original_schemas = transformed.get("components", {}).get("schemas", {})
    renamed_schemas: dict[str, dict] = {}
    ref_map: dict[str, str] = {}
    title_map: dict[str, str] = {}
    for component_name, component_schema in original_schemas.items():
        title = make_title(component_name, used_titles)
        component_schema["title"] = title
        renamed_schemas[title] = component_schema
        source_ref = f"#/components/schemas/{component_name}"
        target_ref = f"#/components/schemas/{title}"
        ref_map[source_ref] = target_ref
        title_map[source_ref] = title

    transformed["components"]["schemas"] = renamed_schemas
    rewrite_refs(transformed, ref_map)
    return transformed, title_map


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_json(path: Path, payload: object) -> None:
    write_text(path, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def build_custom_header(path: Path) -> None:
    write_text(
        path,
        "\n".join(
            [
                "# This file was auto-generated by anilibria_api_client/types/scripts/generate_codegen.py.",
                "# DO NOT EDIT MANUALLY.",
            ]
        )
        + "\n",
    )


def run_codegen(transformed_schema_path: Path, header_path: Path) -> None:
    CODEGEN_DIR.mkdir(parents=True, exist_ok=True)
    generate(
        transformed_schema_path,
        input_filename=transformed_schema_path.name,
        input_file_type=InputFileType.OpenAPI,
        output=OPENAPI_MODELS_PATH,
        output_model_type=DataModelType.PydanticV2BaseModel,
        target_python_version=PythonVersion.PY_313,
        encoding="utf-8",
        disable_timestamp=True,
        use_title_as_name=True,
        snake_case_field=True,
        allow_population_by_field_name=True,
        use_standard_collections=True,
        use_union_operator=True,
        use_subclass_enum=True,
        reuse_model=True,
        disable_appending_item_suffix=True,
        custom_file_header_path=header_path,
        formatters=[],
    )


def expr_name(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return ""


def parse_generated_symbols() -> tuple[list[str], list[str]]:
    tree = ast.parse(OPENAPI_MODELS_PATH.read_text(encoding="utf-8"))
    model_names: list[str] = []
    enum_names: list[str] = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        base_names = {expr_name(base) for base in node.bases}
        if "Enum" in base_names:
            enum_names.append(node.name)
        elif "BaseModel" in base_names or "RootModel" in base_names:
            model_names.append(node.name)
    return sorted(model_names), sorted(enum_names)


def format_exports(names: list[str], indent: str = "    ") -> str:
    return ",\n".join(f'{indent}"{name}"' for name in names)


def write_public_files(model_names: list[str], enum_names: list[str]) -> None:
    generated_enum_exports = [name for name in enum_names if name not in LEGACY_ENUM_NAMES]
    generated_model_exports = [name for name in model_names if name not in LEGACY_MODEL_NAMES]
    enums_content = f'''"""Auto-generated public enum facade for AniLiberty OpenAPI.\n\nDO NOT EDIT MANUALLY.\n"""\n\nfrom __future__ import annotations\n\nfrom enum import Enum\n\nfrom .codegen import openapi_models as _generated\n\n_GENERATED_TYPE_EXPORTS = (\n{format_exports(generated_enum_exports)}\n)\n\nfor _name in _GENERATED_TYPE_EXPORTS:\n    globals()[_name] = getattr(_generated, _name)\n\n\nclass CollectionType(str, Enum):\n    PLANNED = "PLANNED"\n    WATCHED = "WATCHED"\n    WATCHING = "WATCHING"\n    POSTPONED = "POSTPONED"\n    ABANDONED = "ABANDONED"\n\n\nclass ContentType(str, Enum):\n    TV = "TV"\n    ONA = "ONA"\n    WEB = "WEB"\n    OVA = "OVA"\n    OAD = "OAD"\n    MOVIE = "MOVIE"\n    DORAMA = "DORAMA"\n    SPECIAL = "SPECIAL"\n\n\nclass AgeRating(str, Enum):\n    R0_PLUS = "R0_PLUS"\n    R6_PLUS = "R6_PLUS"\n    R12_PLUS = "R12_PLUS"\n    R16_PLUS = "R16_PLUS"\n    R18_PLUS = "R18_PLUS"\n\n\nclass Seasons(str, Enum):\n    WINTER = "winter"\n    SPRING = "spring"\n    SUMMER = "summer"\n    AUTUMN = "autumn"\n\n\nclass SortType(str, Enum):\n    FRESH_AT_DESC = "FRESH_AT_DESC"\n    FRESH_AT_ASC = "FRESH_AT_ASC"\n    RATING_DESC = "RATING_DESC"\n    RATING_ASC = "RATING_ASC"\n    YEAR_DESC = "YEAR_DESC"\n    YEAR_ASC = "YEAR_ASC"\n\n\nclass PublishStatusesType(str, Enum):\n    IS_ONGOING = "IS_ONGOING"\n    IS_NOT_ONGOING = "IS_NOT_ONGOING"\n\n\nclass ProductionStatusesType(str, Enum):\n    IS_IN_PRODUCTION = "IS_IN_PRODUCTION"\n    IS_NOT_IN_PRODUCTION = "IS_NOT_IN_PRODUCTION"\n\n\n__all__ = [\n    "CollectionType",\n    "ContentType",\n    "AgeRating",\n    "Seasons",\n    "SortType",\n    "PublishStatusesType",\n    "ProductionStatusesType",\n    *_GENERATED_TYPE_EXPORTS,\n]\n'''
    models_content = '''"""Auto-generated public input model facade for AniLiberty OpenAPI.\n\nDO NOT EDIT MANUALLY.\n"""\n\nfrom __future__ import annotations\n\nfrom pydantic import BaseModel, ConfigDict\n\nfrom . import (\n    AgeRating,\n    CollectionType,\n    ContentType,\n    ProductionStatusesType,\n    PublishStatusesType,\n    Seasons,\n    SortType,\n)\n\n\nclass TimeCode(BaseModel):\n    """Legacy request DTO for accounts.users_me_views_timecodes_update."""\n\n    model_config = ConfigDict(populate_by_name=True, extra="ignore")\n\n    time: int\n    is_watched: bool\n    release_episode_id: str\n\n\nclass Release(BaseModel):\n    """Legacy request DTO for anime.catalog_releases_get and anime.catalog_releases_post."""\n\n    model_config = ConfigDict(populate_by_name=True, extra="ignore")\n\n    page: int | None = None\n    limit: int | None = None\n    genres: str | None = None\n    types: list[ContentType] | None = None\n    seasons: list[Seasons] | None = None\n    from_year: int | None = None\n    to_year: int | None = None\n    search: str | None = None\n    sorting: SortType | None = None\n    age_ratings: list[AgeRating] | None = None\n    publish_statuses: list[PublishStatusesType] | None = None\n    production_statuses: list[ProductionStatusesType] | None = None\n    include: str | None = None\n    exclude: str | None = None\n\n\nclass ReleaseCollection(BaseModel):\n    """Legacy request DTO for accounts.users_me_collections_releases_get and post."""\n\n    model_config = ConfigDict(populate_by_name=True, extra="ignore")\n\n    type_of_collection: CollectionType\n    page: int | None = None\n    limit: int | None = None\n    genres: str | None = None\n    types: list[ContentType] | None = None\n    years: str | None = None\n    search: str | None = None\n    age_ratings: list[AgeRating] | None = None\n    include: str | None = None\n    exclude: str | None = None\n\n\n__all__ = [\n    "TimeCode",\n    "Release",\n    "ReleaseCollection",\n]\n'''
    responses_content = f'''"""Auto-generated public response model facade for AniLiberty OpenAPI.\n\nDO NOT EDIT MANUALLY.\n"""\n\nfrom __future__ import annotations\n\nfrom .codegen import openapi_models as _generated\n\n_GENERATED_RESPONSE_EXPORTS = (\n{format_exports(generated_model_exports)}\n)\n\nfor _name in _GENERATED_RESPONSE_EXPORTS:\n    globals()[_name] = getattr(_generated, _name)\n\n\n__all__ = list(_GENERATED_RESPONSE_EXPORTS)\n'''
    write_text(PUBLIC_ENUMS_PATH, enums_content)
    write_text(PUBLIC_MODELS_PATH, models_content)
    write_text(PUBLIC_RESPONSES_PATH, responses_content)
    write_text(PACKAGE_MODELS_SHIM, '"""Compatibility shim for public input models."""\n\nfrom .types.models import *\n')
    write_text(PACKAGE_RESPONSES_SHIM, '"""Compatibility shim for public response models."""\n\nfrom .types.responses import *\n')
    write_text(PACKAGE_RESPONSE_MODELS_SHIM, '"""Compatibility shim for public response models."""\n\nfrom .types.responses import *\n')


def sanitize_identifier(name: str) -> str:
    result = re.sub(r"[^0-9A-Za-z_]", "_", name)
    if result and result[0].isdigit():
        result = f"field_{result}"
    if keyword.iskeyword(result):
        result += "_"
    return result


def map_group(path: str) -> str:
    if path in {"/media/vasts", "/media/manifest.xml"}:
        return "ads"
    if path.startswith("/accounts/"):
        return "accounts"
    if path.startswith("/anime/"):
        return "anime"
    if path.startswith("/app/"):
        return "app"
    if path.startswith("/teams/"):
        return "teams"
    if path.startswith("/media/"):
        return "media"
    raise RuntimeError(f"Unsupported path group for {path}")


def method_name_for(path: str, http_method: str, path_operations: dict) -> str:
    special_names = {
        ("/media/vasts", "get"): "vasts",
        ("/media/manifest.xml", "get"): "vasts_manifest_xml",
        ("/teams/", "get"): "get",
    }
    if (path, http_method) in special_names:
        return special_names[(path, http_method)]

    group = map_group(path)
    raw_path = path.strip("/")
    segments = raw_path.split("/")
    if group in {"accounts", "anime", "app", "teams", "media", "ads"}:
        if segments:
            segments = segments[1:]
    tokens: list[str] = []
    for segment in segments:
        if segment.startswith("{") and segment.endswith("}"):
            tokens.append(segment[1:-1])
        else:
            tokens.extend([part for part in re.split(r"[-./]", segment) if part])
    base_name = "_".join(tokens) or "get"
    non_x_methods = [name for name in path_operations if not name.startswith("x-")]
    if len(non_x_methods) > 1 and base_name not in {"otp_get"}:
        base_name = f"{base_name}_{http_method}"
    return sanitize_identifier(base_name)


def resolve_ref_title(ref: str, title_map: dict[str, str]) -> str:
    return title_map.get(ref, "Any")


def schema_to_type_hint(schema: dict | None, title_map: dict[str, str], required: bool = True) -> str:
    if not schema:
        result = "Any"
    elif "$ref" in schema:
        result = resolve_ref_title(schema["$ref"], title_map)
    elif "anyOf" in schema:
        parts = [schema_to_type_hint(part, title_map, required=True) for part in schema["anyOf"]]
        result = " | ".join(sorted(set(parts)))
    elif "oneOf" in schema:
        parts = [schema_to_type_hint(part, title_map, required=True) for part in schema["oneOf"]]
        result = " | ".join(sorted(set(parts)))
    elif schema.get("type") == "array":
        result = f"list[{schema_to_type_hint(schema.get('items'), title_map, required=True)}]"
    elif schema.get("type") == "integer":
        result = "int"
    elif schema.get("type") == "number":
        result = "float"
    elif schema.get("type") == "boolean":
        result = "bool"
    elif schema.get("type") == "string":
        result = "str"
    elif schema.get("type") == "object":
        result = "dict[str, Any]"
    else:
        result = "Any"

    nullable = schema.get("nullable", False) if schema else False
    if not required or nullable:
        return f"{result} | None"
    return result


def build_request_body_parameters(operation: dict, title_map: dict[str, str]) -> tuple[list[dict[str, str]], list[str], str | None, bool]:
    request_body = operation.get("requestBody")
    if not request_body:
        return [], [], None, False

    content = request_body.get("content", {})
    json_schema = None
    for media_type in ("application/json", "application/xml", "application/x-www-form-urlencoded"):
        if media_type in content:
            json_schema = content[media_type].get("schema")
            break
    if not json_schema:
        return [], [], None, False

    if "$ref" in json_schema or json_schema.get("type") in {"array", "object"} and "properties" not in json_schema:
        return (
            [{"name": "body", "annotation": schema_to_type_hint(json_schema, title_map, required=True), "default": "", "required": True}],
            [],
            "json_data=body",
            True,
        )

    required_fields = set(json_schema.get("required", []))
    params: list[dict[str, str]] = []
    body_lines: list[str] = []
    for property_name, property_schema in json_schema.get("properties", {}).items():
        param_name = sanitize_identifier(property_name)
        annotation = schema_to_type_hint(property_schema, title_map, required=property_name in required_fields)
        default = "" if property_name in required_fields else " = None"
        params.append({"name": param_name, "annotation": annotation, "default": default, "required": property_name in required_fields})
        body_lines.append(f'        "{property_name}": {param_name},')

    if not params:
        return [], [], None, False
    return params, body_lines, "json_data=json_data", False


def resolve_parameter(parameter: dict, transformed_schema: dict) -> dict:
    if "$ref" not in parameter:
        return parameter
    match = PARAMETER_REF_PATTERN.match(parameter["$ref"])
    if not match:
        return parameter
    return transformed_schema["components"]["parameters"][match.group("name")]


def build_parameters(operation: dict, transformed_schema: dict, title_map: dict[str, str]) -> tuple[list[dict[str, str]], list[str], list[str]]:
    parameters: list[dict[str, str]] = []
    query_lines: list[str] = []
    path_assignments: list[str] = []
    for parameter in operation.get("parameters", []):
        parameter = resolve_parameter(parameter, transformed_schema)
        original_name = parameter["name"]
        param_name = sanitize_identifier(original_name)
        annotation = schema_to_type_hint(parameter.get("schema"), title_map, required=parameter.get("required", False))
        default = "" if parameter.get("required", False) else " = None"
        parameters.append({"name": param_name, "annotation": annotation, "default": default, "required": parameter.get("required", False)})
        if parameter.get("in") == "query":
            query_lines.append(f'        "{original_name}": {param_name},')
        elif parameter.get("in") == "path":
            path_assignments.append(f"{original_name}={param_name}")
    return parameters, query_lines, path_assignments


def render_method(path: str, http_method: str, operation: dict, transformed_schema: dict, title_map: dict[str, str], path_operations: dict) -> str:
    method_name = method_name_for(path, http_method, path_operations)
    parameters, query_lines, path_assignments = build_parameters(operation, transformed_schema, title_map)
    body_parameters, body_lines, request_argument, raw_body_argument = build_request_body_parameters(operation, title_map)
    all_parameters = parameters + body_parameters
    ordered_parameters = sorted(all_parameters, key=lambda item: (not item["required"], item["name"]))
    signature_params = ["self"]
    signature_params.extend(
        f"{parameter['name']}: {parameter['annotation']}{parameter['default']}" for parameter in ordered_parameters
    )

    lines = [f"    async def {method_name}(", "            " + ",\n            ".join(signature_params), "    ) -> Any:"]
    summary = operation.get("summary") or method_name
    description = operation.get("description") or summary
    lines.append(f'        """{summary}\n\n        {description}\n        """')

    if path_assignments:
        path_args = ", ".join(path_assignments)
        lines.append(f'        endpoint = self._api.build_endpoint_with_params("{path}", {path_args})')
    else:
        lines.append(f'        endpoint = "{path}"')

    if query_lines:
        lines.append("        params = {")
        lines.extend(query_lines)
        lines.append("        }")
    else:
        lines.append("        params = None")

    if raw_body_argument:
        pass
    elif body_lines:
        lines.append("        json_data = {")
        lines.extend(body_lines)
        lines.append("        }")
    else:
        lines.append("        json_data = None")

    api_method = http_method.lower()
    call_arguments = ["endpoint"]
    if api_method == "get":
        call_arguments.append("params=params")
    else:
        if query_lines:
            call_arguments.append("params=params")
        if request_argument:
            call_arguments.append(request_argument)
        elif body_lines:
            call_arguments.append("json_data=json_data")
    lines.append(f"        return await self._api.{api_method}({', '.join(call_arguments)})")
    return "\n".join(lines)


def write_generated_methods(transformed_schema: dict, title_map: dict[str, str]) -> None:
    METHODS_DIR.mkdir(parents=True, exist_ok=True)
    grouped_methods: dict[str, list[str]] = {group: [] for group in GROUP_CONFIG}
    for path, path_operations in sorted(transformed_schema["paths"].items()):
        group = map_group(path)
        for http_method, operation in path_operations.items():
            if http_method.startswith("x-"):
                continue
            grouped_methods[group].append(render_method(path, http_method, operation, transformed_schema, title_map, path_operations))

    write_text(
        METHODS_DIR / "__init__.py",
        "\n".join(
            [
                '"""Generated AniLiberty method groups."""',
                "",
                "from .accounts import GeneratedAccountsMethod",
                "from .ads import GeneratedAdsMethod",
                "from .anime import GeneratedAnimeMethod",
                "from .app import GeneratedAppMethod",
                "from .media import GeneratedMediaMethod",
                "from .teams import GeneratedTeamsMethod",
                "",
                "__all__ = [",
                '    "GeneratedAccountsMethod",',
                '    "GeneratedAdsMethod",',
                '    "GeneratedAnimeMethod",',
                '    "GeneratedAppMethod",',
                '    "GeneratedMediaMethod",',
                '    "GeneratedTeamsMethod",',
                "]",
            ]
        )
        + "\n",
    )

    for group, config in GROUP_CONFIG.items():
        content = [
            '"""Auto-generated AniLiberty methods."""',
            "",
            "from __future__ import annotations",
            "",
            "from typing import Any",
            "",
            "from ....methods._libria import BaseMethod",
            "",
            "",
            f"class {config['class_name']}(BaseMethod):",
        ]
        if grouped_methods[group]:
            content.append("\n\n".join(grouped_methods[group]))
        else:
            content.append("    pass")
        write_text(METHODS_DIR / f"{group}.py", "\n".join(content) + "\n")


def main() -> int:
    if not SCHEMA_PATH.exists():
        print(f"OpenAPI schema not found: {SCHEMA_PATH}", file=sys.stderr)
        return 1

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    transformed, title_map = transform_schema(schema)

    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    try:
        transformed_schema_path = TEMP_DIR / "openapi-transformed.json"
        header_path = TEMP_DIR / "header.txt"
        write_json(transformed_schema_path, transformed)
        build_custom_header(header_path)
        run_codegen(transformed_schema_path, header_path)
    finally:
        if TEMP_DIR.exists():
            shutil.rmtree(TEMP_DIR, ignore_errors=True)

    model_names, enum_names = parse_generated_symbols()
    write_public_files(model_names, enum_names)
    write_generated_methods(transformed, title_map)
    print(f"Generated code in {CODEGEN_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
