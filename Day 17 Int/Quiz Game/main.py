from quiz_data import question_data
from question_model import Question
from quiz_brain import QuizBrain

from colors import *

# create new list - which include new object of class Question(x, y)
question_list = []

for question in question_data:
    q = question["question"]
    a = question["correct_answer"]
    new_question = Question(q, a)
    question_list.append(new_question)


# testing
for item in question_list:
    print(f"{item.answer.ljust(5)} | {item.question}")

quiz = QuizBrain(question_list)

while quiz.still_question():
    quiz.next_question()

print(f"You've completed the quiz \nYour Final score: {quiz.score}/{len(question_list)}")  # quiz.question_number
print(f"{round(quiz.score/len(question_list)*100)}% Ratio")
