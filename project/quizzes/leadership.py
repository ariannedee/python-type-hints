# See https://github.com/ariannedee/python-type-hints/issues/1 for an explanation
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # False during runtime
    from quiz import QuizDict

leadership_quiz: "QuizDict" = {
    "title": "Leadership Style Quiz (Four Color)",
    "questions": [
        {
            "question": "What best describes your work style?",
            "options": [
                ("Fast-paced and bold", "Red"),
                ("Caring and team-oriented", "Yellow"),
                ("Organized and detailed", "Blue"),
                ("Creative and big-picture", "Green")
            ]
        },
        {
            "question": "How do you handle conflict?",
            "options": [
                ("Tackle it directly", "Red"),
                ("Try to make everyone happy", "Yellow"),
                ("Follow proper procedures", "Blue"),
                ("Think about all the possible outcomes", "Green")
            ]
        },
        {
            "question": "What motivates you most?",
            "options": [
                ("Winning", "Red"),
                ("Helping others", "Yellow"),
                ("Getting it right", "Blue"),
                ("New ideas", "Green")
            ]
        },
        {
            "question": "How do you lead a team?",
            "options": [
                ("By taking charge", "Red"),
                ("By supporting people", "Yellow"),
                ("By setting rules", "Blue"),
                ("By inspiring change", "Green")
            ]
        },
        {
            "question": "Which compliments you most?",
            "options": [
                ("You're a go-getter", "Red"),
                ("You're so kind", "Yellow"),
                ("You're so thorough", "Blue"),
                ("You're so imaginative", "Green")
            ]
        }
    ]
}
