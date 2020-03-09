from typing import List
from pydantic import BaseModel

class Query(BaseModel):
    query: List[str]=[]
    page: int
    size: int
    start: int
    watchListOnly: bool
    freeFormSearch: bool
    hideImages: bool
    defaultSort: bool
    specificRowProvided: bool