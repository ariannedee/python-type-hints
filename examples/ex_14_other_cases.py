# %% *args
def print_names(*args: str) -> None:
    for name in args:
        print(name)

print_names("Ringo", "John", "George", "Paul")
print_names(1)  # mypy: arg-type

# %% **kwargs
from typing import Union

NumberOrStr = Union[float, str]

def as_dict(**kwargs: NumberOrStr) -> dict[str, NumberOrStr]:
    return kwargs

print(as_dict(a=1, b=2.0))
print(as_dict(a=["a", "list"]))  # mypy: arg-type

# %% Decorators
import sys

if sys.version_info >= (3, 10):
    from typing import Callable, ParamSpec, TypeVar

    P = ParamSpec('P')  # 3.10+
    R = TypeVar('R')

    def log_decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result = func(*args, **kwargs)
            print(f"Input: {args}, {kwargs}")
            print(f"Output: {result}")
            return result
        return wrapper

    @log_decorator
    def add_numbers(a: int, b: int) -> int:
        return a + b

    print(add_numbers('1', '2'))  # mypy: arg-type

# %% Generators
from typing import Generator, Iterator

# Generator[YieldType, SendType, ReturnType]
def fib(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while n > 0:
        yield a
        b, a = a + b, b
        n -= 1

g: Generator[int, None, None] = fib(10)
i: Iterator[int] = (x for x in range(3))

# %% Overload
from typing import overload, Union

@overload
def parse_value(value: str) -> int: ...
@overload
def parse_value(value: list[str]) -> list[int]: ...
def parse_value(value: Union[str, list[str]]) -> Union[int, list[int]]:  # In 3.10+, use | instead of Union
    """
    Parse either a single string or a list of strings into integers.
    """
    if isinstance(value, list):
        return [int(v) for v in value]
    return int(value)

# Type checker understands these correctly
with_int: int = parse_value("123")
with_list: list[int] = parse_value(["123", "456"])
should_return_list: int = parse_value(["123"])  # mypy: assignment