# Python program to draw square 
# using Turtle Programming 
import turtle 
skk = turtle.Turtle() 
skk.pensize(4)
skk.shapesize(3,3,3)  
  
skk.pencolor("blue") 
skk.fillcolor("orange")  

# Chnage the color of both  
skk.color("green", "red")  

for i in range(4): 
	skk.forward(50) 
	skk.right(90) 
	
turtle.done() 
