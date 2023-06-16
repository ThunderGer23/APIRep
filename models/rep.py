from typing import List
from pydantic import BaseModel

class File(BaseModel):
    id: List[str]