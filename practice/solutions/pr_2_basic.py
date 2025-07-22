"""
Add type hints to functions. Find at least 2 bugs.
"""
from typing import TypedDict


class Question(TypedDict):
    question: str
    answer: str


def ask(question: Question) -> bool:
    user_answer = input(question["question"] + "? ")
    if user_answer.strip().lower() == question["answer"].lower():  # Case-insensitive
        return True
    else:
        return False


class Quiz:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.num_correct = 0

    def run(self):
        for question in self.questions:  # Get questions from self
            correct: bool = ask(question)
            if correct:  # Check bool
                self.num_correct += 1

        print(f"You got {self.num_correct}/{len(self.questions)}")


if __name__ == "__main__":
    qs: list[Question] = [  # Rename questions to avoid name conflict
        {
            "question": "What is the meaning of life",
            "answer": "42"
        },
        {
            "question": "Which programming language was named after a British sketch comedy troupe",
            "answer": "Python"
        }
    ]

    Quiz(qs).run()
