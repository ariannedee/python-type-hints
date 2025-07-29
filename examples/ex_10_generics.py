# %% TypeVar for functions
from typing import TypeVar

T = TypeVar("T")

def first(sequence: list[T]) -> T:
    return sequence[0]

print(first([1, 2, 3]))
print(first(['a', 'b', 'c']))
print(first([1, 'a']))  # Works because T is object

# %% Bounded TypeVar
from typing import TypeVar

class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

A = TypeVar("A", bound=Animal)

def speak(animal: A) -> None:  # Type must be an Animal, Dog is okay
    animal.speak()

speak(Dog())  # Okay

# %% Constrained TypeVar
from typing import TypeVar

NumberOrStr = TypeVar("NumberOrStr", int, float, str)

def last(sequence: list[NumberOrStr]) -> NumberOrStr:  # must be int, float or str
    return sequence[-1]

print(last([1, 2, 3]))
print(last(['a', 'b', 'c']))

# %% TypeVar in aliases
from typing import TypeVar, Iterable, Tuple

Number = TypeVar('Number', int, float, complex)
Vector = Iterable[Tuple[Number, Number]]

def inproduct(v: Vector[Number]) -> Number:
    return sum(x*y for x, y in v)

print(inproduct([(1.2, 3.4)]))

# %% TypeVar in classes
from typing import Generic, TypeVar

B = TypeVar('B')  # Declare a type variable

class Box(Generic[B]):  # Subclass Generic with the variable
    def __init__(self, content: T):
        self.content = content

    def get(self) -> T:
        return self.content

    def set(self, value: T) -> None:
        self.content = value

# Box that holds an int
int_box: Box[int] = Box(123)
print(int_box.get())  # 123
int_box.set(456)
print(int_box.get())

# Box that holds a str
str_box: Box[str] = Box("hello")
print(str_box.get())

# Box that holds a list of floats
float_list_box: Box[list[float]] = Box([1.0, 2.5])
print(float_list_box.get())  # [1.0, 2.5]
