#pip install windows-curses

import time
import winsound
import curses

# Initialize the screen
stdscr = curses.initscr()
curses.start_color()

# Define a list of colors
colors = [curses.COLOR_RED, curses.COLOR_GREEN, curses.COLOR_YELLOW, curses.COLOR_BLUE, curses.COLOR_MAGENTA, curses.COLOR_CYAN]

# Start of the loop
for a in range(10):
    # Set the color pair
    curses.init_pair(a + 1, colors[a % len(colors)], curses.COLOR_BLACK)
    
    # Add the string with color
    stdscr.addstr(0, 0, str(a), curses.color_pair(a + 1))
    stdscr.refresh()
    
    # Add a beep sound with frequency changing based on 'a'
    winsound.Beep(1000 + a * 100, 200)  # Frequency is 1000 + a*100, duration is 200 ms.
    
    time.sleep(1)  # Wait for 1 second

# End the window
curses.endwin()
