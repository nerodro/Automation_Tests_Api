from pydantic import BaseModel, validator, Field

from typing import ClassVar, Dict, List, Optional, Literal

class Put_Update(BaseModel):
    #names = "johns"
    id: int
    name: Literal["sam"]
    job: Literal["worker"]
    createdAt: str

