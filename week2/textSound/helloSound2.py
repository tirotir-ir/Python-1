import subprocess

# The text you want eSpeak to say
text = "Hello, world!"

# Command to run eSpeak
command = ['espeak', text]

# Run the command
subprocess.run(command)