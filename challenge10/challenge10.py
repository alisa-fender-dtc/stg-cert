import unittest
from copart_api.search.search_api import SearchAPI
from pydantic import ValidationError
from copart_api.search.input_spreadsheet import InputSpreadsheet

class challenge10(unittest.TestCase):

    def test_copart_search_api(self):
        search_input_file = 'search_input.xlsx'
        si = InputSpreadsheet(search_input_file)
        query_dict = si.query_dict
        # print(query_dict)
        
        for query_num in query_dict.keys():
            query = ""
            for field in query_dict[query_num].keys():
                if query_dict[query_num][field] == '':
                    pass
                else:
                    query = query + ' ' + str(query_dict[query_num][field])
            query = query.strip()

            try:
                print("Query: {}".format(query))
                api = SearchAPI()
                api.run_query(query)
                self.assertTrue(api.validate_query())
                api.log_response_text()
                print("Number of results returned: {}".format(api.get_total_elements()))
                del api
            except ValidationError as e:
                print("Exception: {}".format(e))
            except Exception as e:
                print("Exception: {}".format(e))




if __name__ == '__main__':
    unittest.main()
