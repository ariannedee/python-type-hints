# %% Any
from typing import Any

def print_twice(x: Any) -> None:
    print(x)
    print(x)

# %%  Multiple values
import sys

from math import sqrt

def hypotenuse(a: int | float, b: int | float) -> float:  # 3.10
    return sqrt(a ** 2 + b ** 2)

assert hypotenuse(3, 4) == 5.0
assert hypotenuse(3.0, 4.0) == 5.0

# %%  <3.10, use Union
from typing import Union

def stringify(val: Union[int, float, str]) -> str:
    return str(val)

# %% Optional
from typing import Optional

def find_index(item: str, a_list: list[str]) -> Optional[int]:
    for i, x in enumerate(a_list):
        if x == item:
            return i
    return None
