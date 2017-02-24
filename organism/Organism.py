import math
import random
class Individual:
    ''' One instance of organism '''
    def __init__(self, energy,x,y):
        self.energy = energy
        self.maxEnergy = 1024
        self.energyPerTick = 1
        self.color = (122,122,122)
        self.positionX = x
        self.positionY = y
        self.alive = True
        self.deadSince = 0
        self.digestionMultiplyer = random.random()

    def tick(self):
        self.energy = self.energy - self.energyPerTick
        if self.energy <= 0:
            self.alive = False
            self.color = (255,0,0)
            self.deadSince += 1
            if self.deadSince>120:
                self.color=(0,0,0)
        else:
            # Generate color based on energy
            newColor = ((self.energy/float(self.maxEnergy)))*255
            self.color = (0,newColor,0)

    def takeInEnergy(self,amount):
        self.energy = amount*self.digestionMultiplyer




    def getColor(self):
        return self.color

    def setPos(self,x,y):
        self.positionX = x
        self.positionY = y

    def getX(self):
        return self.positionX
    def getY(self):
        return self.positionY
