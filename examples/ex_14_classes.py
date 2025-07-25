# %% Basic classes
class Greeter:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}!"

# %% Class methods and class variables
class Counter:
    count: int = 0

    @classmethod
    def increment(cls) -> None:
        cls.count += 1

counter_1 = Counter()
counter_2 = Counter()
counter_1.increment()
counter_1.increment()
print(counter_2.count)

# %% ClassVar
from typing import ClassVar

class User:
    max_users: ClassVar[int] = 100

    def __init__(self, name: str):
        self.name = name

u = User('Monty')
print(u.max_users)

# %% Properties
class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.14 * self._radius ** 2


class Person:
    def greet(self) -> str:
        return "Hello!"

class Cowboy(Person):
    def greet(self) -> str:
        return "Howdy!"


#%% Generics
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# %% Forward references as strings
class Node:
    value: int
    next: 'Node'  # forward reference as a string

    def __init__(self, value: int, next: 'Node' = None):
        self.value = value
        self.next = next

# %% Forward references with future import
from __future__ import annotations

class Node2:
    value: int
    next: Node2  # works now

    def __init__(self, value: int, next: Node2 = None):
        self.value = value
        self.next = next

# %% Type and TypeVar
from typing import Type, TypeVar

TShape = TypeVar("TShape", bound="Shape")

class Shape:
    @classmethod
    def create(cls: Type[TShape]) -> "Shape":
        return cls()

class Square(Shape):
    sides = 4

square = Square.create()
print(square.sides)  # mypy: attr-defined

# %% Returning self or cls
from datetime import date
from typing import Type, TypeVar

TAnimal = TypeVar("TAnimal", bound="Animal")

class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls: Type[TAnimal], name: str) -> TAnimal:
        return cls(name, date.today())

    def twin(self: TAnimal, name: str) -> TAnimal:
        return type(self)(name, self.birthday)

class Cat(Animal):
    def meow(self) -> None:
        print(f"{self.name} says meow!")

fluffy = Cat.newborn("Fluffy")
ginger = fluffy.twin("Ginger")
fluffy.meow()
ginger.meow()

# %% Dataclasses
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# %%
from dataclasses import field
from typing import ClassVar

@dataclass
class BlogPost:
    title: str
    tags: list[str] = field(default_factory=list)  # avoids shared mutable default
    max_comments: ClassVar[int] = 30
