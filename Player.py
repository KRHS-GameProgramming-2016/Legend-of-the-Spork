import pygame, sys, math, time

class Player(pygame.sprite.Sprite):
    def __init__(self,  size=64, speed=0, maxSpeed=5, pos=[0,0], health=3):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = size
        self.imagesLeft = [pygame.transform.scale(pygame.image.load("Res/Player/Player side.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Player/Player side.png"), [self.size,self.size])]
        self.imagesRight = [pygame.transform.scale(pygame.image.load("Res/Player/Player side Right.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Player/Player side Right.png"), [self.size,self.size])]
        self.imagesUp = [pygame.transform.scale(pygame.image.load("Res/Player/Player Back.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Player/Player Back.png"), [self.size,self.size])]
        self.imagesDown = [pygame.transform.scale(pygame.image.load("Res/Player/Player.png"), [self.size,self.size]),
                           pygame.transform.scale(pygame.image.load("Res/Player/Player.png"), [self.size,self.size])]
        self.size = size

        self.state = "right"
        self.prevState = "right"
        self.images = self.imagesRight

        self.speedx = 0
        self.speedy = 0
        self.maxSpeed = maxSpeed
        self.speed = [self.speedx, self.speedy]
        self.didBounceX = False
        self.didBounceY = False

        self.hit = False
        self.health = health
        self.living = True
        self.attacking = False

        self.frame = 0
        self.animationTimer = 0
        self.animationTimerMax = 5 #.3 * 60 #seconds * 60 fps
        self.images = self.imagesRight
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxFrame = len(self.images) - 1

        self.animate()
        
        self.hitTimer = 0
        self.hitTimerMax = 1*60 #second * 60fps

    def update(self, *args):
        screenSize = args[0]
        self.move()
        self.animate()
        
        if self.hit:
            if self.hitTimer < self.hitTimerMax:
                self.hitTimer += 1
            else:
                self.hitTimer = 0
                self.hit = False
        if self.health <= 0:
            self.living = False    
        #self.screenCollide(screenSize)

    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

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
        wallHit = False
        if self.rect.top < 0 or self.rect.bottom > screenHeight:
            self.speedy = 0
            wallHit = True
        if self.rect.left < 0 or self.rect.right > screenWidth:
            self.speedx = 0
            wallHit = True
        return wallHit

    def impassableCollide(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.speedx = 0
        self.didBounceX = True
        self.speedy = 0
        self.didBounceY = True


    def bugCollide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if not self.hit:
                    self.hit = True
                    self.health -= 1
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.didBounceX = True
                self.didBounceY = True
                self.speedx = 0
                self.speedy = 0
                other.decideDirection()
                
                if self.health <= 0:
                    self.living = False

    def attack(self):
        self.attacking = True
