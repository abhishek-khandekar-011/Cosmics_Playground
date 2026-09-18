from tkinter import *
from quiz import QuizBrain

THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.label.grid(row=0, column=1, sticky="E", pady=(0, 20))

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question text goes here...",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        True_image = PhotoImage(file= "true.png")
        self.true_button = Button(image= True_image, highlightthickness= 0, command= self.true_answer)
        self.true_button.grid(row = 2, column = 0)

        False_image =  PhotoImage(file= "false.png")
        self.false_button = Button(image= False_image, highlightthickness= 0, command= self.false_answer)
        self.false_button.grid(row = 2, column = 1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"score:{self.quiz.score}")
            q__text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text = q__text)
        else:
            self.canvas.itemconfig(self.q_text, text = "You have reached end of the quiz")
            self.true_button.config(state= "disabled")
            self.false_button.config(state= "disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")

        self.window.after(1000, self.get_next_question)





if __name__ == "__main__":
    ui = UserInterface()



