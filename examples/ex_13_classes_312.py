#%% Generics
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# %% Returning self and class problems
from typing import Self  # Added in 3.11

class Shape:
    @classmethod
    def create(cls) -> Self:
        return cls()

class Square(Shape):
    sides = 4

square = Square.create()
print(square.sides)

# %% Returning self or cls
from datetime import date
from typing import Type, Self

class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls: Type[Self], name: str) -> Self:
        return cls(name, date.today())

    def twin(self: Self, name: str) -> Self:
        return type(self)(name, self.birthday)

class Cat(Animal):
    def meow(self) -> None:
        print(f"{self.name} says meow!")

fluffy = Cat.newborn("Fluffy")
ginger = fluffy.twin("Ginger")
fluffy.meow()
ginger.meow()
