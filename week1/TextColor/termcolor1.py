#pip install termcolor
from termcolor import colored
from colorama import init
init()

print(colored('Hello, World!', 'green'))

print(colored('Hello, World!', 'red', attrs=['bold', 'underline']))

print(colored('Hello, World!', 'cyan', attrs=['blink']))

print(colored('Hello, World!', 'green', attrs=['reverse']))

print(colored('Hello, World!', 'grey', attrs=['concealed']))

print(colored('Hello, World!', 'red', attrs=['bold', 'underline', 'reverse']))


colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
for color in colors:
    print(colored('Hello, World!', color))


def print_colored(text, color, attrs=None):
    print(colored(text, color, attrs=attrs))

print_colored('Hello, World!', 'blue', ['bold'])
print_colored('Hello, World!', 'yellow', ['underline'])
print_colored('Hello, World!', 'magenta', ['reverse'])
