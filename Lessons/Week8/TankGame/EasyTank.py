from Cannon import *
from Bullet import *
from Tank import *

class EasyTank(Tank):
    def __init__(self, x, y, cannonColor, bodyColor, bulletColor, laserColor):
        super(EasyTank, self).__init__(x, y, cannonColor, bodyColor, bulletColor, laserColor)
        self.bullets = 1
        self.cannon = Cannon(x, y, cannonColor, laserColor, False)
    
    def computeNextMove(self, walls, bullets):
        pass
    
