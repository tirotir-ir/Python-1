# Open a file in write mode (it will create the file if it doesn't exist)
with open('hello_world2.txt', 'w') as file:
    # Write "Hello, World!" to the file
    a=input('type to file: ')
    file.write(a)
