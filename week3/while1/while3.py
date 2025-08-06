import time
import winsound

x = 1
while x <= 5:
    print(x)
    x += 1
    time.sleep(1)
    winsound.Beep(1000, 200)
