from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):      # quiz_brain is from QuizBrain class
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.config(font=("Arial", 22, "bold"))
        self.score_label.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questionText = self.canvas.create_text(
            150, 125,
            text=f"",
            font=FONT,
            fill=COLOR,
            width=250   #for wrap text
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        correct_img = PhotoImage(file="images/true.png")
        self.correct_butt = Button(image=correct_img, highlightthickness=0, command=self.true_butt)
        self.correct_butt.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_butt = Button(image=wrong_img, highlightthickness=0, command=self.false_butt)
        self.wrong_butt.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # restart background color to the - white
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=q_text)
        else:
            self.canvas.itemconfig(self.questionText, text=f"Quiz was ended!\nYour result: \n{self.quiz.score/len(self.quiz.question_list)*100}%")
            self.correct_butt.config(state="disabled")   # disabled buttons when app end
            self.wrong_butt.config(state="disabled")

    def true_butt(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_butt(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question)





