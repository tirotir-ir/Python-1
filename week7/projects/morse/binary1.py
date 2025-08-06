# Function to convert binary to character
def binary_to_char(binary):
    char = chr(int(binary, 2))
    return char

# Function to convert character to binary
def char_to_binary(char):
    binary = bin(ord(char))[2:].zfill(8)
    return binary

# Main function
def main():
    choice = input("Enter 'b' to convert binary to character, or 'c' to convert character to binary: ")
    if choice.lower() == 'b':
        binary = input("Enter binary: ")
        character = binary_to_char(binary)
        print("Corresponding character:", character)
    elif choice.lower() == 'c':
        char = input("Enter a character: ")
        binary = char_to_binary(char)
        print("Binary representation:", binary)
    else:
        print("Invalid choice. Please enter 'b' or 'c'.")

if __name__ == "__main__":
    main()
