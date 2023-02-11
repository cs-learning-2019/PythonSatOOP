from <------ We need to import this -------> import *

class LargeAlienShip(SpaceShip):
    def __init__(self, x, y, speed, health):
        super(LargeAlienShip, self).__init__(<------ Pass in the correct parameters ------>)
        self.damage = 200
        self.size = 80
        
    def drawShip(self):
        fill(166, 27, 242)
        # Draw a square for the large alien ship
        <----- missing something... ----->(self.x, self.y, self.size, self.size)
        
    def moveShip(self):
        self.y = self.y + self.speed
        
        
    
