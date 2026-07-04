from pydantic import BaseModel
from typing import List, Optional


class ResumeModel(BaseModel):
    name: str
    skills: List[str]
    experience: str
    projects: Optional[List[str]] = []
    education: Optional[str] = None
    raw_text: str