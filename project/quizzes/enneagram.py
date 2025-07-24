from typing import TYPE_CHECKING

if TYPE_CHECKING:  # False during runtime
    import quiz

enneagram_quiz: "quiz.QuizDict" = {
    "title": "Which Enneagram Type Are You?",
    "questions": [
        {
            "question": "What drives your everyday behavior?",
            "options": [
                ("Doing the right thing is most important", "1"),
                ("Being loved and appreciated", "2"),
                ("Succeeding and being admired", "3"),
                ("Being unique and emotionally authentic", "4"),
            ]
        },
        {
            "question": "In a crisis, you are most likely to...",
            "options": [
                ("Retreat and analyze what's going on", "5"),
                ("Question everything and prepare for all possibilities", "6"),
                ("Focus on what's fun or exciting to distract yourself", "7"),
                ("Take charge and protect yourself and others", "8"),
            ]
        },
        {
            "question": "What brings you the most satisfaction?",
            "options": [
                ("Feeling peaceful and avoiding conflict", "9"),
                ("Improving yourself and staying ethical", "1"),
                ("Being there for people who need you", "2"),
                ("Being successful and goal-oriented", "3"),
            ]
        },
        {
            "question": "What's your communication style?",
            "options": [
                ("Deep, poetic, or emotionally rich", "4"),
                ("Precise, clear, and focused on facts", "5"),
                ("Playful, energetic, and scattered", "7"),
                ("Firm, direct, and authoritative", "8"),
            ]
        },
        {
            "question": "How do you tend to handle relationships?",
            "options": [
                ("By being caring and indispensable", "2"),
                ("By being dependable and prepared", "6"),
                ("By being calm and accommodating", "9"),
                ("By being driven and impressive", "3"),
            ]
        },
        {
            "question": "What frustrates you the most?",
            "options": [
                ("Injustice or laziness", "1"),
                ("Feeling invisible or misunderstood", "4"),
                ("Being controlled or disrespected", "8"),
                ("Feeling trapped or missing out", "7"),
            ]
        },
        {
            "question": "What’s most important in your personal growth?",
            "options": [
                ("Staying calm and keeping the peace", "9"),
                ("Expressing your inner truth", "4"),
                ("Developing self-reliance and confidence", "6"),
                ("Letting go of control and trusting others", "8"),
            ]
        },
        {
            "question": "How do you view your ideal self?",
            "options": [
                ("Moral, principled, and self-controlled", "1"),
                ("Helpful, generous, and warm", "2"),
                ("Creative, deep, and emotionally honest", "4"),
                ("Prepared, loyal, and responsible", "6"),
            ]
        },
        {
            "question": "Your biggest inner fear might be...",
            "options": [
                ("Being without support or guidance", "6"),
                ("Being insignificant or a failure", "3"),
                ("Being in pain or deprived", "7"),
                ("Losing connection or harmony", "9"),
            ]
        }
    ]
}
