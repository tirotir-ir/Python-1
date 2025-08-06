import tkinter as tk
from tkinter import simpledialog, messagebox

flashcards = []

def add_flashcard():
    question = simpledialog.askstring("Input", "Enter the question:")
    answer = simpledialog.askstring("Input", "Enter the answer:")
    if question and answer:
        flashcards.append((question, answer))
        save_flashcards()

def show_flashcard():
    if flashcards:
        question, answer = flashcards[0]
        question_label.config(text=question)
        answer_label.config(text="")
    else:
        question_label.config(text="No flashcards available.")
        answer_label.config(text="")

def show_answer():
    if flashcards:
        answer_label.config(text=flashcards[0][1])

def next_flashcard():
    if flashcards:
        flashcards.append(flashcards.pop(0))
        show_flashcard()

def save_flashcards():
    with open("flashcards.txt", "w") as file:
        for question, answer in flashcards:
            file.write(question + "\n")
            file.write(answer + "\n")

def load_flashcards():
    try:
        with open("flashcards.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                question = lines[i].strip()
                answer = lines[i+1].strip()
                flashcards.append((question, answer))
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("Flashcard Application")

add_button = tk.Button(root, text="Add Flashcard", command=add_flashcard)
add_button.pack(pady=10)

show_button = tk.Button(root, text="Show Flashcard", command=show_flashcard)
show_button.pack(pady=10)

answer_button = tk.Button(root, text="Show Answer", command=show_answer)
answer_button.pack(pady=10)

next_button = tk.Button(root, text="Next Flashcard", command=next_flashcard)
next_button.pack(pady=10)

question_label = tk.Label(root, text="", font=("Helvetica", 24))
question_label.pack(pady=20)

answer_label = tk.Label(root, text="", font=("Helvetica", 18))
answer_label.pack(pady=20)

load_flashcards()
show_flashcard()

root.mainloop()
