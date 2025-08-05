# %% Data validation
from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
    last_login: datetime

user = User(
    id="123",  # Casts '123' to int
    name="Guido",
    last_login ="2025-01-02T03:04:05",  # Casts to dt
)
print(user.id)          # 123
print(user.last_login)  # datetime object

# %% Error reporting
try:
    User(id='abc', name='Alice', last_login="2025-01-02T03:04:05")
except Exception as e:
    print(e)

# %% Nested models
class Address(BaseModel):
    city: str
    zip: str

class Person(BaseModel):
    name: str
    address: Address

p = Person(name="John", address={"city": "NY", "zip": "10001"})
print(p.address.city)  # NY

# %% More validation
from pydantic import (BaseModel, EmailStr, Field, ValidationError,
                      field_validator)
from typing import Annotated
import re

class Adult(BaseModel):
    name: str
    age: Annotated[int, Field(ge=18)]  # Must be greater than 18
    email: EmailStr

    @field_validator("name")
    @classmethod
    def name_cannot_have_numbers(cls, value: str) -> str:
        if re.search(r'\d', value):
            raise ValueError("Name cannot contain numbers")
        return value

user_data = {"name": "Monty3", "age": 15, "email": "@monty@python.com"}

try:
    user = Adult(**user_data)
    print(f"✅ Valid user: {user}")
except ValidationError as e:
    print(f"❌ Invalid user data for {user_data['name']}:")
    print(e)

# %% TypedDict validation
import sys

if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from pydantic import TypeAdapter, ValidationError

class UserDict(TypedDict):
    id: int
    name: str
    is_active: bool

user_adapter = TypeAdapter(UserDict)

user_from_dict: UserDict = {'id': 1, 'name': 'Monty', 'is_active': False}
try:
    user_adapter.validate_python(user_from_dict)
except ValidationError as e:
    print(repr(e))
