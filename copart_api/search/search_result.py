from pydantic import BaseModel
from copart_api.search.data import Data


class SearchResult(BaseModel):
    returnCode: int
    returnCodeDesc: str
    data: Data