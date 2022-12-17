from Weapon import *

class Sword(Weapon):
    def __init__(self, level, baseDamage, maxDistance):
        super(Sword, self).__init__(level, baseDamage, maxDistance)
    
    def swing(self):
        return self.baseDamage
    
    def thrust(self):
        return self.baseDamage * 1.2
