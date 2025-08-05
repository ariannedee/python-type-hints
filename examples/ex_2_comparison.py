# %% Basic function comparison
def is_correct_basic(guess, answer):
    return guess.strip().lower() == answer.lower()


def is_correct_w_docstring(guess, answer):
    """
    Check if the guess matches the answer, ignoring case and whitespace.

    Args:
        guess (str): The string to check
        answer (str): The correct answer to compare against

    Returns:
        bool: True if the guess matches the answer (case-insensitive, ignoring whitespace),
              False otherwise
    """
    return guess.strip().lower() == answer.lower()


def is_correct_w_type_comments(guess, answer):
    # type: (str, str) -> bool
    return guess.strip().lower() == answer.lower()


def is_correct_w_type_comments_multiline(guess,  # type: str
                                         answer  # type: str
                                         ):
    # type: (...) -> bool
    """Check if the guess matches the answer, ignoring case and whitespace."""
    return guess.strip().lower() == answer.lower()


def is_correct_w_annotations(guess: str, answer: str) -> bool:
    return guess.strip().lower() == answer.lower()


def is_correct_best_practice(guess: str, answer: str) -> bool:
    """Check if the guess matches the answer, ignoring case and whitespace."""
    return guess.strip().lower() == answer.lower()


# %% More complex function without type hints
def group_by_category(items):
    grouped = {}
    for item in items:
        category = item["category"]
        name = item["name"]
        grouped.setdefault(category, []).append(name)
    return grouped


grocery_list = [
    {"category": "Pasta", "name": "Spaghetti"},
    {"category": "Dairy", "name": "Eggs"},
    {"category": "Dairy", "name": "Parmesan"},
    {"category": "Produce", "name": "Garlic"},
    {"category": "Produce", "name": "Snap peas"},
]

groceries_by_aisle = {  # Return value from group_by_category()
    'Pasta': ['Spaghetti'],
    'Dairy': ['Eggs', 'Parmesan'],
    'Produce': ['Garlic', 'Snap peas']
}

assert group_by_category(grocery_list) == groceries_by_aisle

# %% With docstring
def group_by_category_w_docstring(items):
    """ Group items based on their category.
    Args:
        items (list of dict): A list of dictionaries representing items.
            Each dictionary must have the following structure:
            - 'category' (str)
            - 'name' (str)

    Returns:
        A dict mapping categories (str) to a list of item names (str).
        For example:
            {
                'Language': ['Python', 'Java'],
                'Database': ['MySQL'],
            }
    """
    ...

# %% With built-in generic containers
def group_by_category_w_hints(items: list[dict[str, str]]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for item in items:
        category = item["category"]
        name = item["name"]
        grouped.setdefault(category, []).append(name)
    return grouped


grocery_list: list[dict[str, str]]

group_by_category_w_hints(grocery_list)

# %% With typing imports and TypedDict
from typing import Dict, List, TypedDict


class Item(TypedDict):
    category: str
    name: str


def group_by_category_w_typed_dict(items: List[Item]) -> Dict[str, List[str]]:
    grouped: Dict[str, List[str]] = {}
    for item in items:
        category = item["category"]
        name = item["name"]
        grouped.setdefault(category, []).append(name)
    return grouped


grocery_list: List[Item]

group_by_category_w_typed_dict(grocery_list)
