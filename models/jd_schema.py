from pydantic import BaseModel
from typing import List

class JD(BaseModel):
    role: str
    skills: List[str]
    experience: str
    location: str
    education: str