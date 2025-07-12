# %% Any
from typing import Any

def print_twice(x: Any) -> None:
    print(x)
    print(x)

# %%  Multiple values
def hypotenuse(a: int | float, b: int | float) -> float:
    ...
    return (a ** 2 + b ** 2) ** 0.5

assert hypotenuse(3, 4) == 5.0
assert hypotenuse(3.0, 4.0) == 5.0

# %%  <3.9, use Union
from typing import Union

def distance(a: Union[list, tuple], b: Union[list, tuple]) -> float:
    return hypotenuse(a[0] - b[0], a[1] - b[1])

assert distance([0, 0.0], (3, 4.0)) == 5

# %% Optional
from typing import Optional

def truncate(num: float, precision: Optional[int] = None) -> int | float:
    if precision is None:
        return round(num)
    return round(num * 10 ** precision) / 10 ** precision

assert truncate(1.234, None) == 1
assert truncate(12.34) == 12
assert truncate(1.234, 1) == 1.2
assert truncate(1.234, 2) == 1.23
assert truncate(1.234, 0) == 1.0
