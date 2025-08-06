def greet(name, age):
    try:
        age = int(age)
        if age < 13:
            age_group = "child"
        elif 13 <= age < 20:
            age_group = "teenager"
        else:
            age_group = "adult"
        print(f"Hello, {name}! You are a {age_group}.")
    except ValueError:
        print("Please enter a valid age.")

name = input("Enter your name: ")
age = input("Enter your age: ")
greet(name, age)
