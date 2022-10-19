from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


# create new list - which include new object of class Question(x, y)
question_list = []

for question in question_data:
    q = question['question']
    a = question['correct_answer']
    new_question = Question(q, a)
    question_list.append(new_question)


quiz = QuizBrain(question_list)

while quiz.still_question():
    quiz.next_question()

print(f"You've completed the quiz \nYour Final score: {quiz.score}/{len(question_list)}")  # quiz.question_number
print(f"{round(quiz.score/len(question_list)*100)}% Ration")




"""
# using only function
def quiz():
    x = 0
    score = 0
    while True:
        if x == len(question_data):
            break
        question_ask = input(f"{x + 1}. {question_data[x]['question']} ").lower()
        answer = question_data[x]['correct_answer'].lower()
        if question_ask == answer:
            score += 1
        else:
            print(f"Correct answer was: {answer}")
        print(f"Total score is: {score}")
        x += 1


quiz()

"""
