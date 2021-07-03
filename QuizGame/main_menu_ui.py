from tkinter import *
from question_model import Question
import data
from quiz_brain import QuizBrain
from ui import QuizInterface
THEME_COLOR = "#375362"
FONT = ("Arial", 14, "bold")
FONT_BUTTON = ("Arial", 9, "bold")


class MainMenu:
    def __init__(self):
        self.window = Tk()
        self.window.title("Trivia Crack")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.answer = False

        self.canvas = Canvas(width=350, height=300, bg="white")
        self.text = Label(
            text="Choose a category!",
            font=FONT,
            fg=THEME_COLOR,
            bg="white",
            pady=40)
        self.text.grid(row=0, column=0, columnspan=3)
        self.canvas.grid(row=0, column=0, columnspan=3, rowspan=4, pady=20)

        self.computer = Button(text="General",
                               font=FONT_BUTTON,
                               relief="groove",
                               bg=THEME_COLOR,
                               fg="white",
                               activeforeground="black",
                               activebackground="white",
                               width=10,
                               command=lambda: self.get_data(9))
        self.computer.grid(row=1, column=0)

        self.math = Button(text="Math",
                           font=FONT_BUTTON,
                           relief="groove",
                           bg=THEME_COLOR,
                           fg="white",
                           activeforeground="black",
                           activebackground="white",
                           width=10,
                           command=lambda: self.get_data(19))
        self.math.grid(row=1, column=1)

        self.computer = Button(text="Computer",
                               font=FONT_BUTTON,
                               relief="groove",
                               bg=THEME_COLOR,
                               fg="white",
                               activeforeground="black",
                               activebackground="white",
                               width=10,
                               command=lambda: self.get_data(18))
        self.computer.grid(row=1, column=2)

        self.geo = Button(text="Geography",
                          font=FONT_BUTTON,
                          relief="groove",
                          bg=THEME_COLOR,
                          fg="white",
                          activeforeground="black",
                          activebackground="white",
                          width=10,
                          command=lambda: self.get_data(22))
        self.geo.grid(row=2, column=0)

        self.history = Button(text="History",
                              font=FONT_BUTTON,
                              relief="groove",
                              bg=THEME_COLOR,
                              fg="white",
                              activeforeground="black",
                              activebackground="white",
                              width=10,
                              command=lambda: self.get_data(23))
        self.history.grid(row=2, column=1)

        self.politics = Button(text="Politics",
                               font=FONT_BUTTON,
                               relief="groove",
                               bg=THEME_COLOR,
                               fg="white",
                               activeforeground="black",
                               activebackground="white",
                               width=10,
                               command=lambda: self.get_data(24))
        self.politics.grid(row=2, column=2)

        self.window.mainloop()

    def get_data(self, category):
        question_bank = []
        questions = data.get_questions(category)
        for question in questions:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        quiz = QuizBrain(question_bank)
        self.window.destroy()
        QuizInterface(quiz, questions[0]["category"])
