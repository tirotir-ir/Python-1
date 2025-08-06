import time
import winsound

a = 0

for i in range(10):
    print(a) 
    winsound.Beep(1000, 200)  
    a += 1   
    time.sleep(1)  