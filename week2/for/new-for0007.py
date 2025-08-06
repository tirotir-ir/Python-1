import time
import winsound
import random

# Initialize a random target number
target = random.randint(1, 10)

for i in range(10):
    # Ask the user to guess a number
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == target:
        print("Congratulations! You guessed it right.")
        winsound.Beep(2000, 200)  # Play a success sound
        break
    else:
        print("Oops! That's not correct. Try again.")
        winsound.Beep(500, 200)  # Play an error sound
    
    time.sleep(1)  # Wait for 1 second

if guess != target:
    print(f"Sorry, you didn't guess it. The correct number was {target}.")
