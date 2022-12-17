from Arrow import *
from Player import *

class ArrowMan(Player):
    def __init__(self, rank):
        super(ArrowMan, self).__init__(rank)
        self.weapon = Arrow(1, 50, 2)
        
    def shoot(self):
        damage_done = 0
        if self.stamina >= 2:
            damage_done = self.weapon.shoot()
            self.stamina = self.stamina - 2
        
        return damage_done
       
       
       
       
       
       
       
        
        
