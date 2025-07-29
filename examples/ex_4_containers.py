# %% Import from typing vs built-in generics
from __future__ import annotations  # Use in < 3.9 to support built-in generics, e.g. list[int]

from typing import List

numbers_1: List[int] = [1, 2, 3, 4]  # Use typing.List in < 3.9 unless you import annotations from __future__

numbers_2: list[int] = [1, 2, 3, 4]  # Use list in 3.9+, or if you import annotations from __future__

# %% Lists
from typing import Any
from ex_3_basic_usage import User

grocery_list: list[str] = ["Spaghetti", "Eggs", "Garlic"]
users: list[User] = [User(1, "Monty", True)]  # Custom class
truthy: list = [1, 1.0, True, '1']  # Any type
falsy: list[Any] = [0, 0.0, False, '']  # Any type
numbers: list[int | float] = [1, 2.5, 3, 4.0]  # Multiple types

# %% Dictionaries
letter_counts: dict[str, int] = {"a": 3, "b": 1, "n": 2}
many: dict[str, int | str | None] = {"a": 1, "b": '2', "c": None}

# %% TypedDict for specifying dict structure
from typing import TypedDict

class UserDict(TypedDict):
    id: int
    name: str
    is_active: bool

more_users: list[UserDict] = [
    {'id': 1, 'name': 'Monty', 'is_active': False},
    {'id': 2, 'name': 'Guido', 'is_active': True},
]
print(more_users[0]["name"].capitalize())

# %% TypedDict - All keys are optional`
class Location(TypedDict, total=False):
    latitude: float
    longitude: float
    name: str

locations: list[Location] = [
    {'latitude': 33.958, 'longitude': -83.368, 'name': 'Athens'},
    {'latitude': 42.986, 'longitude': -81.251},
    {'name': 'Paris'},
]

# %% TypedDict - Specific keys are optional
import sys

if sys.version_info >= (3, 11):
    from typing import TypedDict, NotRequired  # 3.11+

    class Point(TypedDict):
        x: int
        y: int
        z: NotRequired[int]

# %% Tuples
x: tuple[int] = (1,)

y: tuple[int, float] = (1, 2.3)

z: tuple[list[int], dict[str, float], tuple[bool]]
z = ([1, 2], {'pi': 3.14}, (True,))

letters: tuple[str, ...] = ('a', 'b', 'c')  # Any number of str arguments

a_tuple: tuple  # Equivalent to tuple[Any, ...]

empty_tuple: tuple[()] = ()

# %% Sets
primes: set[int] = {2, 3, 5, 7, 11}
