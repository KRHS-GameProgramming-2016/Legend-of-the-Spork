import pygame, sys, math, time

class Player(pygame.sprite.Sprite):
    def __init__(self, size = [64, 64], maxSpeed = 5, speed = [0, 0], pos = [0, 64]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.imageLeft  = pygame.image.load("")
        self.imageRight = pygame.image.load("")
        self.imageUp = pygame.image.load("")
        self.imageDown = pygame.image.load("")
        #self.imagesLeft = pygame.image.load(
        #self.imagesRight = pygame.image.load(
        #self.imagesUp = pygame.image.load(
        #self.imagesDown = pygame.image.load(
        self.size = size
        
        self.state = "right"
        self.prevState = "right"
        self.imageState = "right"
        self.image = self.imageRight
        self.rect = self.image.get_rect()
        
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.didBounceX = False
        self.didBounceY = False
        self.pos = [self.rect.left, self.rect.top]
        self.lives = 5
        self.hit = False
        self.health = 3
        self.maxSpeed = maxSpeed 
        
        #self.frame = 0
        #self.maxFrame = len(self.images) - 1
        #self.animationTimer = 0
        #self.animationTimerMax = .2 * 60 #seconds * 60 fps
        #self.blinkFrame = 0
    def animate(self):
        if self.prevState != self.state:
            if self.state == "right":
                self.image == self.imageRight
                #self.image = self.imagesRight
            elif self.state == "left":
                self.image == self.imageLeft
                #self.image = self.imagesLeft
            elif self.state == "up":
                self.image == self.imageUp
                #self.image = self.imagesUp
            elif self.state == "down":
                self.image == self.imageDown
                #self.image = self.imagesDown
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.animate()
    def direction(direction):
        return direction
    def go(self, direction):
        if direction == "right":
            self.speedx = self.speedx
            self.speedy = 0
            self.state == "right"
            self.move()
        if direction == "left":
            self.speedx == -self.speedx
            self.speedy = 0
            self.state == "left"
            self.move()
        if direction == "up":
            self.speedx = 0
            self.speedy = self.speedy
            self.state == "up"
            self.move()
        if direction == "down":
            self.speedx = 0
            self.speedy = -self.speedy
            self.state == "down"
            self.move()
            
        if direction == "stop up":
            self.speedy = 0
            self.prevState = "up"
        if direction == "stop down":
            self.speedy = 0
            self.prevState = "down"
        if direction == "stop left":
            self.speedx = 0
            self.prevState = "left"
        if direction == "stop right":
            self.speedx = 0
            self.prevState = "right"
            
            
    def dist(self, pt):
        x = pt[0] - self.rect.right
        y = pt[1] - self.rect.bottom
        if x < 0:
            x += -64
            x += x
        if y < 0:
            y += -64
            y += y
        return [x, y]
        
    def screenCollide(self, screenSize):
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        if self.rect.top < 0 or self.rect.bottom > screenHeight:
            self.speedy = 0
        if self.rect.left < 0 or self.rect.right > screenHeight:
            self.speedx = 0
