# %% Aliases
import sys
from math import sqrt

Coord = tuple[float, float]        # 3.5

if sys.version_info >= (3, 10):
    from typing import TypeAlias
    Coord2: TypeAlias = tuple[float, float]  # 3.10

# type Coord3 = tuple[float, float] # 3.12

def distance(p1: Coord, p2: Coord) -> float:
    return sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )

print(distance((10, 10), (7, 6)))

# %% NewType
from typing import NewType

UserId = NewType("UserId", int)

def get_user(user_id: UserId) -> dict[str, object]:
    return {"id": user_id, "name": "Monty"}

uid1 = UserId(1)    # Works
uid2 = UserId('2')  # mypy: arg-type

get_user(3)          # mypy: arg-type
get_user(UserId(4))  # Works

# %% NewType + TypeDict example
from typing import TypedDict, NewType

UserId_ = NewType("UserId_", int)
ProductId = NewType("ProductId", int)

class Purchase(TypedDict):
    user_id: UserId_
    product_id: ProductId
    quantity: int

purchase: Purchase = {
    "user_id": UserId_(1),
    "product_id": ProductId(42),
    "quantity": 3,
}

def process(p: Purchase) -> None:
    print(f"User {p['user_id']} bought {p['quantity']} of product {p['product_id']}")
