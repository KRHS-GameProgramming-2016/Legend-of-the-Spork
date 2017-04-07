import pygame, sys, math

class Tiles():
    def __init__(self, kind, pos=[0,0], size=None, self.containers):
        if version = "grass":
            self.image = pygame.image.load("Res/Tiles/Grass.png")
        elif version = "path":
            self.image = pygame.image.load("Res/Tiles/StonePath.png")
        elif version = "sand":
            self.image = pygame.image.load("Res/Tiles/Sand.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
