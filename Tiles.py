import pygame, sys, math

class Tiles(pygame.sprite.Sprite):
    def __init__(self, version, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.version = version
        if self.version == "grass":
            self.image = pygame.image.load("Res/Tiles/Grass.png")
        elif self.version == "path":
            self.image = pygame.image.load("Res/Tiles/StonePath.png")
        elif self.version == "sand":
            self.image = pygame.image.load("Res/Tiles/Sand.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
