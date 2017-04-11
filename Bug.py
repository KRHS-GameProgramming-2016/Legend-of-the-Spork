import pygame, sys, math, random

class Bug(pygame.sprite.Sprite):
    def __init__(self, speed=0, pos=[0,0], size=64):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.imagesLeft = [pygame.transform.scale(pygame.image.load("Res/Enemies/Bug1.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/Bug2.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/Bug3.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/Bug4.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/Bug5.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/Bug6.png"), [self.size,self.size])]
        
        self.maxSpeed = speed
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.state = "right"
        self.prevState = "right"
        
        self.frame = 0
        self.animationTimer = 0
        self.animationTimerMax = .3 * 60 #seconds * 60 fps
        self.images = self.imagesRight
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxFrame = len(self.images) - 1
        
        
        
        self.hit = False
