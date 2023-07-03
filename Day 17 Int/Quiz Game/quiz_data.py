"""
for data
trivia

https://opentdb.com/
"""
import requests
response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")

data_json = response.json()
question_data = data_json["results"]


# we can just use local data instead of API
"""
question_data = [

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "Linus Torvalds created Linux and Git.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "The logo for Snapchat is a Bell.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "RAM stands for Random Access Memory.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "Ada Lovelace is often considered the first computer programmer.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "The Windows 7 operating system has six main editions.",
     "correct_answer": "True", "incorrect_answers": ["False"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "The Windows ME operating system was released in the year 2000.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]},

    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
     "correct_answer": "True",
     "incorrect_answers": ["False"]}
]
"""

