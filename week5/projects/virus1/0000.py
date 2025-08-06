import time
import sys

def print_colored_text(text, color_code):
    sys.stdout.write(f"\033[{color_code}m{text}\033[0m")
    sys.stdout.flush()

def virus_simulation():
    colors = ['31', '32', '33', '34', '35', '36']  # Red, Green, Yellow, Blue, Magenta, Cyan
    print("Virus simulation starting...")
    time.sleep(2)
    
    for i in range(10):  # Change color 10 times
        color = colors[i % len(colors)]
        print_colored_text("This is a harmless, funny simulation of a virus spreading!\n", color)
        time.sleep(0.5)  # Simulate some delay

if __name__ == "__main__":
    virus_simulation()
