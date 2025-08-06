MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S':'...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

def translate(text, mode):
  """
  Translates text to/from Morse code.

  Args:
      text: The text to translate.
      mode: 'to_morse' or 'from_morse' depending on translation direction.

  Returns:
      The translated text in Morse code or English.
  """
  if mode == 'to_morse':
    result = ' '.join(MORSE_CODE.get(char.upper(), '?') for char in text)
  elif mode == 'from_morse':
    # Split the Morse code into individual characters
    morse_characters = text.split()
    # Convert each Morse character to its corresponding letter
    result = ''.join(key for key, value in MORSE_CODE.items() if value == morse_character for morse_character in morse_characters)
  else:
    print("Invalid mode. Please specify 'to_morse' or 'from_morse'.")
    return
  return result

# Main program loop
while True:
  print("Morse Code Translator")
  print("1. Text to Morse Code")
  print("2. Morse Code to Text")
  print("3. Exit")
  choice = input("Enter your choice (1-3): ")

  if choice == '1':
    text = input("Enter text to convert: ")
    morse_code = translate(text, 'to_morse')
    print(f"Morse Code: {morse_code}")
  elif choice == '2':
    morse_code = input("Enter Morse code to convert: ")
    text = translate(morse_code, 'from_morse')
    print(f"Text: {text}")
  elif choice == '3':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")
