from Sword import *
from Player import *

class SwordMan(Player):
    def __init__(self, rank):
        super(SwordMan, self).__init__(rank)
        self.weapon = Sword(1, 50, 2)
        
    def weakAttack(self):
        damage_done = 0
        if self.stamina >= 10:
            damage_done = self.weapon.swing()
            self.stamina = self.stamina - 10
        
        return damage_done
        
    def strongAttack(self):
        damage_done = 0
        if self.stamina >= 50:
            damage_done = self.weapon.thrust()
            self.stamina = self.stamina - 50
        
        return damage_done
       
       
       
       
       
       
       
        
        
