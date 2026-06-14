from typing import Literal

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["ok"]
    version: str


class VersionResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    version: str
    environment: str
    api_prefix: str
