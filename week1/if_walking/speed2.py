from PIL import Image

def determine_status(speed):
    if speed < 4:
        status = "WALKING"
        img = Image.open('walking.png')
        img.show()
    elif speed < 12:
        status = "RUNNING"
        img = Image.open('running.png')
        img.show()
    else:
        status = "BIKING"
        img = Image.open('biking.png')
        img.show()
    return status

# Example usage
#speed = 3
speed = int(input("Please enter: "))
print(determine_status(speed)) 
