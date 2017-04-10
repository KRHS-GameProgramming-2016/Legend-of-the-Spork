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
        self.dirts = []
        self.players = []
        self.enemies = []
        self.playerSpawns = []
        self.tileSize = tileSize

        self.loadLevel(levelFile, levelNumber)

    def unloadLevel(self):
        self.dirts = []
        self.player = []
        self.enemySpawn = []

    def loadLevel(self, levelFile, levelNumber):
        f = open("Resources/Levels/"+levelFile)
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

        startIndex = lines.index(str(levelNumber))+1
        endIndex = startIndex + 10

        newlines = []
        for line in range(startIndex, endIndex):
            #print lines[line]
            newlines += [lines[line]]
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
                if c in "~" :       #River
                    self.impassable += [Impassables("river",
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
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
                if c in "-" :       #Tree
                    self.backgrounditems += [BackgroundItems("bench",
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
                if c in "&" :       #Boulder
                    self.impassable += [Impassables("tree",
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  ]
#Minimun speed = 1 | max = 64


if __name__ == "__main__":
    level = Level("World1.lvl", 1)
