from tkinter import *

r=Tk()
r.title('tirotir')
r.geometry('400x150')
r.resizable(False, False)
label = Label(r, text='This is a label').place(x=30, y=10)

Button(r, text="ok").pack(side=LEFT, pady=50)

r.mainloop()