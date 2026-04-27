# %% Aliases
from math import sqrt

type Coords = tuple[float, float]

def distance(p1: Coords, p2: Coords) -> float:
    return sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )

print(distance((10, 10), (7, 6)))