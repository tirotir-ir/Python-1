#izehtk
# Basic Tkinter Window

import tkinter as tk

root = tk.Tk()
root.title('Title')
root.geometry('300x200')
label = tk.Label(root, text='Hello, World!')
label.pack()
label = tk.Label(root, text='Izeh!')
label.pack()

root.mainloop()

# Exercise 1: Change the window title to "My App".
# Question 1: How do you set the title of a Tkinter window?
# Guide: Use the title() method on the root object with the new title as the argument.

# Exercise 2: Modify the window size to 400x300 pixels.
# Question 2: How do you set the size of a Tkinter window?
# Guide: Use the geometry() method on the root object with the new dimensions as the argument.

# Exercise 3: Add a label to the window that says "Hello, Tkinter!".
# Question 3: How do you add a label to a Tkinter window?
# Guide: Use the Label widget and pack() method to add and display the label.

# Exercise 4: Add a button to the window that closes the application when clicked.
# Question 4: How do you add a button to a Tkinter window and bind it to an action?
# Guide: Use the Button widget and the command parameter to bind the button to a function that calls root.destroy().

# Exercise 5: Change the background color of the window to light blue.
# Question 5: How do you change the background color of a Tkinter window?
# Guide: Use the configure() method on the root object with the bg parameter set to the desired color.


'''
label = tk.Label(root, text='Hello, Tkinter!')
label.pack()
'''

'''
import tkinter as tk

def close_application():
    root.destroy()
   
root = tk.Tk()
    
close_button = tk.Button(root, text='Close', command=close_application)
close_button.pack(pady=10)    
'''


'''
root.configure(bg='light blue')  
'''