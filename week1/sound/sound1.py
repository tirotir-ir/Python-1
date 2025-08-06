import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load and play the sound
pygame.mixer.music.load(r'E:\PYTHON\Term1\pythonWeeks1\week1\sound\alivesound.mp3')
pygame.mixer.music.play()

# Keep the program running until the music finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
