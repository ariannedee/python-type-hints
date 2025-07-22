"""
Add type hints to functions. Find at least 2 bugs.
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
            self.num_correct += correct

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
