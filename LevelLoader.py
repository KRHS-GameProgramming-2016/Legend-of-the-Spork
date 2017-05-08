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
        self.tileSize = 64
        self.loadLevel(levelFile, levelNumber)


    def unloadLevel(self):
        pass

    def loadLevel(self, levelFile, levelNumber):
        f = open("Res/World/"+levelFile+".lvl")
        lines = f.readlines()
        f.close()

        for line in lines:
            print line

        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]

        lines = newlines



        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c in "`" :       #Grass
                    Tiles("grass",
                           [x*self.tileSize + self.tileSize/2,
                            y*self.tileSize + self.tileSize/2],
                           self.tileSize)

                if c in "=" :       #Path
                    Tiles("path",
                           [x*self.tileSize + self.tileSize/2,
                            y*self.tileSize + self.tileSize/2],
                           self.tileSize)

                if c in '"' :       #Sand
                    Tiles("sand",
                           [x*self.tileSize + self.tileSize/2,
                            y*self.tileSize + self.tileSize/2],
                           self.tileSize)
                if c in "~" :       #River
                    Impassables("river",
                           [x*self.tileSize + self.tileSize/2,
                            y*self.tileSize + self.tileSize/2],
                           self.tileSize)
                

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
                
                
                if c in "p":       #Player
                    Player(64, 0, 5, 
                        [x*self.tileSize + self.tileSize/2,
                         y*self.tileSize + self.tileSize/2])
                if c in "q" :       #Bug
                    Bug(1,
                           [x*self.tileSize + self.tileSize/2,
                            y*self.tileSize + self.tileSize/2],
                           self.tileSize)
                if c in "*" :       #Boulder
                    Impassables("boulder",
                           [x*self.tileSize + self.tileSize/2,
                            y*self.tileSize + self.tileSize/2],
                           self.tileSize)
                #if c in "w" :       #Wolf
                    #Impassables("boulder",
                           #[x*self.tileSize + self.tileSize/2,
                            #y*self.tileSize + self.tileSize/2],
                           #self.tileSize)

                #if c in "e" :       #Bandit
                    #Impassables("boulder",
                           #[x*self.tileSize + self.tileSize/2,
                            #y*self.tileSize + self.tileSize/2],
                           #self.tileSize)

                #if c in "r" :       #Troll
                    #Impassables("boulder",
                           #[x*self.tileSize + self.tileSize/2,
                            #y*self.tileSize + self.tileSize/2],
                           #self.tileSize)

                #if c in "t" :       #Boss
                    #[Impassables("boulder",
                           #[x*self.tileSize + self.tileSize/2,
                            #y*self.tileSize + self.tileSize/2],
                           #self.tileSize)
