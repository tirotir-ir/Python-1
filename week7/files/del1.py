import os

current_dir = os.path.dirname(__file__)  # Get the directory of your script
file_path = os.path.join(current_dir, 'file2.txt')  # Combine with filename

if os.path.exists(file_path):
    os.remove(file_path)
    print(f'{file_path} has been deleted.')
else:
    print(f'{file_path} does not exist.')
