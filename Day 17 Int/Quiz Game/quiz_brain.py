class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.score = 0
        self.question_number = 0
        self.x = None  # for - True or false

    def still_question(self):
        return self.question_number < len(self.question_list)
        # returned True or False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False) (1/0)?: ")

        # 1 True and 0 False
        if current_question.answer == "True":
            self.x = 1
        elif current_question.answer == "False":
            self.x = 0

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower() or int(user_answer) == self.x:
            self.score += 1
            print(f"That's a correct answer")
        else:
            print("That's wrong!")
        print()
        print(f"Correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number} \n")
