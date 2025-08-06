import os
import random
import ctypes

def set_random_wallpaper():
    # Path to the wallpapers folder
    wallpapers_folder = os.path.join(os.path.expanduser("~"), "Desktop", "wallpapers")
    
    # Get a list of all files in the wallpapers folder
    files = [f for f in os.listdir(wallpapers_folder) if os.path.isfile(os.path.join(wallpapers_folder, f))]
    
    # Choose a random file
    if files:
        random_file = random.choice(files)
        file_path = os.path.join(wallpapers_folder, random_file)
        
        # Set the wallpaper (Windows-specific)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 3)
        
        print(f"Wallpaper changed to {random_file}.")
    else:
        print("No wallpapers found in the specified folder.")

if __name__ == "__main__":
    set_random_wallpaper()
