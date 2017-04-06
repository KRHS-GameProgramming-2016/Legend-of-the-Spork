import sys, math, pygame, random
from Player import *
from Bug import *
from Wolf import *
from Boss import *
from LevelLoader import *
from Spork import *
from HUD import *
from Tiles import *
from Impassable import *
from Shop import *
from Title import *
from BackgroundItems import *
pygame.init()

clock = pygame.time.Clock()

width = 768
height = 640
size = width, height
screen = pygame.display.set_mode(size)
bgColor = 0,0,0
level = Level("World1.lvl")
BG = Background(size)
