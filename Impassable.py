import pygame, sys, math

class Impassables():
    def __init__(self, kind, pos=[0,0], size=None, self.containers):
        if impass = "river":
            self.image = pygame.image.load("Res/Tiles/BrightWater.png")
        elif impass = "boulder":
            self.image = pygame.image.load("Res/Tiles/Boulder.png")
            if size:
                self.image = pygame.transform.scale(self.image, [size,size])
