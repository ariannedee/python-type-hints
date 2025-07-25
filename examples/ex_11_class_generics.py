# %%
from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

# %%
from typing import Iterator

class Bag[T]:                         # Classes
    def __iter__(self) -> Iterator[T]:
        ...

    def add(self, arg: T) -> None:
        ...