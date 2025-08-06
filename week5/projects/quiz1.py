import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    }
]

def start_quiz():
    global current_question, score
    current_question = 0
    score = 0
    show_question()

def show_question():
    question_label.config(text=questions[current_question]["question"])
    for i, option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option)

def check_answer(answer):
    global score, current_question
    correct_answer = questions[current_question]["answer"]
    if answer == correct_answer:
        score += 1
    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo("Quiz Finished", f"Quiz finished!\nYour score: {score}/{len(questions)}")

root = tk.Tk()
root.title("Quiz Application")

question_label = tk.Label(root, text="", wraplength=300, font=("Helvetica", 12))
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", width=30, command=lambda i=i: check_answer(questions[current_question]["options"][i]))
    button.pack(pady=5)
    option_buttons.append(button)

start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack(pady=10)

root.mainloop()
