from pydantic import BaseModel, validator, Field

from typing import ClassVar, Dict, List, Optional, Literal

class Patch_Update(BaseModel):
    #names = "johns"
   # id: int
    name: Literal["olly"]
    job: Literal["coder"]
    #createdAt: str

