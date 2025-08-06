#Import the Tkinter library
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
#Create an instance of Tkinter frame
win= Tk()
#Define the geometry
win.geometry("750x350")
win.title("Image Gallery")
def select_file():
   path= filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','*.jpg'),('all files','*.*')))
   img= Image.open(path)
   img=ImageTk.PhotoImage(img)
   label= Label(win, image= img)
   label.image= img
   label.pack()
#Create a label and a Button to Open the dialog
Label(win, text="Click the Button below to select an Image", font=('Caveat 15 bold')).pack(pady=20)
button= ttk.Button(win, text="Select to Open", command= select_file)
button.pack(ipadx=5, pady=15)
win.mainloop()