from Sword import *

class SwordMan:
    def __init__(self, rank):
        self.health = 100 * rank
        self.stamina = 100 * rank
        self.weapon = Sword(1, 50, 1)
        self.rank = rank
        self.isAlive = True
    
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
    
    def increase_stamina_at_end_of_phase(self):
        self.stamina = self.stamina + 30
    
    def heal(self, amount):
        self.health = self.health + amonut
        
    def take_damage(self, amount):
        self.health = self.health - amonut
        if self.health <= 0:
            self.isAlive = False
       
       
       
       
       
       
       
        
        
