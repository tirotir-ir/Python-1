import time
import sys
from termcolor import colored

def color_animation(text, colors, delay=0.2):
    for color in colors:
        sys.stdout.write('\r' + colored(text, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
for _ in range(5):
    color_animation("Hello, World!", colors)
