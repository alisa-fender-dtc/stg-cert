from copart_api.search.search_result import SearchResult
from copart_api.search.search_request import SearchRequest
from common.slingqa_utils import utils
import requests
import json
import sys

class SearchAPI():
    def __init__(self):
        self.request = None
        self.result = None
        self.query = None
        self.response = None
        self.utils = utils()

    def run_query(self, query):
        self.query = query
        self.request = SearchRequest(self.query)
        self.response = requests.post(self.request.url, headers=self.request.get_headers(), data=self.request.get_form_data())
        self.result = SearchResult(**self.response.json())

    def validate_query(self):
        ret_val = False
        if self.query in self.result.data.query.query[0]:
            ret_val = True
        else:
            print("Query {} does not match received {}".format(self.query, self.result.data.query.query[0]))

        return ret_val

    def log_response_text(self):
        # print("Response Text: {}".format(self.response.text))
        self.utils.dump_to_text_file(self.response.text, sys._getframe(1).f_code.co_name)

    def get_total_elements(self):
        try:
            return self.result.data.results.totalElements
        except:
            return None




