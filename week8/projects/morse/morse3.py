import tkinter as tk

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ' ': '/'
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in morse_code:
            morse += morse_code[char] + ' '
    return morse.strip()

# Function to convert Morse code to text
def morse_to_text(morse):
    text = ''
    morse_list = morse.split(' ')
    for code in morse_list:
        for key, value in morse_code.items():
            if code == value:
                text += key
    return text

# Event handler for encoding button
def encode():
    text = entry.get()
    morse = text_to_morse(text)
    output.delete(1.0, tk.END)
    output.insert(tk.END, morse)

# Event handler for decoding button
def decode():
    morse = entry.get()
    text = morse_to_text(morse)
    output.delete(1.0, tk.END)
    output.insert(tk.END, text)

# Creating the tkinter window
window = tk.Tk()
window.title("Morse Code Converter")

# Creating widgets
entry_label = tk.Label(window, text="Enter text/Morse code:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

encode_button = tk.Button(window, text="Encode to Morse", command=encode)
encode_button.pack()

decode_button = tk.Button(window, text="Decode to Text", command=decode)
decode_button.pack()

output_label = tk.Label(window, text="Result:")
output_label.pack()
output = tk.Text(window, height=5, width=50)
output.pack()

# Running the tkinter event loop
window.mainloop()
