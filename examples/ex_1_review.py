question_1 = {  # Dictionary (dict)
    "question": "What is the meaning of life",
    "answer": 42
}

question_2 = {
    "question": "Which programming language was named after a British sketch comedy troupe",
    "answer": "Python"
}

questions = [question_1, question_2]  # List

def is_correct(guess, answer):
    return guess.strip().lower() == answer.lower()

def ask(question):  # Function
    user_answer = input(question["question"] + "? ")  # User input
    if is_correct(user_answer, question["answer"]):  # Conditional
        print('Correct')
        return True
    else:
        print('Incorrect')
        return False


class Quiz:  # Class
    def __init__(self, questions):  # Dunder methods - __init__ is the initializer that gets called implicitly on Quiz()
        self.questions = questions  # Instance attributes
        self.num_correct = 0

    def run(self):  # Method
        for question in questions:  # For-loop
            correct = ask(question)
            self.num_correct += correct

        print(f"You got {self.num_correct}/{len(self.questions)}")  # F-string (interpolation)


if __name__ == "__main__":
    Quiz(questions).run()
