from Sword import *
from Arrow import *

class Player(object):
    def __init__(self, rank):
        self.health = 100 * rank
        self.stamina = 100 * rank
        self.rank = rank
        self.isAlive = True
    
    def increase_stamina_at_end_of_phase(self):
        self.stamina = self.stamina + 30
    
    def heal(self, amount):
        self.health = self.health + amount
        
    def take_damage(self, amount):
        self.health = self.health - amount
        if self.health <= 0:
            self.isAlive = False
