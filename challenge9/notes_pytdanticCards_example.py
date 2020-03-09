from pydantic import BaseModel
from pydantic import Field
import requests
import unittest
from typing import List, Optional, Set, Tuple, Union, Dict

class BaseResponse(BaseModel):
    error: Optional

class challenge9rson(unittest.TestCase):
    def test_json(self):
        url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
        response = requests.get(url)
        data = json.loads(response.text)
        print(data)

        print("deck_id type: {}".format(type(data["deck_id"])))
