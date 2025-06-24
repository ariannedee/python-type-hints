# Functions
def echo(text: str, times: int) -> str:
    return (text + '\n') * times

print(echo("Hello", 3.0))


def greet(name, shout: bool = False) -> str:
    if shout:
        return f"Hello, {name.upper()}!"
    return f"Hello, {name}."


# Variables
age: int = 30
active: bool
active = True


# Lists
from typing import List  # Can use built-in 'list' in 3.9+

user_ids: List[int] = [123, 456, 789]


# Classes
from dataclasses import dataclass

@dataclass  # Quick class creation feature for storing data (3.7+)
class User:
    id: int
    name: str
    active: bool

def deactivate(user: User):
    user.active = False

users: List[User] = [
    User(1, 'Monty', True),
    User(2, 'Guido', True),
]

for u in users:
    deactivate(u)
