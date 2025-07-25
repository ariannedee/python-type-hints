import json
import os
from random import shuffle
from typing import TypedDict, cast
from collections import defaultdict

from pydantic import TypeAdapter

Option = tuple[str, str]  # (option, result)

class Question(TypedDict):
    question: str
    options: list[Option]


class QuizDict(TypedDict):
    title: str
    questions: list[Question]


quiz_validator = TypeAdapter(QuizDict)

class Quiz:
    def __init__(self, title: str, questions: list[Question]):
        self.title = title
        self.questions = questions
        self.scores: dict[str, int] = defaultdict(int)  # result: count

    def get_result(self, results_list: list[str]) -> tuple[str, dict[str, int]]:
        for result in results_list:
            self.scores[result] += 1
        top_category = max(self.scores.items(), key=lambda tup: tup[1])[0]
        return top_category, dict(self.scores)


class InteractiveQuiz(Quiz):
    @staticmethod
    def ask_question(question: Question) -> str:
        print(f"{question['question']}")
        choices = question["options"]
        shuffle(choices)
        option_keys = "ABCDEFGHIJ"[:len(choices)]
        for key, (option, _) in zip(option_keys, choices):
            print(f"  {key}: {option}")

        while True:
            answer = input(f"Your answer ({'/'.join(option_keys)}): ").strip().upper()
            if len(answer) == 1 and answer in option_keys:
                key_index = option_keys.index(answer)
                return choices[key_index][1]
            else:
                print(f"❌ Invalid choice. Please select {', '.join(option_keys[:-1])} or {option_keys[-1]}.")

    def run(self) -> None:
        print(f"\n🎓 {self.title} 🎓\n")
        results = []
        for i, question in enumerate(self.questions, start=1):
            results.append(self.ask_question(question))
            print()
        result, scores = self.get_result(results)
        print(f"\n✅ Result: **{result}**!")
        print("📊 Scores:")
        for category, score in sorted(scores.items(), key=lambda tup: tup[1], reverse=True):
            print(f"  {category}: {score}")


class QuizManager:
    def __init__(self, storage_dir: str = "quizzes"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def save_quiz(self, quiz: QuizDict, filename: str) -> None:
        quiz_validator.validate_python(quiz)
        path = os.path.join(self.storage_dir, filename)
        with open(path, 'w') as f:
            json.dump(quiz, f, indent=2)

    def load_quiz(self, filename: str) -> Quiz:
        path = os.path.join(self.storage_dir, filename)
        with open(path, 'r') as f:
            quiz_data = json.load(f)

        quiz_validator.validate_python(quiz_data)
        return Quiz(quiz_data["title"], quiz_data["questions"])

    def list_quizzes(self) -> list[str]:
        return [f for f in os.listdir(self.storage_dir) if f.endswith(".json")]

def get_input_from_options(choices: list[str]) -> str:
    while True:
        for choice in choices:
            print("- " + choice.capitalize())

        user_choice = input("-> ").strip().lower()

        if user_choice in choices:
            return user_choice
        else:
            print("Invalid selection")


if __name__ == '__main__':
    # Import quizzes from .py files
    from quizzes.enneagram import enneagram_quiz
    from quizzes.hogwarts import hogwarts_quiz
    from quizzes.language import language_quiz
    from quizzes.leadership import leadership_quiz
    from quizzes.programming import programming_quiz

    quiz_manager = QuizManager()

    # Save quizzes to .json files
    quiz_manager.save_quiz(enneagram_quiz, "enneagram.json")
    quiz_manager.save_quiz(hogwarts_quiz, "hogwarts.json")
    quiz_manager.save_quiz(leadership_quiz, "leadership.json")
    quiz_manager.save_quiz(cast(QuizDict, language_quiz), "language.json")
    quiz_manager.save_quiz(cast(QuizDict, programming_quiz), "programming.json")

    # Run quiz
    quiz = quiz_manager.load_quiz(f'programming.json')
    run_quiz = InteractiveQuiz(quiz.title, quiz.questions)
    run_quiz.run()
