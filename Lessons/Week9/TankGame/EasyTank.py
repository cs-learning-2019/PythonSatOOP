from Cannon import *
from Bullet import *
from Tank import *

class EasyTank(Tank):
    def __init__(self, x, y, cannonColor, bodyColor, bulletColor, laserColor):
        super(EasyTank, self).__init__(x, y, cannonColor, bodyColor, bulletColor, laserColor)
        self.bullets = 1
        self.cannon = Cannon(x, y, cannonColor, laserColor, False)
        self.aimTolerance = 50  # Feel free to modify this
        self.fireChance = 20 # Percentage of how often the tank will shoot 
    
    def computeNextMove(self, walls, bullets, playerTank):
        pass
        # Compute the movement of the tank to dodge bullets (maximize profit)
        # Since this is an easy tank we don't want it to perfectly avoid bullets so no need to consider the bullet's direction
        # Make sure the tank does not go through walls so we can use self.isTankTouchingWall() to help us
        
        
        # Calculate the end position of the tank's cannon
        # We don't want the AI to have aimbot since that would be unfair so we need to add some aim tolerance
        # The idea is to use the tank's aim tolerance so that the cannon is not always pointing directly at the player
        # Hint: you can re-use some of the code from updateCannonParameters in the Cannon class
        # Hint: x = random(-1.0 * self.aimTolerance , self.aimTolerance)
        # Hint: y = random(-1.0 * self.aimTolerance , self.aimTolerance)
        
    
        # Calculate if the tank should shoot
        # Since this is the easy tank we only give it 1 bullet
        # The tank will take a shoot with a chance of self.fireChance regardless of where the cannon is pointed
        # Generate a random number between [0, 100]
        
    
