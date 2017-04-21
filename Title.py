import pygame, sys, math, random

class Title(pygame.sprite.Sprite):
    def __init__(self, image, size):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = size
        self.image = pygame.image.load(image)
        
        if size:
            self.image = pygame.transform.scale(self.image, size)
        
        self.rect = self.image.get_rect()
