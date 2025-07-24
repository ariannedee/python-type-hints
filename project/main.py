from quiz import QuizManager, get_input_from_options, InteractiveQuiz

if __name__ == '__main__':
    quiz_manager = QuizManager()

    # Prompt user for quiz to run from available json files
    quiz_files = quiz_manager.list_quizzes()
    quiz_manager.list_quizzes()
    quiz_names = [filename.split('.json')[0] for filename in quiz_files]
    print("Which quiz do you want to do?")
    chosen_quiz = get_input_from_options(quiz_names)
    quiz = quiz_manager.load_quiz(f'{chosen_quiz}.json')

    # Run quiz
    run_quiz = InteractiveQuiz(quiz.title, quiz.questions)
    run_quiz.run()
