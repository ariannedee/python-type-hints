# %% __annotations__
def greet(name: str, times: int = 2) -> str:
    return f"Hello {name}! " * times

print(greet.__annotations__)
# {'name': <class 'str'>, 'times': <class 'int'>, 'return': <class 'str'>}

# %%
from typing import get_type_hints

print(get_type_hints(greet))
# {'name': <class 'str'>, 'times': <class 'int'>, 'return': <class 'str'>}

# %% Forward references
from typing import Any, Optional

def links_to(node: 'Node') -> 'Optional[Node]':
    return node.next

class Node:
    def __init__(self, val: Any, next_: Optional['Node'] = None) -> None:
        self.val = val
        self.next = next_


print(links_to.__annotations__)  # {'node': 'Node', 'return': 'Optional[Node]'}
print(get_type_hints(links_to))  # {'node': <class 'Node'>, 'return': Optional[Node]}

# %% inspect module
import inspect

sig = inspect.signature(greet)
for name, param in sig.parameters.items():
    print(f"{name}: {param.annotation}, {param.kind}, {param.default}")
print(f"Return: {sig.return_annotation}")

# name: <class 'str'>, POSITIONAL_OR_KEYWORD, <class 'inspect._empty'>
# times: <class 'int'>, POSITIONAL_OR_KEYWORD, 2
# Return: <class 'str'>