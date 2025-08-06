import time
import sys
from termcolor import colored

def typing_effect_colored(text, colors, delay=0.1):
    color_index = 0
    for char in text:
        sys.stdout.write(colored(char, colors[color_index]))
        sys.stdout.flush()
        time.sleep(delay)
        color_index = (color_index + 1) % len(colors)
    print()  # Move to the next line

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
typing_effect_colored("Hello, World!", colors)
