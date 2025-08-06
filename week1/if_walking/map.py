#izehmap
import tkinter as tk
from tkintermapview import TkinterMapView

# Create a root window
root = tk.Tk()
root.title("Simple Map")
root.geometry("800x600")

# Create a map widget
map_widget = TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Set the starting position (latitude and longitude)
map_widget.set_position(37.7749, -122.4194)  # San Francisco coordinates
map_widget.set_zoom(10)  # Set zoom level

# Run the Tkinter loop
root.mainloop()

# Practical Exercise 1:
# Modify the code to add a marker at a specific location on the map.

# Guidelines:
# 1. Use the add_marker method of the map_widget.
# 2. Provide the latitude and longitude for the marker.

# Practical Exercise 2:
# Modify the code to change the map type to satellite view.

# Guidelines:
# 1. Use the set_map_type method of the map_widget.
# 2. Set the map type to 'satellite'.

# Practical Exercise 3:
# Modify the code to allow the user to input coordinates and update the map position.

# Guidelines:
# 1. Use the input() function to get latitude and longitude from the user.
# 2. Update the map position using the set_position method.

# Practical Exercise 4:
# Modify the code to add a button that resets the map to the original position.

# Guidelines:
# 1. Create a button widget.
# 2. Define a function that sets the map position back to the original coordinates.
# 3. Bind the button to the function.

# Practical Exercise 5:
# Modify the code to display the current coordinates of the map center in a label.

# Guidelines:
# 1. Create a label widget.
# 2. Use the get_position method of the map_widget to get the current coordinates.
# 3. Update the label text with the coordinates.

# Questions:
# 1. How can you change the zoom level of the map programmatically?
# 2. What method would you use to add multiple markers on the map?
# 3. How can you handle exceptions that may occur during map operations?


'''
import tkinter as tk
from tkintermapview import TkinterMapView

# Create a root window
root = tk.Tk()
root.title("Simple Map")
root.geometry("800x600")

# Create a map widget
map_widget = TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Set the starting position (latitude and longitude)
map_widget.set_position(37.7749, -122.4194)  # San Francisco coordinates
map_widget.set_zoom(10)  # Set zoom level

# Add a marker
map_widget.add_marker(37.7749, -122.4194, text="San Francisco")

# Run the Tkinter loop
root.mainloop()
'''



'''
import tkinter as tk
from tkintermapview import TkinterMapView

# Create a root window
root = tk.Tk()
root.title("Simple Map")
root.geometry("800x600")

# Create a map widget
map_widget = TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Set the starting position (latitude and longitude)
map_widget.set_position(37.7749, -122.4194)  # San Francisco coordinates
map_widget.set_zoom(10)  # Set zoom level

# Change map type to satellite
map_widget.set_map_type("satellite")

# Run the Tkinter loop
root.mainloop()
'''



'''
import tkinter as tk
from tkintermapview import TkinterMapView

# Create a root window
root = tk.Tk()
root.title("Simple Map")
root.geometry("800x600")

# Create a map widget
map_widget = TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Function to update map position
def update_position():
    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))
    map_widget.set_position(lat, lon)

# Set the starting position (latitude and longitude)
map_widget.set_position(37.7749, -122.4194)  # San Francisco coordinates
map_widget.set_zoom(10)  # Set zoom level

# Update map position based on user input
update_position()

# Run the Tkinter loop
root.mainloop()
'''



'''
import tkinter as tk
from tkintermapview import TkinterMapView

# Create a root window
root = tk.Tk()
root.title("Simple Map")
root.geometry("800x600")

# Create a map widget
map_widget = TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Set the starting position (latitude and longitude)
original_lat, original_lon = 37.7749, -122.4194  # San Francisco coordinates
map_widget.set_position(original_lat, original_lon)
map_widget.set_zoom(10)  # Set zoom level

# Function to reset map position
def reset_position():
    map_widget.set_position(original_lat, original_lon)

# Add a reset button
reset_button = tk.Button(root, text="Reset Position", command=reset_position)
reset_button.pack()

# Run the Tkinter loop
root.mainloop()
'''




'''
import tkinter as tk
from tkintermapview import TkinterMapView

# Create a root window
root = tk.Tk()
root.title("Simple Map")
root.geometry("800x600")

# Create a map widget
map_widget = TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Set the starting position (latitude and longitude)
map_widget.set_position(37.7749, -122.4194)  # San Francisco coordinates
map_widget.set_zoom(10)  # Set zoom level

# Create a label to display coordinates
coord_label = tk.Label(root, text="")
coord_label.pack()

# Function to update label with current coordinates
def update_label():
    lat, lon = map_widget.get_position()
    coord_label.config(text=f"Latitude: {lat}, Longitude: {lon}")

# Update label initially
update_label()

# Run the Tkinter loop
root.mainloop()
'''