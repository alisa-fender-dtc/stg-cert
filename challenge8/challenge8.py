import unittest
from copart_api.search.search_api import SearchAPI
from pydantic import ValidationError

class challenge8(unittest.TestCase):

    def test_copart_search_api(self):
        queries = ['toyota camry', 'honda accord', 'nissan skyline', 'batm0bile', 'SUBARU']
        # queries = ['toyota camry']

        for query in queries:
            try:
                print("Query: {}".format(query))
                api = SearchAPI()
                api.run_query(query)
                self.assertEqual(api.response.status_code, 200)
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
