# ❌ Without classes: making two cars gets messy fast.

# Car 1
car1_brand = "Toyota"
car1_color = "Red"

def drive_car1():
    return f"The {car1_color} {car1_brand} is driving."

def stop_car1():
    return f"The {car1_color} {car1_brand} stopped."

# Car 2
car2_brand = "BMW"
car2_color = "Black"

def drive_car2():
    return f"The {car2_color} {car2_brand} is driving."

def stop_car2():
    return f"The {car2_color} {car2_brand} stopped."

if __name__ == "__main__":
    print(drive_car1())
    print(stop_car2())
    # Imagine adding Car 3, 4, 5... we'd repeat all this again.