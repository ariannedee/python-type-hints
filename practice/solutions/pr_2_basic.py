Question = dict[str, str]


question_1: Question = {
    "question": "What is the meaning of life",
    "answer": "42"  # Make str
}

question_2: Question = {
    "question": "Which programming language was named after a British sketch comedy troupe",
    "answer": "Python"
}

qs: list[Question] = [question_1, question_2]  # Rename questions to avoid name conflict


def ask(question: Question) -> bool:
    user_answer = input(question["question"] + "? ")
    if user_answer.lower() == question["answer"].lower():
        return True
    else:
        return False


class Quiz:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.num_correct = 0

    def run(self):
        for question in self.questions:  # Get questions from self
            correct = ask(question)
            if correct:  # Check bool
                self.num_correct += 1

        print(f"You got {self.num_correct}/{len(self.questions)}")


if __name__ == "__main__":
    Quiz(qs).run()
