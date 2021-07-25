from tkinter import *

THEME_COLOR = "#375362"
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")

        self.my_text = self.canvas.create_text(150, 100, text="question", font=("Ariel", 15, "italic"), width=250)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)
        # img = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, command=self.chose_wrong)
        self.wrong_button.grid(row=3, column=1, columnspan=2)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, command=self.chose_right)
        self.right_button.grid(row=3, column=0)

        self.my_score = Label(text=f"score : 0", bg=THEME_COLOR, fg="white", font=("Ariel", 20, "italic"))
        self.my_score.grid(row=0, column=2)

        self.get_next()

        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.my_score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.my_text, text=q_text)
        else:
            self.canvas.itemconfig(self.my_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def chose_right(self):
        self.feedback(self.quiz.check_answer("True"))

    def chose_wrong(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        print(is_right)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next)
