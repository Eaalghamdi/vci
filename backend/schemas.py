from datetime import date
from pydantic import BaseModel


class ProjectRequest(BaseModel):
    ProjectTitle: str
    VideoTitle: str
    VideoPath: str