import pygame, sys
pygame.init()

clock = pygame.time.Clock()

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Race Game")

class ROCKET:
    def __init__(self):
        self.rocketImg = pygame.image.load("code/roket.png")
        self.rocket_x = screen_width/2 - 32
        self.rocket_y = screen_height/2 + 100

    def draw_rocket(self):
        screen.blit(self.rocketImg, (self.rocket_x, self.rocket_y))

    def move_rocket(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rocket_x + 15 > 0:
            self.rocket_x -= 5

        if key[pygame.K_RIGHT] and self.rocket_x < screen_width - 40:
            self.rocket_x += 5

class BULLET(ROCKET):
    def __init__(self):
        super().__init__()
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_x = self.rocket_x + 25
        self.bullet_y = self.rocket_y
        self.move = [0, 0]
        self.bullet_speed = 5
        self.bullet_rect = pygame.Rect(self.bullet_x, self.bullet_y, self.bullet_width, self.bullet_height)

    def draw_bullet(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.move[1] == 0:
            rocket_center_x = rocket.rocket_x + self.rocketImg.get_width() // 2 
            self.bullet_x = rocket_center_x - self.bullet_width // 2
            self.move[1] = -1

        self.bullet_y += self.move[1] * self.bullet_speed
        self.bullet_rect.topleft = (self.bullet_x, self.bullet_y)

        if self.bullet_y < self.rocket_y - 10:
            pygame.draw.rect(screen, (0, 0, 0), self.bullet_rect)

        if self.bullet_y < - 20:
            self.bullet_y = self.rocket_y
            self.move[1] = 0

rocket = ROCKET()
bullet = BULLET()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    rocket.draw_rocket()
    rocket.move_rocket()
    bullet.draw_bullet()


    pygame.display.flip()
    clock.tick(60)