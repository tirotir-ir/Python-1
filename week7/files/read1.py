import os

current_dir = os.path.dirname(__file__)  # Get the directory of your script
file_path = os.path.join(current_dir, 'file.txt')  # Combine with filename

#with open(os.path.join(os.path.dirname(__file__), 'file.txt'), 'r') as file:
with open(file_path, 'r') as file:
        content = file.read()
print(content)