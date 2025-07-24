# %% Literal
from typing import Literal, TypedDict

Difficulty = Literal["easy", "medium", "hard"]

class Question(TypedDict):
    question: str
    answer: str
    difficulty: Difficulty

# %% Constants
from typing import Final

DAYS_IN_A_WEEK: Final = 7
DAYS_IN_A_WEEK = 8  # mypy: misc error

# %% NoReturn
import time
from typing import NoReturn

def elapsed_time() -> NoReturn:
    seconds = 0
    while True:
        print(seconds, end='\r')
        time.sleep(1)
        seconds += 1

elapsed_time()

# %% Callable (e.g. function passed as argument)
from typing import Callable

def case_insensitive(guess: str, answer: str) -> bool:
    return guess.strip().lower() == answer.lower()

def is_correct(guess: str, answer: str,
               scorer: Callable[[str, str], bool]) -> int:
    return scorer(guess, answer)

assert is_correct(' monty Python', 'Monty Python', case_insensitive) is True

# %% Annotated - metadata
from typing import Annotated

def age_check(age: Annotated[int, "must be positive"]) -> bool:
    return age > 0