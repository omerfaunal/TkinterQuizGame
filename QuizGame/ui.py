from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 12, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain, category):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Crack")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.answer = False

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.category_label = Label(text=f"{category}", fg="white", bg=THEME_COLOR)
        self.category_label.grid(row=0, column=0)

        self.canvas = Canvas(width=350, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            175,
            125,
            width=300,
            text="Question",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(
                self.question_text,
                text=f"Congratulations, you finished the quiz! \n Your Score: {self.quiz_brain.score}/10",
                font=("Comic Sans MS", 12, "italic"),
                fill="black",
                justify="center")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.config(bg="white")

    def true_pressed(self):
        self.answer = self.quiz_brain.check_answer("True")
        self.after_answer()

    def false_pressed(self):
        self.answer = self.quiz_brain.check_answer("False")
        self.after_answer()

    def after_answer(self):
        if self.answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
