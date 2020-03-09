import requests
import unittest
from pandas.io.json import json_normalize



class challenge9rson(unittest.TestCase):
    def test_json(self):
        url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
        response = requests.get(url)
        flat = json_normalize(response.json())
        print(flat)

if __name__ == '__main__':
    unittest.main()
