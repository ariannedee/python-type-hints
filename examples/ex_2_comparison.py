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


def is_correct_w_annotations(guess: str, answer: str) -> bool:
    return guess.strip().lower() == answer.lower()


def is_correct_best_practice(guess: str, answer: str) -> bool:
    """
    Check if the guess matches the answer, ignoring case and whitespace.
    """
    return guess.strip().lower() == answer.lower()

# -------------------------------------------------------------------

# More complex function without type hints
def run_quiz_basic(questions: list[dict[str, str]]) -> None:
    for question in questions:
        answer = input(question["question"] + "? ")
        if answer == question["answer"]:
            print("Correct")
        else:
            print("Incorrect")

quiz_questions = [
    {"question": "What is the meaning of life?", "answer": "42"},
    {"question": "What was Python named after?", "answer": "Monty Python"}
]

run_quiz_basic(quiz_questions)


# With built-in generic containers
def run_quiz_w_container(questions: list[dict[str, str]]) -> None:
    for question in questions:
        answer = input(question["question"] + "? ")
        if answer == question["answer"]:
            print("Correct")
        else:
            print("Incorrect")

quiz_questions: list[dict[str, str]]
run_quiz_w_container(quiz_questions)


# With typing containers and TypedDict
from typing import List, TypedDict

class Question(TypedDict):
    question: str
    answer: str

def run_quiz_w_typeddict(questions: List[Question]) -> None:
    for question in questions:
        answer = input(question["question"] + "? ")
        if answer == question["answer"]:
            print("Correct")
        else:
            print("Incorrect")

quiz_questions: List[Question]
run_quiz_w_typeddict(quiz_questions)
