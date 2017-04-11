import sys, math, pygame, random
from Player import *
from Bug import *
#from Wolf import *
#from Troll import *
#from Boss import *
from LevelLoader import *
#from Spork import *
#from HUD import *
from Tiles import *
from Impassable import *
#from Shop import *
#from Title import *
from BackgroundItems import *
pygame.init()

clock = pygame.time.Clock()

width = 768
height = 640
size = width, height
screen = pygame.display.set_mode(size)
bgColor = 0,0,0


all = pygame.sprite.OrderedUpdates()

players = pygame.sprite.Group()
bugs = pygame.sprite.Group()
#wolfs = pygame.sprite.Group()
#bandits = pygame.sprite.Group()
#trolls = pygame.sprite.Group()
#bosss = pygame.sprite.Group()
impassables = pygame.sprite.Group()
backgrounditems = pygame.sprite.Group()
tiles = pygame.sprite.Group()

Player.containers = all, players
Bug.containers = all, bugs
#Wolf.containers = all, wolfs
#Bandit.containers = all, bandits
#Troll.containers = all, trolls
#Boss.containers = all, bosss
Impassables.containers = all, impassables
BackgroundItems.containers = all, backgrounditems
Tiles.containers = all, tiles

level = Level("World1")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_LEFT:
                player.go("left")
            if event.key == pygame.K_d:
                player.dig()
            if event.key == pygame.K_s:
                playerBullets += [Playerfire(player.state, player.rect.center)]
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
                
    all.update(size)
    
    bgColor = r,g,b = 0,0,0
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
