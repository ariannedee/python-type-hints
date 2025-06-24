from __future__ import annotations  # Use in < 3.9 to support built-in generics, e.g. list[int]

from typing import List

numbers_1: List[int] = [1, 2, 3, 4]  # Must use List in < 3.9

numbers_2: list[int] = [1, 2, 3, 4]  # Can use list in 3.9+


# Lists
from typing import Any
from ex_3_basic_usage import User

grocery_list: list[str] = ["Spaghetti", "Eggs", "Garlic"]
users: list[User] = [User(1, "Monty", True)]  # Custom class
truthy: list = [1, 1.0, True, '1']  # Any type
falsy: list[Any] = [0, 0.0, False, '']  # Any type
numbers: list[int | float] = [1, 2.5, 3, 4.0]  # Multiple types


# Dictionaries
from typing import TypedDict

letter_counts: dict[str, int] = {"a": 3, "b": 1, "n": 2}

class UserDict(TypedDict):
    id: int
    name: str
    is_active: bool

more_users: list[UserDict] = [
    {'id': 1, 'name': 'Monty', 'is_active': False},
    {'id': 2, 'name': 'Guido', 'is_active': True},
]

class PartialUser(TypedDict, total=False):
    id: int
    name: str
    is_active: bool

from typing import TypedDict, NotRequired

class FlexibleUser(TypedDict):
    id: int
    name: NotRequired[str]
    is_active: bool


# Tuples
x: tuple[int] = (1,)

y: tuple[int, float] = (1, 2.3)

z: tuple[list[int], dict[str, float], tuple[bool]]
z = ([1, 2], {'pi': 3.14}, (True,))

letters: tuple[str, ...] = ('a', 'b', 'c')  # Any number of arguments

a_tuple: tuple  # Equivalent to tuple[Any, ...]

empty_tuple: tuple[()] = ()


# Sets
primes: set[int] = {2, 3, 5, 7, 11}
