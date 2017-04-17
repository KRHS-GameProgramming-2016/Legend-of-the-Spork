import sys, math, random

class Titlescreen(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = screenSize
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.Title = False
        self.screen = 1
        
        if self.screen == 1:
            pygame.image.load("Res/Background/Titlescreen1.png")
        else:
            pygame.image.load("Res/Background/Titlescreen2.png")
    
    
