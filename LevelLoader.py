import sys, math, random
from Player import *
from Bug import *
from Wolf import *
from Bandit import *
from Troll import *
from Boss import *
from Spork import *
from Tiles import *
from Shop import *
from Impassable import *
from BackgroundItems import *

class Level():
    def __init__(self, levelFile, levelNumber=1, tileSize=64):
        self.tile = []
        self.players = []
        self.bugs = []
        self.wolfs = []
        self.bandits = []
        self.trolls = []
        self.bosss = []
        self.impassables = []
        self.backgrounditems = []
        self.tileSize = tileSize

        self.loadLevel(levelFile, levelNumber)

    def unloadLevel(self):
        self.tiles = []
        self.player = []
        self.bugSpawn = []
        self.wolfSpawn = []
        self.banditSpawn = []
        self.trollSpawn = []
        self.bossSpawn = []
        self.impassableSpawn = []
        self.backgrounditemSpawn = []

    def loadLevel(self, levelFile, levelNumber):
        f = open("Res/World/"+levelFile+".lvl")
        lines = f.readlines()
        f.close()

        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]

        lines = newlines

        for line in lines:
            print line

        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c in "`" :       #Grass
                    self.tiles += [Tiles("grass",
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
                if c in "=" :       #Path
                    self.tiles += [Tiles("path",
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
                if c in '"' :       #Sand
                    self.tiles += [Tiles("sand",
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
        f = open("Res/World/"+levelFile+".tng")
        lines = f.readlines()
        f.close()

        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]

        lines = newlines

        for line in lines:
            print line

        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c in "~" :       #River
                    self.impassable += [Impassables("river",
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
                if c in "*" :       #Boulder
                    self.impassable += [Impassables("boulder",
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
#Minimun speed = 1 | max = 64


if __name__ == "__main__":
    level = Level("World1.lvl", 1)
