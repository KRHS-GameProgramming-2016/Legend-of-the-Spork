import pygame, sys, math, random

class Bug(pygame.sprite.Sprite):
    def __init__(self, speed=0, pos=[0,0], size=64):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = size
        self.imagesLeft = [pygame.transform.scale(pygame.image.load("Res/Enemies/PNG/Bug1.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/PNG/Bug2.png"), [self.size,self.size])]
        self.imagesRight = [pygame.transform.scale(pygame.image.load("Res/Enemies/PNG/Bug1R.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/PNG/Bug2R.png"), [self.size,self.size])]
        self.imagesUp = [pygame.transform.scale(pygame.image.load("Res/Enemies/PNG/Bug1.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/PNG/Bug2.png"), [self.size,self.size])]
        self.imagesDown = [pygame.transform.scale(pygame.image.load("Res/Enemies/PNG/Bug1.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Enemies/PNG/Bug2.png"), [self.size,self.size])]

        self.maxSpeed = speed

        self.didBounceX = False
        self.didBounceY = False
        self.hp = 3
        self.living = True

        self.state = "right"
        self.prevState = "right"

        self.frame = 0
        self.animationTimer = 0
        self.animationTimerMax = 5 #.3 * 60 #seconds * 60 fps
        self.images = self.imagesRight
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxFrame = len(self.images) - 1

        self.decideDirection()
        self.hit = False
        self.animate()

    def update(self, *args):
        screenSize = args[0]
        self.move()
        self.animate()
        self.screenCollide(screenSize)
        print self.hp
        if self.hp == 0:
            self.living = False

        if self.living == False:
            self.kill()
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        if self.speedx != 0:     #moving left/right
            if self.rect.left % self.size == 0:
                self.decideDirection()
        else:     #moving up/down
            if self.rect.top % self.size == 0:
                self.decideDirection()


    def decideDirection(self):
        d = random.randint(0,3)
        if d == 0:
            self.speedx = 0
            self.speedy = -self.maxSpeed
            self.state = "up"
        elif d == 1:
            self.speedx = self.maxSpeed
            self.speedy = 0
            self.state = "right"
        elif d == 2:
            self.speedx = 0
            self.speedy = self.maxSpeed
            self.state = "down"
        elif d == 3:
            self.speedx = -self.maxSpeed
            self.speedy = 0
            self.state = "left"

    def animate(self):
        if self.prevState != self.state:
            self.prevState = self.state
            if self.state == "right":
                self.images = self.imagesRight
            elif self.state == "left":
                self.images = self.imagesLeft
            elif self.state == "up":
                self.images = self.imagesUp
            elif self.state == "down":
                self.images = self.imagesDown
            self.frame = 0
            self.maxFrame = len(self.images) - 1
            self.animationTimer = self.animationTimerMax

        if self.animationTimer < self.animationTimerMax:
            self.animationTimer += 1

        else:
            self.animationTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]

    def screenCollide(self, screenSize):
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        if self.rect.top < 0 or self.rect.bottom > screenHeight:
            self.speedy = 0
            self.decideDirection()
        if self.rect.left < 0 or self.rect.right > screenHeight:
            self.speedx = 0
            self.decideDirection()

    def playerCollide(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.speedx = 0
        self.didBounceX = True
        self.speedy = 0
        self.didBounceY = True
        other.hit = True
        
    def weaponCollide(self, other):
        self.decideDirection()
        self.hp -= other.damage

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
        return math.sqrt(xDiff**2 + yDiff**2)
