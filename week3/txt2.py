import time

text = input('Enter any word: ')

for letter in reversed(text):
    print(letter, end='', flush=True)
    time.sleep(1)