"""Only run this file in 3.12+ (See PEP """
# %% Generic syntax for functions
def first[T](items: list[T]) -> T:
    return items[0]

print(first([1, 2, 3]))
print(first(['a', 'b', 'c']))
print(first([1, 'a']))  # Works because T is object

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

# %% Constrained generics
def last[T: (int, float, str)](sequence: list[T]) -> T:  # T must be int, float or str
    return sequence[-1]

print(last([1, 2, 3]))
print(last(['a', 'b', 'c']))

# %% Generic syntax for type aliases
type ListOrSet[T] = list[T] | set[T]

# %% Generic syntax for classes
class Box[T]:
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
