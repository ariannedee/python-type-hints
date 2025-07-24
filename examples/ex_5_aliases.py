# %% Aliases
from math import sqrt
from typing import TypeAlias

type Coords = tuple[float, float]       # 3.12
Coord: TypeAlias = tuple[float, float]  # 3.10
Coordinate = tuple[float, float]        # 3.5

def distance(p1: Coord, p2: Coordinate) -> float:
    return sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )

print(distance((10, 10), (7, 6)))

# %% NewType
from typing import NewType

UserId = NewType("UserId", int)

def get_user(user_id: UserId) -> dict:
    ...

uid1 = UserId(1)    # Works
uid2 = UserId('2')  # Mypy: arg-type

get_user(3)          # Mypy: arg-type
get_user(UserId(4))  # Works

# %% NewType + TypeDict example
from typing import TypedDict, NewType

UserId = NewType("UserId", int)
ProductId = NewType("ProductId", int)

class Purchase(TypedDict):
    user_id: UserId
    product_id: ProductId
    quantity: int

purchase: Purchase = {
    "user_id": UserId(1),
    "product_id": ProductId(42),
    "quantity": 3,
}

def process(p: Purchase) -> None:
    print(f"User {p['user_id']} bought {p['quantity']} of product {p['product_id']}")
