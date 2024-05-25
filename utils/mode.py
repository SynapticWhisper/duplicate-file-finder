from enum import Enum


class Mode(str, Enum):
    EASY = "search_by_filename"
    MEDIUM = "search_by_md5_hash"
    HARD = "search_by_sha256_hash"
