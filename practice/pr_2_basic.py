"""
1. Add type hints to functions.
2. Find at least 2 bugs.
3. Get mypy to pass with no errors
4. Bonus: Run with questions from quiz_questions.py and get mypy to pass
"""

def ask(question):
    user_answer = input(question["question"] + "? ")
    if user_answer == question["answer"]:
        return True
    else:
        return False


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.num_correct = 0

    def run(self):
        for question in questions:
            correct = ask(question)
            if correct:
                self.num_correct += correct
                print("Correct!")
            else:
                print("Nope")

        print(f"You got {self.num_correct}/{len(self.questions)}")


if __name__ == "__main__":
    questions = [
        {
            "question": "What is the meaning of life",
            "answer": 42
        },
        {
            "question": "Which programming language was named after a British sketch comedy troupe",
            "answer": "Python"
        }
    ]

    Quiz(questions).run()
