from Weapon import *

class Arrow(Weapon):
    def __init__(self, level, baseDamage, maxDistance):
        super(Arrow, self).__init__(level, baseDamage, maxDistance)
    
    def shoot(self):
        return self.baseDamage
        
        
