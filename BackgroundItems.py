import pygame, sys, math

class BackgroundItems(pygame.sprite.Sprite):
    def __init__(self, passable, pos=[0,0], size=None):
        self.passable = passable
        pygame.sprite.Sprite.__init__(self, self.containers)
        if self.passable == "bench":
            self.image == pygame.image.load("Res/Background/Bench.png")
        elif self.passable == "tree":
            self.image = pygame.image.load("Res/Background/Tree.png")
        if size:
            self.image == pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
