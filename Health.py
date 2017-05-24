import pygame, sys, math, random

class Health(pygame.sprite.Sprite):
    def __init__(self, pos, value=3):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.oneLifeImage = pygame.image.load("Res/Health/hearts1life.png")
        self.twoLivesImage = pygame.image.load("Res/Health/hearts2lives.png")
        self.threeLivesImage = pygame.image.load("Res/Health/hearts3lives.png")
        self.fourLivesImage = pygame.image.load("Res/Health/hearts4lives.png")
        self.fiveLivesImage = pygame.image.load("Res/Health/hearts5lives.png")

        self.image = self.threeLivesImage
        self.rect = self.image.get_rect(center = pos)
        self.value = value

    def update(self, *args):
        newValue = args[1]
        if newValue != self.value:
            self.value = newValue
            if self.value == 5:
                self.image = self.fiveLivesImage
            if self.value == 4:
                self.image = self.fourLivesImage
            if self.value == 3:
                self.image = self.threeLivesImage
            if self.value == 2:
                self.image = self.twoLivesImage
            if self.value == 1:
                self.image = self.oneLifeImage
            self.rect = self.image.get_rect(center = self.rect.center)
