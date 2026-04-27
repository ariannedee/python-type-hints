# %% Aliases
from math import sqrt
from typing import TypeAlias

Coord = tuple[float, float]              # 3.5
Coord2: TypeAlias = tuple[float, float]  # 3.10
# type Coord3 = tuple[float, float]      # 3.12

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

# %% Deeply nested types without aliases

def process_batch(
    data: list[list[float]],
    ids: list[str]
) -> tuple[dict[str, list[float]], list[str]]:
    ...

# %% Nested types with aliases
from typing import TypeAlias

Embedding: TypeAlias = list[float]
UserID: TypeAlias = str
Batch: TypeAlias = list[Embedding]

def process_batch_w_aliases(
    embeddings: Batch,
    user_ids: list[UserID]
) -> tuple[dict[UserID, Embedding], list[UserID]]:
    ...