from tkinter import *
from tkinter import messagebox

def check():
    username = e1.get()
    password = e2.get()
    if username == "admin" and password == "123":
        messagebox.showinfo("Login Successful", "Welcome!")
    
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

top = Tk()
top.geometry("400x250")

uname_label = Label(top, text="Username")
uname_label.place(x=30, y=50)

password_label = Label(top, text="Password")
password_label.place(x=30, y=90)

e1 = Entry(top, width=20)
e1.place(x=100, y=50)

e2 = Entry(top, width=20, show='*')
e2.place(x=100, y=90)

sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue", command=check)
sbmitbtn.place(x=30, y=120)

top.mainloop()
