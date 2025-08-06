import time
import os
import sys

def blinking_text(text, blink_times=5, delay=0.5):
    for _ in range(blink_times):
        sys.stdout.write(text)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(delay)

blinking_text("Hello, World!")
