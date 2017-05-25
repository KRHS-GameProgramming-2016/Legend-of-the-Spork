import pygame, math, pygame, random

class Spork(pygame.sprite.Sprite):
    def __init__(self, size = 64, pos = [0, 0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load("Res/Background/Spork.png"), [size, size])

        self.rect = self.image.get_rect(center = pos)
