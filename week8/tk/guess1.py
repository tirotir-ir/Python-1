import tkinter as tk
import random

def check_guess():
    try:
        guess = int(entry.get())
        if guess == number:
            result_label.config(text="Correct! You guessed the number!")
        elif guess < number:
            result_label.config(text="Too low! Try again.")
        else:
            result_label.config(text="Too high! Try again.")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Generate a random number
number = random.randint(1, 100)

# Create the main window
root = tk.Tk()
root.title("Guessing Game")

# Create a label
instruction_label = tk.Label(root, text="Guess a number between 1 and 100")
instruction_label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to check the guess
button = tk.Button(root, text="Guess", command=check_guess)
button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
