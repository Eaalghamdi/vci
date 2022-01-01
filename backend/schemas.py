from datetime import date
from pydantic import BaseModel


class ProjectRequest(BaseModel):
    ProjectTitle: str
    VideoPath: str
    VideoTitle: str