from SpaceShip import *
from SmallBullet import *
from LargeBullet import *

class HumanShip(SpaceShip):
    def __init__(self, x, y, health):
        super(HumanShip, self).__init__(x, y, -1, health)
        self.smallAmmo = 4
        self.largeAmmo = 1
    
    def drawShip(self):
        fill(0, 0, 255)
        triangle(self.x, self.y, self.x - 40, self.y + 40, self.x + 40, self.y + 40)
    
    def fireSmallBullet(self, bullets):
        if <------ We can only fire if we have small ammo -------> > 0:
            newBullet = SmallBullet(self.x - 10, self.y)
            bullets.append(<----- The bullet we just created ------->)
            self.smallAmmo = self.smallAmmo - <----- This should be a number ----->
    
    def fireLargeBullet(self, bullets):
        if <------ We can only fire if we have large ammo -------> > 0:
            newBullet = LargeBullet(self.x - 25, self.y)
            bullets.append(<----- The bullet we just created ------->)
            self.largeAmmo = self.largeAmmo - <----- This should be a number ----->
        
        
    
