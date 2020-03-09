import json
import requests
import unittest

class challenge9rson(unittest.TestCase):
    def test_json(self):
        url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
        response = requests.get(url)
        data = json.loads(response.text)
        print(data)

        print("deck_id type: {}".format(type(data["deck_id"])))
