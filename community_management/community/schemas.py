from pydantic import BaseModel, Field
from community_management.community.constants import TopicKind
from datetime import datetime


class CommunityInputModel(BaseModel):
    name: str = Field(min_length=3, max_length=255, examples=[])
    topic: TopicKind = Field(examples=[TopicKind.MOVIES])
    owner_username: str = Field(min_length=3, max_length=255, examples=["John Doe"])
    adult_only: bool = False


class CommunityModel(CommunityInputModel):
    id: int = Field(ge=1)
    created_at: datetime
