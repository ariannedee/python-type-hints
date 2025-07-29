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
from typing import Protocol, Self, TypeVar

T = TypeVar("T", bound="Comparable")

class Comparable(Protocol):
    def __lt__(self: T, other: T) -> bool: ...

class Temperature(Comparable):
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    def __lt__(self, other: Self) -> bool:
        return self.celsius < other.celsius

    def __repr__(self) -> str:
        return f"{self.celsius}°C"

t1 = Temperature(30)
t2 = Temperature(20)
t3 = Temperature(21.5)

temps = [t1, t2, t3]
temps.sort()
assert temps == [t2, t3, t1]

U = TypeVar("U", bound=Comparable)

def min_value(x: U, y: U) -> U:  # Function that accepts comparables
    return x if x < y else y

assert min_value(t1, t2) == t2
