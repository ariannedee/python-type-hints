"""
Add type hints to functions. Find at least 2 bugs.
"""
from typing import TypedDict


class Question(TypedDict):
    question: str
    answer: str


def ask(question: Question) -> bool:
    user_answer = input(question["question"].strip("?") + "? ")
    if user_answer.strip().lower() == question["answer"].lower():  # Case-insensitive
        return True
    else:
        return False


class Quiz:
    def __init__(self, qs: list[Question]):
        self.questions = qs
        self.num_correct = 0

    def run(self) -> None:
        for question in self.questions:  # Get questions from self
            correct: bool = ask(question)
            if correct:  # Check bool
                self.num_correct += 1
                print("Correct!")
            else:
                print("Nope")

        print(f"You got {self.num_correct}/{len(self.questions)}")


if __name__ == "__main__":
    from quiz_questions import questions
    Quiz(questions).run()