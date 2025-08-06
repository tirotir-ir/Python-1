import tkinter as tk

# Function to convert character to binary
def char_to_binary(char):
    binary = bin(ord(char))[2:].zfill(8)
    return binary

# Function to convert binary to character
def binary_to_char(binary):
    char = chr(int(binary, 2))
    return char

# Event handler for converting character to binary
def convert_to_binary():
    char = entry.get()
    binary = char_to_binary(char)
    output_label.config(text="Binary representation: " + binary)

# Event handler for converting binary to character
def convert_to_char():
    binary = entry.get()
    character = binary_to_char(binary)
    output_label.config(text="Corresponding character: " + character)

# Creating the tkinter window
window = tk.Tk()
window.title("Character and Binary Converter")

# Creating widgets
entry_label = tk.Label(window, text="Enter a character or binary:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

convert_to_binary_button = tk.Button(window, text="Convert to Binary", command=convert_to_binary)
convert_to_binary_button.pack()

convert_to_char_button = tk.Button(window, text="Convert to Character", command=convert_to_char)
convert_to_char_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

# Running the tkinter event loop
window.mainloop()
