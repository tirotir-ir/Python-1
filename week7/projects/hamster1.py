import pygame
import random

# مقداردهی اولیه pygame
pygame.init()

# تنظیمات صفحه نمایش
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hamster Game")

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# تنظیمات همستر
hamster_width, hamster_height = 50, 50
hamster_x, hamster_y = WIDTH // 2, HEIGHT // 2
hamster_speed = 5

# تنظیمات دشمن
enemy_width, enemy_height = 50, 50
enemy_x, enemy_y = random.randint(0, WIDTH-enemy_width), random.randint(0, HEIGHT-enemy_height)
enemy_speed = 3

# تنظیمات امتیاز
score = 0
font = pygame.font.SysFont(None, 35)

# تابع رسم امتیاز
def draw_score(score):
    text = font.render("Score: " + str(score), True, BLACK)
    win.blit(text, [10, 10])

# حلقه اصلی بازی
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hamster_x - hamster_speed > 0:
        hamster_x -= hamster_speed
    if keys[pygame.K_RIGHT] and hamster_x + hamster_speed < WIDTH - hamster_width:
        hamster_x += hamster_speed
    if keys[pygame.K_UP] and hamster_y - hamster_speed > 0:
        hamster_y -= hamster_speed
    if keys[pygame.K_DOWN] and hamster_y + hamster_speed < HEIGHT - hamster_height:
        hamster_y += hamster_speed

    # حرکت دشمن
    if hamster_x < enemy_x:
        enemy_x -= enemy_speed
    elif hamster_x > enemy_x:
        enemy_x += enemy_speed

    if hamster_y < enemy_y:
        enemy_y -= enemy_speed
    elif hamster_y > enemy_y:
        enemy_y += enemy_speed

    # برخورد با دشمن
    if abs(hamster_x - enemy_x) < hamster_width and abs(hamster_y - enemy_y) < hamster_height:
        score += 1
        enemy_x, enemy_y = random.randint(0, WIDTH-enemy_width), random.randint(0, HEIGHT-enemy_height)

    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, (hamster_x, hamster_y, hamster_width, hamster_height))
    pygame.draw.rect(win, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    draw_score(score)
    pygame.display.update()

pygame.quit()
