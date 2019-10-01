
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 50
height = 50
vel = 10

isJump = False

jump_count = 10



run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LCTRL]:#increasing the velocity
        vel = 30
    else:
        vel = 10

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - width - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            isJump = False
            jump_count = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

