from fastapi import FastAPI

from community_management import __version__
from community_management.user.controller import user_router
from community_management.community.controller import community_router

app = FastAPI(title="Social Media", version=__version__)
app.include_router(router=user_router, tags=["user-controller"])
app.include_router(router=community_router, tags=["community-controller"])
