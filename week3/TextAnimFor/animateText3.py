import time
import os
import sys

def moving_text(text, width=50, delay=0.1):
    space = ' ' * width
    for i in range(width + len(text)):
        sys.stdout.write('\r' + space + text[:i])
        sys.stdout.flush()
        time.sleep(delay)
        text = text[-1] + text[:-1]

moving_text("Hello, World!")
