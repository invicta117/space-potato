import pygame
import os
BLACK = (0, 0, 0)


class DEF(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.image.load(os.path.join("images","pixil-frame-0(3).png")).convert()
        # self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

    def moveLeft(self, pixels):
        self.rect.x -=pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x >= 650:
            self.rect.x = 650
