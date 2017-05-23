import sys, math, pygame, random

from Player import *
from Bug import *
from Wolf import *
#from Troll import *
#from Boss import *
from LevelLoader import *
#from Spork import *
#from HUD import *
from Tiles import *
from Impassable import *
from Shop import *
from Title import *
from BackgroundItems import *
from Health import *
from Weapon import *
pygame.init()

clock = pygame.time.Clock()

width = 700
height = 850 # 700 for game screen, 150 for HUD crap
size = width, height
gameSize = 11*64,11*64
screen = pygame.display.set_mode(size)
bgColor = 0,0,0

all = pygame.sprite.OrderedUpdates()

players = pygame.sprite.Group()
bugs = pygame.sprite.Group()
wolfs = pygame.sprite.Group()
#bandits = pygame.sprite.Group()
#trolls = pygame.sprite.Group()
#bosss = pygame.sprite.Group()
impassables = pygame.sprite.Group()
interactables = pygame.sprite.Group()
shops = pygame.sprite.Group()
backgrounditems = pygame.sprite.Group()
tiles = pygame.sprite.Group()
titles = pygame.sprite.Group()
healths = pygame.sprite.Group()
weapons = pygame.sprite.Group()

Player.containers = all, players
Bug.containers = all, bugs
Wolf.containers = all, wolfs
#Bandit.containers = all, bandits
#Troll.containers = all, trolls
#Boss.containers = all, bosss
Impassables.containers = all, impassables
Shop.containers = all, shops, interactables, impassables
BackgroundItems.containers = all, backgrounditems
Tiles.containers = all, tiles
Title.containers = all, tiles
Health.containers = all, healths
Weapon.containers = all, weapons

world = 1
screenx = 1
screeny = 1

while True:
    menu = True
    controls = True
    end = False
    Title("Res/Background/Controls copy.png", size)
    while controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    controls = False
                    menu = True
                    end = False
                    Title("Res/Background/Titlescreen.png", size)

        all.update(size)

        bgColor = r,g,b = 0,0,0
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    menu = False
                if event.key == pygame.K_2:
                    sys.exit()

        all.update(size)

        bgColor = r,g,b = 0,0,0
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

    for s in all.sprites():
        s.kill()

    level = Level(str(world) + str(screenx) + str(screeny))
    player = Player(64, 0, 5,[96,96])
    health = Health([width*.20, 750], player.health)
    while player.living == True:
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
                if event.key == pygame.K_LSHIFT:
                    player.attack()

                if event.key == pygame.K_w:
                    player.go("up")
                if event.key == pygame.K_s:
                    player.go("down")
                if event.key == pygame.K_d:
                    player.go("right")
                if event.key == pygame.K_a:
                    player.go("left")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_LEFT:
                    player.go("stop left")

                if event.key == pygame.K_w:
                    player.go("stop up")
                if event.key == pygame.K_s:
                    player.go("stop down")
                if event.key == pygame.K_d:
                    player.go("stop right")
                if event.key == pygame.K_a:
                    player.go("stop left")

            if players.sprites <= 0:
                menu = False
                controls = False
                end = True

        all.update(gameSize, player.health)

        if player.screenCollide(gameSize):
            if player.rect.left <= 0:
                screenx -= 1
                px = gameSize[0] - (64/2 + 1)
                py = player.rect.center[1]
            if player.rect.right >= gameSize[0]:
                screenx += 1
                px = 0 + (64/2 + 1)
                py = player.rect.center[1]
            if player.rect.top <= 0:
                screeny -= 1
                px = player.rect.center[0]
                py = gameSize[1] - (64/2 + 1)
            if player.rect.bottom >= gameSize[1]:
                screeny += 1
                px = player.rect.center[0]
                py = 0 + (64/2 + 1)

            ph = player.health
            for s in all.sprites():
                s.kill()
            level = Level(str(world) + str(screenx) + str(screeny))
            player = Player(64, 0, 5, [px, py], ph)
            health = Health([width*.20, 750], player.health)

        playerHitsImpassables = pygame.sprite.spritecollide(player, impassables, False)
        playerHitsIntearactables = pygame.sprite.spritecollide(player, interactables, False)
        playerHitsShops = pygame.sprite.spritecollide(player, shops, False)
        playerHitsBugs = pygame.sprite.spritecollide(player, bugs, False)

        for impassable in playerHitsImpassables:
            player.impassableCollide(impassable)

        for bug in playerHitsBugs:
            player.bugCollide(bug)


        bgColor = r,g,b = 0,0,0
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    for s in all.sprites():
        s.kill()

    if player.living == False:
        end = True
        controls = False
        menu = False

    while end:
        Title("Res/Background/End.png", size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                sys.exit()

        all.update(size)

        bgColor = r,g,b = 0,0,0
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

    for s in all.sprites():
        s.kill()
