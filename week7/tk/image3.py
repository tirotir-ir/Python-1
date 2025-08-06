#import the tkinter library in the notebook

from tkinter import *
#creating an instance of the tkinter canvas
win= Tk()
#define the size of the window
win.geometry("700x150")

#define the image label having some properties

label_img= Label(win, text= "Hello World", font= "sans-serif",relief=
"solid",width= 20, height= 8, anchor= CENTER)
label_img.pack()
#displaying the canvas without closing the window
win.mainloop()