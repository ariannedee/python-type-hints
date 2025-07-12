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

def find_index(item: str, a_list: list[str]) -> Optional[int]:
    for i, x in enumerate(a_list):
        if x == item:
            return i
    return None
