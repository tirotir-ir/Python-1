#pip install termcolor
from termcolor import colored
from colorama import init
init()

print(colored('Hello, World!', 'green'))
print(colored('Hello, World!', 'red', 'on_blue', ['bold', 'blink']))