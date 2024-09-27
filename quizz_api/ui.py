from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain



        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250,bg="white", highlightthickness=0)
        self.canvas.grid(row=1,column=0, columnspan=2, pady=30)
        self.question_text = self.canvas.create_text(150, 125, width=280 ,text="here goes the question", fill=THEME_COLOR , font=("Arial",20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        correct_img = PhotoImage(file="true.png")
        self.true_button = Button(image=correct_img, highlightthickness=0, command=self.true)
        self.true_button.grid(column=0,row=3)

        false_img = PhotoImage(file="false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false)
        self.false_button.grid(column=1,row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
       self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        wrong = self.quiz.check_answer("False")
        self.give_feedback(wrong)
    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000,self.get_next_question)









