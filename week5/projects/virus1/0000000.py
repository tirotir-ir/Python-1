import time
import os

def bounce_animation():
    text = "Bouncing text!"
    width = 40
    padding = 0
    direction = 1

    print("Virus simulation starting...")
    time.sleep(2)

    for _ in range(20):  # Bounce 20 times
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print(' ' * padding + text)
        time.sleep(0.1)  # Simulate some delay
        padding += direction

        if padding >= width - len(text) or padding <= 0:
            direction *= -1  # Change direction

if __name__ == "__main__":
    bounce_animation()
