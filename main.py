import pygame
import sys


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # duplicate the image to avoid losing resolution
        # when rotating it (pygame issues)
        self.original_image = pygame.image.load('Audi.png')
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(640, 360))
        self.angle = 0
        self.rotation_speed = 1.8
        self.direction = 0
        # forward is the direction
        self.forward = pygame.math.Vector2(0, -1)  # default is upwards
        self.active = False

    def set_rotation(self):
        if self.direction == 1:
            self.angle -= self.rotation_speed
        if self.direction == -1:
            self.angle += self.rotation_speed

        self.image = pygame.transform.rotozoom(
            self.original_image, self.angle, 0.25)
        self.rect = self.image.get_rect(center=self.rect.center)

    def get_rotation(self):
        # rotate_ip = rotate in place
        if self.direction == 1:
            self.forward.rotate_ip(self.rotation_speed)
        if self.direction == -1:
            self.forward.rotate_ip(-self.rotation_speed)

    def accelerate(self):
        if self.active:
            self.rect.center += self.forward * 5

    def update(self):
        self.set_rotation()
        self.get_rotation()
        self.accelerate()


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

bg_track = pygame.image.load('Track.png')

car = pygame.sprite.GroupSingle(Car())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car.sprite.direction += 1
            if event.key == pygame.K_LEFT:
                car.sprite.direction -= 1
            if event.key == pygame.K_SPACE:
                car.sprite.active = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car.sprite.direction -= 1
            if event.key == pygame.K_LEFT:
                car.sprite.direction += 1
            if event.key == pygame.K_SPACE:
                car.sprite.active = False

    screen.blit(bg_track, (0, 0))
    car.update()
    car.draw(screen)
    pygame.display.update()
    clock.tick(120)
