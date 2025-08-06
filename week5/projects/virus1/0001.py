import os

def create_fake_virus():
    # Get the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Define folder and file paths
    folder_path = os.path.join(desktop_path, "virus")
    file_path = os.path.join(folder_path, "message.txt")
    
    # Create the folder
    os.makedirs(folder_path, exist_ok=True)
    
    # Write a message to the text file
    with open(file_path, 'w') as file:
        file.write("Give your money ha ha ha!!!")
    
    print("Fake virus created on the desktop.")

if __name__ == "__main__":
    create_fake_virus()
