from typing import List
from pydantic import BaseModel
import copart_api.search.vehicle


class Results(BaseModel):
    totalElements: int
    content: List[copart_api.search.vehicle.Vehicle]=[]
    realTime: bool
    #TODO: spellCheckList and suggestions coming as null. Find way to check. Optional? Field?
    #TODO: facetFields
