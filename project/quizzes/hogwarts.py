from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import quiz

hogwarts_quiz: quiz.QuizDict = {
    "title": "Hogwarts House Quiz",
    "questions": [
        {
            "question": "What do you value most?",
            "options": [
                ("Courage", "Gryffindor"),
                ("Wisdom", "Ravenclaw"),
                ("Loyalty", "Hufflepuff"),
                ("Ambition", "Slytherin")
            ]
        },
        {
            "question": "Which activity do you enjoy most?",
            "options": [
                ("Exploring new places", "Gryffindor"),
                ("Reading a good book", "Ravenclaw"),
                ("Helping a friend", "Hufflepuff"),
                ("Planning for success", "Slytherin")
            ]
        },
        {
            "question": "Pick a magical creature.",
            "options": [
                ("Phoenix", "Gryffindor"),
                ("Owl", "Ravenclaw"),
                ("Niffler", "Hufflepuff"),
                ("Basilisk", "Slytherin")
            ]
        },
        {
            "question": "What’s your greatest strength?",
            "options": [
                ("Bravery", "Gryffindor"),
                ("Intelligence", "Ravenclaw"),
                ("Patience", "Hufflepuff"),
                ("Determination", "Slytherin")
            ]
        },
        {
            "question": "How do you respond to challenges?",
            "options": [
                ("Face them head-on", "Gryffindor"),
                ("Analyze and strategize", "Ravenclaw"),
                ("Stay calm and support others", "Hufflepuff"),
                ("Use them as stepping stones to power", "Slytherin")
            ]
        }
    ]
}
