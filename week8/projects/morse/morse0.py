# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ' ': '/'
}

# Reverse Morse code dictionary
reverse_morse_code = {v: k for k, v in morse_code.items()}

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
        if code in reverse_morse_code:
            text += reverse_morse_code[code]
    return text

# Function to handle user input and conversion
def convert():
    choice = input("Enter 'm' to convert Morse code to text, or 't' to convert text to Morse code: ")
    if choice.lower() == 'm':
        morse_input = input("Enter Morse code: ")
        text_output = morse_to_text(morse_input)
        print("Decoded Text:", text_output)
    elif choice.lower() == 't':
        text_input = input("Enter text: ")
        morse_output = text_to_morse(text_input)
        print("Encoded Morse Code:", morse_output)
    else:
        print("Invalid choice. Please enter 'm' or 't'.")

# Main function
def main():
    convert()

if __name__ == "__main__":
    main()
