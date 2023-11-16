from enum import Enum


class TopicKind(str, Enum):
    FUN = "fun"
    MOVIES = "movies"
    SCIENCE = "science"
    SPORTS = "sports"