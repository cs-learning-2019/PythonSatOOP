"""
This class represents the Earth that we are protecting
- The starting health of Earth is 300 and the size should be 1500
- self.size will be the radius of the Earth in both the x and y directions
"""

class Earth:
    def __init__(self):
        self.x = 350
        self.y = 1610
        self.size = <------ The size ------->
        self.health = <------ The health ------->
        
    def drawEarth(self):
        if self.health >= 300:
            fill(0, 200, 0)
            ellipse(self.x, self.y, self.size, self.size)
        elif self.health >= 200:
            fill(242, 196, 27)
            <------ Draw the Earth (this is not a trick question is should be very easy) ------->
        elif self.health >= 100:
            fill(200, 0, 0)
            <------ Draw the Earth (this is not a trick question is should be very easy) ------->
    
    def takeDamage(self, amount):
        <------ Subtract the provided amount from Earth's health ------->
