import pygame, sys, math, time

class Player(pygame.sprite.Sprite):
    def __init__(self,  size = 64, speed=0, maxSpeed = 5, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.imageLeft  = pygame.transform.scale(pygame.image.load("Res/Player/Player side.png"), [size, size])
        self.imageRight = pygame.transform.scale(pygame.image.load("Res/Player/Player side Right.png"), [size, size])
        self.imageUp = pygame.transform.scale(pygame.image.load("Res/Player/Player Back.png"), [size, size])
        self.imageDown = pygame.transform.scale(pygame.image.load("Res/Player/Player.png"), [size, size])
        #self.imagesLeft = pygame.image.load(
        #self.imagesRight = pygame.image.load(
        #self.imagesUp = pygame.image.load(
        #self.imagesDown = pygame.image.load(
        self.size = size

        self.state = "right"
        self.prevState = "right"
        self.imageState = "right"
        self.image = self.imageRight
        self.rect = self.image.get_rect(center = pos)


        self.speedx = 0
        self.speedy = 0
        self.maxSpeed = maxSpeed
        self.speed = [self.speedx, self.speedy]
        self.didBounceX = False
        self.didBounceY = False

        self.lives = 5
        self.hit = False
        self.health = 3
        self.living = True

        #self.frame = 0
        #self.maxFrame = len(self.images) - 1
        #self.animationTimer = 0
        #self.animationTimerMax = .2 * 60 #seconds * 60 fps
        #self.blinkFrame = 0

        self.animate()

    def update(self, screenSize):
        self.move()
        self.screenCollide(screenSize)
    
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.animate()



    def animate(self):
        if self.prevState != self.state:
            if self.state == "right":
                self.image == self.imageRight
                print "right"
            elif self.state == "left":
                self.image == self.imageLeft
                print "left"
            elif self.state == "up":
                self.image == self.imageUp
                print "up"
            elif self.state == "down":
                self.image == self.imageDown
                print "down"

    def go(self, direction):
        if direction == "right":
            self.speedx = self.maxSpeed
            self.speedy = 0
            self.state = "right"
        elif direction == "left":
            self.speedx = -self.maxSpeed
            self.speedy = 0
            self.state = "left"
        elif direction == "up":
            self.speedx = 0
            self.speedy = -self.maxSpeed
            self.state = "up"
        elif direction == "down":
            self.speedx = 0
            self.speedy = self.maxSpeed
            self.state = "down"

        elif direction == "stop up":
            self.speedy = 0
            self.prevState = "up"
        elif direction == "stop down":
            self.speedy = 0
            self.prevState = "down"
        elif direction == "stop left":
            self.speedx = 0
            self.prevState = "left"
        elif direction == "stop right":
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
