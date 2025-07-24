import json
import os
from random import shuffle
from collections import defaultdict


class Quiz:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
        self.scores = defaultdict(int)  # result: count

    def get_result(self, results_list):
        for result in results_list:
            self.scores[result] += 1
        top_category = max(self.scores.items(), key=lambda tup: tup[1])[0]
        return top_category, dict(self.scores)


class InteractiveQuiz(Quiz):
    @staticmethod
    def ask_question(question):
        print(f"{question["question"]}")
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

    def run(self):
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
    def __init__(self, storage_dir = "quizzes"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def save_quiz(self, quiz, filename):
        path = os.path.join(self.storage_dir, filename)
        with open(path, 'w') as f:
            json.dump(quiz, f, indent=2)

    def load_quiz(self, filename):
        path = os.path.join(self.storage_dir, filename)
        with open(path, 'r') as f:
            quiz_data = json.load(f)

        return Quiz(quiz_data["title"], quiz_data["questions"])

    def list_quizzes(self):
        return [f for f in os.listdir(self.storage_dir) if f.endswith(".json")]

def get_input_from_options(choices):
    while True:
        for choice in choices:
            print("- " + choice.capitalize())

        user_choice = input("-> ").strip().lower()

        if user_choice in choices:
            return user_choice
        else:
            print("Invalid selection")

if __name__ == '__main__':
    from quizzes.programming import programming_quiz

    quiz_manager = QuizManager()
    quiz_manager.save_quiz(programming_quiz, "programming.json")

    quiz = quiz_manager.load_quiz(f'programming.json')

    run_quiz = InteractiveQuiz(quiz.title, quiz.questions)
    run_quiz.run()
