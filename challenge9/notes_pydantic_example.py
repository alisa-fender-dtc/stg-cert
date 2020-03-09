from datetime import datetime
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []

class Admin(User):
    rights: List[str] = []


json = {
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"]


}


user = User(**json)
print(user.id)
print(user.name)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())


admin_json = {
    "name": "Matt",
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friends": [1],
    "rights": ["full", "read_only", "delete"]
}

admin = Admin(**admin_json)
print(admin.id)
print(admin.name)
print(repr(admin.signup_ts))
print(admin.friends)
print(admin.rights)
print(admin.dict())
