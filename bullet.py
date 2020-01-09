import pygame

from random import randint

BLACK = (0,0,0)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0,width, height])

        self.velocity = [0, 0]

        self.rect = self.image.get_rect()
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)


    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def fire(self):
        if self.velocity[1] == 0:
            self.velocity[1] = -5

    def notfire(self):
        self.rect.x = 400
        self.rect.y = 700
        self.velocity[1] = 0
