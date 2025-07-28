# %% Generic syntax for functions
def first[T](items: list[T]) -> T:
    return items[0]

print(first([1, 2, 3]))
print(first(['a', 'b', 'c']))
print(first([1, 'a']))  # Works because T is object

# %% Type variables
from typing import TypeVar  # <3.12

T = TypeVar("T")

def first2(sequence: list[T]) -> T:
    return sequence[0]

# %% Bounded generics
class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

def speak[T: Animal](animal: T) -> None:  # Type must be an Animal, Dog is okay
    animal.speak()

speak(Dog())  # Okay

# %% Bounded TypeVar
A = TypeVar("A", bound=Animal)

def speak2(animal: A) -> None:
    animal.speak()

# %% Constrained generics
def last[T: (int, float, str) = int](sequence: list[T]) -> T:  # T must be int, float or str
    return sequence[-1]

print(last([1, 2, 3]))
print(last(['a', 'b', 'c']))

# %% TypeVar with constraints
from typing import TypeVar

NumberOrStr = TypeVar("NumberOrStr", int, float, str)

def last2(sequence: list[NumberOrStr]) -> NumberOrStr:
    return sequence[-1]

# %% Generic syntax for type aliases
type ListOrSet[T] = list[T] | set[T]

# %% TypeVar in aliases
from typing import TypeVar, Iterable, Tuple

Number = TypeVar('Number', int, float, complex)
Vector = Iterable[Tuple[Number, Number]]

def inproduct(v: Vector[Number]) -> Number:
    return sum(x*y for x, y in v)

print(inproduct([(1.2, 3.4)]))

# %% Generic syntax for classes


# %% TypeVar with classes
from typing import Generic, TypeVar

B = TypeVar('B')  # Declare a type variable

class Box(Generic[B]):  # Subclass Generic with the variable
    def __init__(self, value: B):
        self.value = value

    def get(self) -> B:
        return self.value

    def set(self, value: B) -> None:
        self.value = value

# Box that holds an int
int_box = Box[int](123)
print(int_box.get())  # 123
int_box.set(456)
print(int_box.get())

# Box that holds a str
str_box = Box[str]("hello")
print(str_box.get())

# Box that holds a list of floats
float_list_box = Box[list[float]]([1.0, 2.5])
print(float_list_box.get())  # [1.0, 2.5]
