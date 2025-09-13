# ✅ With classes: one blueprint, many cars (Factory analogy).

class Car:
    def __init__(self, brand, color):
        # attributes (data)
        self.brand = brand
        self.color = color

    # methods (actions)
    def drive(self):
        return f"The {self.color} {self.brand} is driving."

    def stop(self):
        return f"The {self.color} {self.brand} stopped."

if __name__ == "__main__":
    car1 = Car("Toyota", "Red")
    car2 = Car("BMW", "Black")

    print(car1.drive())
    print(car2.stop())