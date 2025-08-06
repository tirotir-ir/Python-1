import time
import winsound
from termcolor import colored

# Initialize variable 'a'
a = 0

# Define a list of colors
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

# Start of the loop
for i in range(10):
    # Show the current value of 'a' in different colors
    print(colored(a, colors[a % len(colors)]))
    
    # Add a beep sound with frequency changing based on 'a'
    winsound.Beep(1000 + a * 100, 200)  # Frequency is 1000 + a*100, duration is 200 ms.
    
    a += 1    # Increment 'a' by 1
    time.sleep(1)  # Wait for 1 second
