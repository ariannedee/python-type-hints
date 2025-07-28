# %% Covariant
from typing import Protocol, TypeVar

T_co = TypeVar("T_co", covariant=True)

class Producer(Protocol[T_co]):
    def produce(self) -> T_co: ...

# %% Contravariant
from typing import Protocol, TypeVar

T_contra = TypeVar("T_contra", contravariant=True)

class Consumer(Protocol[T_contra]):
    def consume(self, item: T_contra) -> None: ...
