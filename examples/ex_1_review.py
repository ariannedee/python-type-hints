question_1 = {  # Variable, dictionary (dict)
    "question": "What is the meaning of life",
    "answer": 42
}

question_2 = {
    "question": "Which programming language was named after a British sketch comedy troupe",
    "answer": "Python"
}

questions = [question_1, question_2]  # List

def ask(question):  # Function
    user_answer = input(question["question"] + "? ")
    if user_answer == question["answer"]:
        return True
    else:
        return False


class Quiz:  # Class
    def __init__(self, questions):
        self.questions = questions
        self.num_correct = 0

    def run(self):  # Method
        for question in questions:
            correct = ask(question)
            self.num_correct += correct

        print(f"You got {self.num_correct}/{len(self.questions)}")  # F-string (interpolation)


if __name__ == "__main__":
    Quiz(questions).run()
