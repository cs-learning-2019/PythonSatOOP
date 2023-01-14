from <------ We need to import this -------> import *

class SmallAlienShip(<---- We need to inherit from a super class ----->):
    def __init__(self, x, y, speed, health):
        super(SmallAlienShip, self).__init__(<------ Pass in the correct parameters ------>)
        self.damage = 100
        self.size = 50
        
    def drawShip(self):
        fill(208, 121, 255)
        rect(self.x, self.y, self.size, self.size)
        
    def moveShip(self):
        self.y = self.y + self.speed
        
        
    
