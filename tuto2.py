
import pygame
pygame.init()
pygame.font.init()

font = pygame.font.Font('freesansbold.ttf', 32)

win = pygame.display.set_mode((500, 480)) # window
pygame.display.set_caption("First Game")

blue = (0, 0, 128)
green = (0, 255, 0)



walkRight = [pygame.image.load('Pygame-Images/Game/R1.png'), pygame.image.load('Pygame-Images/Game/R2.png'), pygame.image.load('Pygame-Images/Game/R3.png'), pygame.image.load('Pygame-Images/Game/R4.png'), pygame.image.load('Pygame-Images/Game/R5.png'), pygame.image.load('Pygame-Images/Game/R6.png'), pygame.image.load('Pygame-Images/Game/R7.png'), pygame.image.load('Pygame-Images/Game/R8.png'), pygame.image.load('Pygame-Images/Game/R9.png')]
walkLeft = [pygame.image.load('Pygame-Images/Game/L1.png'), pygame.image.load('Pygame-Images/Game/L2.png'), pygame.image.load('Pygame-Images/Game/L3.png'), pygame.image.load('Pygame-Images/Game/L4.png'), pygame.image.load('Pygame-Images/Game/L5.png'), pygame.image.load('Pygame-Images/Game/L6.png'), pygame.image.load('Pygame-Images/Game/L7.png'), pygame.image.load('Pygame-Images/Game/L8.png'), pygame.image.load('Pygame-Images/Game/L9.png')]
bg = pygame.image.load('Pygame-Images/Game/bg1.jpg')
char = pygame.image.load('Pygame-Images/Game/standing.png')


#bullet_sound = pygame.mixer.Sound('bullet.wav')
#hit_sound = pygame.mixer.Sound('hit.wav')

music = pygame.mixer.music.load('Pygame-Images/Game/music.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
score = 0
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jump_count = 10
        self.right = False
        self.left = False
        self.walk_count = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(walkRight[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jump_count = 10
        self.x = 60
        self.y = 410
        self.walk_count = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()




class enemy(object):
    walkRight = [pygame.image.load('Pygame-Images/Game/R1E.png'), pygame.image.load('Pygame-Images/Game/R2E.png'), pygame.image.load('Pygame-Images/Game/R3E.png'),
                 pygame.image.load('Pygame-Images/Game/R4E.png'), pygame.image.load('Pygame-Images/Game/R5E.png'), pygame.image.load('Pygame-Images/Game/R6E.png'),
                 pygame.image.load('Pygame-Images/Game/R7E.png'), pygame.image.load('Pygame-Images/Game/R8E.png'), pygame.image.load('Pygame-Images/Game/R9E.png'),
                 pygame.image.load('Pygame-Images/Game/R10E.png'), pygame.image.load('Pygame-Images/Game/R11E.png')]
    walkLeft = [pygame.image.load('Pygame-Images/Game/L1E.png'), pygame.image.load('Pygame-Images/Game/L2E.png'), pygame.image.load('Pygame-Images/Game/L3E.png'),
                pygame.image.load('Pygame-Images/Game/L4E.png'), pygame.image.load('Pygame-Images/Game/L5E.png'), pygame.image.load('Pygame-Images/Game/L6E.png'),
                pygame.image.load('Pygame-Images/Game/L7E.png'), pygame.image.load('Pygame-Images/Game/L8E.png'), pygame.image.load('Pygame-Images/Game/L9E.png'),
                pygame.image.load('Pygame-Images/Game/L10E.png'), pygame.image.load('Pygame-Images/Game/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]  # This will define where our enemy starts and finishes their path.
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 9
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:  # Since we have 11 images for each animtion our upper bound is 33.
                # We will show each image for 3 frames. 3 x 11 = 33.
                self.walkCount = 0

            if self.vel > 0:  # If we are moving to the right we will display our walkRight images
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:  # Otherwise we will display the walkLeft images
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1]-20, 50, 10))  # health bar red
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1]-20, 50 - (5*(10 - self.health)), 10) )  # health bar green

            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2 )

    def move(self):
        if self.vel > 0:  # If we are moving right
            if self.x + self.vel < self.path[1] :  # If we have not reached the furthest right point on our path.
                self.x += self.vel
            else:  # Change direction and move back the other way
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:  # If we are moving left
            if self.x - self.vel > self.path[0]:  # If we have not reached the furthest left point on our path
                self.x += self.vel
            else:  # Change direction
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):
        print("hit")
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redraw_game_window():
    win.blit(bg, (0, 0))
    text = font.render(" Score : "+str(score), 1, (0, 0, 0))
    win.blit(text, (370 , 10))
    man.draw(win)
    goblin.draw(win)
    font2 = pygame.font.SysFont('comicsans', 30, True)
    myname = font2.render("powered by chemsou", 1, green, blue )
    win.blit(myname, (20, 20))


    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# MAINLOOP
# variables

font = pygame.font.SysFont('comicsans', 30, True)

man = player(300, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
bullets = []
shoot_loop = 0

run = True
while run:  # loop

    clock.tick(27)

    if goblin.visible:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                # hit_sound.play()
                man.hit()
                score -= 5

    if shoot_loop > 0:  # this statement is to space the bullet shots
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:  # the loop to hit the goblin
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and\
                bullet.y + bullet.radius > goblin.hitbox[1]:

            if goblin.hitbox[0] < bullet.x + bullet.radius and\
                    bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                # hit_sound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot_loop == 0:
        # bullet_sound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(man.x + man.width // 2, round(man.y + man.height // 2), 6, (0, 0, 0), facing))
            shoot_loop = 1

    if keys[pygame.K_LCTRL]:  # increasing the velocity
        man.vel = 30
    else:
        man.vel = 10

    if keys[pygame.K_LEFT] and man.x > man .vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False

    else:
        man.standing = True
        man.walk_count = 0

    if not man.isJump:

        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walk_count = 0
    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2) * 0.5 * neg
            man.jump_count -= 1
        else:
            man.isJump = False
            man.jump_count = 10

    redraw_game_window()
pygame.quit()

