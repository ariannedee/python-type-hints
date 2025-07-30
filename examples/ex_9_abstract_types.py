# %%
from typing import Optional, Sequence  # Use int | None in 3.10+

def smallest_item_index(seq: Sequence[int]) -> Optional[int]:
    if len(seq) == 0:           # length
        return None
    smallest = min(seq)         # iterable
    return seq.index(smallest)  # index method

assert smallest_item_index([5, 2, 1, 4, 5]) == 2
assert smallest_item_index((1, 1)) == 0
assert smallest_item_index([]) is None

# %%
from typing import Iterable

def num_chars(items: Iterable[str]) -> int:
    total = 0
    for item in items:
        total += len(item)
    return total

assert num_chars([]) == 0                        # List
assert num_chars("1234") == 4                    # String
assert num_chars(('1234567', )) == 7             # Tuple
assert num_chars({'1', '2345'}) == 5             # Set
assert num_chars({'12': 'a', '3456': 'b'}) == 6  # Dict
assert num_chars(str(i) for i in range(9)) == 9  # Generator

# %%
from typing import Sequence

def total(values: Sequence[float]) -> float:
    if len(values) == 0:
        return 0
    return values[0] + total(values[1:])

assert total([]) == 0
assert total([1]) == 1
assert total((1, 2, 3)) == 6
assert total([1.1, 2.2, 3.3]) == 6.6

# %%
from collections.abc import Mapping

def print_key_w_counts(data: Mapping[str, int]) -> None:
    for key, value in data.items():
        print(key * value)

print_key_w_counts({'A': 1, 'B': 2, 'C': 3})

from collections import ChainMap
d = ChainMap({'A': 1, 'B': 2}, {'B': 1, 'C': 3})
print_key_w_counts(d)
