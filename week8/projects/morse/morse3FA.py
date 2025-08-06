import tkinter as tk

# Persian (Farsi) Morse code dictionary
persian_morse_code = {
    'ا': '.-', 'ب': '-...', 'پ': '.--.', 'ت': '-',
    'ث': '--.-', 'ج': '.---', 'چ': '----', 'ح': '....',
    'خ': '---', 'د': '.--', 'ذ': '--..', 'ر': '.-.',
    'ز': '-.-', 'ژ': '-..-', 'س': '...', 'ش': '--.',
    'ص': '....-', 'ض': '-.--', 'ط': '-..-', 'ظ': '-..-.',
    'ع': '-.-.', 'غ': '--', 'ف': '..-.', 'ق': '-.-.',
    'ک': '-.-', 'گ': '--.', 'ل': '.-..', 'م': '--',
    'ن': '-.', 'و': '.--', 'ه': '..-', 'ی': '..--'
}

# Function to convert text to Persian Morse code
def text_to_persian_morse(text):
    morse = ''
    for char in text:
        if char in persian_morse_code:
            morse += persian_morse_code[char] + ' '
    return morse.strip()

# Function to convert Persian Morse code to text
def persian_morse_to_text(morse):
    text = ''
    morse_list = morse.split(' ')
    for code in morse_list:
        for key, value in persian_morse_code.items():
            if code == value:
                text += key
    return text

# Event handler for encoding button
def encode():
    text = entry.get()
    morse = text_to_persian_morse(text)
    output.delete(1.0, tk.END)
    output.insert(tk.END, morse)

# Event handler for decoding button
def decode():
    morse = entry.get()
    text = persian_morse_to_text(morse)
    output.delete(1.0, tk.END)
    output.insert(tk.END, text)

# Creating the tkinter window
window = tk.Tk()
window.title("Persian Morse Code Converter")

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
