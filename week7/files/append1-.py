import os

current_dir = os.path.dirname(__file__)  # Get the directory of your script
file_path = os.path.join(current_dir, 'file.txt')  # Combine with filename

# Open the file in append mode
with open(file_path, 'a') as file:
    while True:
        user_input = input("message ('q'= quit): ")
        if user_input.lower() == 'q':
            break
        file.write(user_input + '\n')

print("saved to 'file.txt'.")
