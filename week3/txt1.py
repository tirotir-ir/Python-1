import time

text = input('Enter any word: ')

for letter in text:
    print(letter, end='', flush=True)
    time.sleep(1)

