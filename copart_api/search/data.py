from pydantic import BaseModel
import copart_api.search.query
import copart_api.search.results

class Data(BaseModel):
    query: copart_api.search.query.Query
    results: copart_api.search.results.Results