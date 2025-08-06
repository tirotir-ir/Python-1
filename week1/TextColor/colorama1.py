#pip install colorama
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"salam "+ Fore.YELLOW+ Back.BLUE+"tirotir")
print(Back.CYAN+"Izeh")
print(Fore.RED + Back.GREEN+ "Iran")