from PIL import Image
print("Walking, Running or Biking?!")
speed = int(input("Please enter a number between(1-20): "))

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

print(status)
