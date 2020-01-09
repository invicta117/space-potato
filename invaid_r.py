import pygame
from random import randint
import os
BLACK = (0,0,0)


class INVD(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(os.path.join("images","pixil-frame-0(1).png")).convert()
        #self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.velocity = [0, 0]

        self.rect = self.image.get_rect()
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

    def update(self):
        self.rect.x += self.velocity[0]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        #self.velocity[1] = self.velocity[1]

    def move(self):
        self.velocity[0] = 3


