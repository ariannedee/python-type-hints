# See https://github.com/ariannedee/python-type-hints/issues/1 for an explanation
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # False during runtime
    from quiz import QuizDict

programming_quiz: QuizDict = {
    "title": "Which Programming Language Are You?",
    "questions": [
        {
            "question": "How do you feel about strict rules?",
            "options": [
                ("Love them. Structure is everything.", "Java"),
                ("I prefer some freedom.", "Python"),
                ("Rules are made to be broken.", "JavaScript"),
                ("I want total control.", "C")
            ]
        },
        {
            "question": "What's your ideal project?",
            "options": [
                ("Enterprise backend systems", "Java"),
                ("Data science and automation", "Python"),
                ("Interactive websites", "JavaScript"),
                ("Game engines or embedded systems", "C")
            ]
        },
        {
            "question": "What's your vibe?",
            "options": [
                ("Professional and reliable", "Java"),
                ("Friendly and practical", "Python"),
                ("Creative and chaotic", "JavaScript"),
                ("Efficient and powerful", "C")
            ]
        },
        {
            "question": "How do you handle bugs?",
            "options": [
                ("Write lots of unit tests to prevent them", "Java"),
                ("Add print/debug statements and work it out calmly", "Python"),
                ("Open DevTools and wing it", "JavaScript"),
                ("Read core dumps and hex if I have to", "C")
            ]
        },
        {
            "question": "Pick a motto:",
            "options": [
                ("Write once, run anywhere", "Java"),
                ("Simple is better than complex", "Python"),
                ("Move fast and break things", "JavaScript"),
                ("Trust nothing, manage everything", "C")
            ]
        },
        {
            "question": "What's your relationship with memory?",
            "options": [
                ("I let the runtime deal with it", "Java"),
                ("I trust garbage collection, but I’m cautious", "Python"),
                ("What’s memory? Oh look, a new JS framework!", "JavaScript"),
                ("I manage it myself, byte by byte", "C")
            ]
        }
    ]
}
