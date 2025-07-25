# %% Object has a name attribute
from typing import Protocol

class Named(Protocol):
    name: str

def greet(entity: Named) -> None:
    print(f"Hello {entity.name}")

# %% Object supports read and write methods
from typing import Protocol

class FileLike(Protocol):
    def read(self) -> str: ...
    def write(self, s: str) -> None: ...

# %% Objects can be compared to each other (so can be sorted)
from typing import Protocol, TypeVar

T = TypeVar("T", bound="Comparable")

class Comparable(Protocol):
    def __lt__(self: T, other: T) -> bool: ...