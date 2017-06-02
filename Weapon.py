import sys, pygame, math, random

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.imageRight = pygame.image.load("Res/Player/Spork.png")
        self.imageLeft = pygame.image.load("Res/Player/WeaponLeft.png")
        self.imageUp = pygame.image.load("Res/Player/WeaponUp.png")
        self.imageDown = pygame.image.load("Res/Player/WeaponDown.png")
        
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
    
    def update(self, *args):
        attacking = args[2]
        if not attacking:
            self.kill()
            
    def bugCollide(self, other):
        other.hp -= 1
        other.decideDirection()
