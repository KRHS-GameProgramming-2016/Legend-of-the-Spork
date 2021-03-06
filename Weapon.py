import sys, pygame, math, random

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.imageRight = pygame.image.load("Res/Player/Spork.png")
        self.imageLeft = pygame.image.load("Res/Player/SporkLeft.png")
        self.imageUp = pygame.image.load("Res/Player/SporkUp.png")
        self.imageDown = pygame.image.load("Res/Player/SporkDown.png")

        if direction == "right":
            self.image = self.imageRight
            pos = [pos[0] + 35,
                   pos[1] + 10]
        elif direction == "left":
            self.image = self.imageLeft
            pos = [pos[0] - 35,
                   pos[1] + 10]
        elif direction == "up":
            self.image = self.imageUp
            pos = [pos[0] + 10,
                   pos[1] - 35]
        elif direction == "down":
            self.image = self.imageDown
            pos = [pos[0] - 10,
                   pos[1] + 35]
        self.rect = self.image.get_rect(center = pos)
        self.damage = 1
        self.collideTimer = 0
        self.collideTimerMax = .5*60 #second * 60fpss

    def update(self, *args):
        attacking = args[2]
        if not attacking:
            self.kill()
        if self.collideTimer < self.collideTimerMax:
            self.collideTimer += 1
            self.damage = 0

        else:
            self.animationTimer = 0
            self.damage = 1
