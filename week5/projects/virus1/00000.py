import time
import random

def random_message():
    messages = [
        "I'm spreading good vibes!",
        "No harm, just fun!",
        "Catch me if you can!",
        "Spreading smiles, not viruses!",
        "Just a harmless prank!"
    ]
    return random.choice(messages)

def virus_simulation():
    print("Virus simulation starting...")
    time.sleep(2)
    
    for _ in range(5):  # Display 5 random messages
        print(random_message())
        time.sleep(1)  # Simulate some delay

if __name__ == "__main__":
    virus_simulation()
