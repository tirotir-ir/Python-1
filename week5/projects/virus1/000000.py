import time
import random

def random_ascii_art():
    art = [
        """
        (\_/)
        (o.o)
        (> <)
        """,
        """
        (¬_¬)
        """,
        """
        (•_•)
        ( •_•)>⌐■-■
        (⌐■_■)
        """,
        """
        (✿◠‿◠)
        """
    ]
    return random.choice(art)

def virus_simulation():
    print("Virus simulation starting...")
    time.sleep(2)
    
    for _ in range(5):  # Display 5 random ASCII arts
        print(random_ascii_art())
        time.sleep(1)  # Simulate some delay

if __name__ == "__main__":
    virus_simulation()
