import pygame, sys, math

class Impassables(pygame.sprite.Sprite):
    def __init__(self, impass, pos=[0,0], size=None):
        self.impass = impass
        pygame.sprite.Sprite.__init__(self, self.containers)
        if self.impass == "river":
            self.image = pygame.image.load("Res/ImpassableObj/BrightWater.png")
        elif self.impass == "boulder":
            self.image = pygame.image.load("Res/ImpassableObj/Boulder.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
