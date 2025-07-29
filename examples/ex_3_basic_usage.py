# %% Functions
def echo(text: str, times: int) -> str:
    return (text + '\n') * times

print(echo("Hello", 3))


def greet(name: str, shout: bool = False) -> str:
    if shout:
        return f"Hello, {name.upper()}!"
    return f"Hello, {name}."

# %% Variables
age: int = 30
active: bool
active = True

# %% Lists
items: list = [1, 2.0, False, None, ['list']]
user_ids: list[int] = [123, 456, 789]
mapping: dict[str, int] = {'a': 1, 'b': 2}

# %% Classes
from dataclasses import dataclass

@dataclass  # Quick class creation feature for storing data (3.7+)
class User:
    id: int
    name: str
    active: bool

def deactivate(user: User) -> None:
    user.active = False

users: list[User] = [
    User(1, 'Monty', True),
    User(2, 'Guido', True),
]

for u in users:
    deactivate(u)
