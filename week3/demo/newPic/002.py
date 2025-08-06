#pip install pillow
from PIL import Image

print("Lotfan, entexab konid:")
print("1. Arme edare Bargh")
print("2.Arme Bank")
print("3.marde Parti")

#a = int(input("Please enter: 1 or 2 or 3: "))
a = int(input(''))
if a==1:
  img = Image.open('bargh.jpg')
elif a==2:
  img = Image.open('bmi.jpg')
elif a==3:
  img = Image.open('part.jpg')
else:
  print("Bye!")

img.show()
