from Vector2D import *

class Cannon:
    def __init__(self, x, y):
        self.baseRadius = 40
        self.barrelLength = 100
        self.startPosition = Vector2D(x, y);
        
        # We also initialize the end position and direction with default values
        self.endPosition = Vector2D(x, y)
        self.directionVector = Vector2D(1, 0)
    
    def updateCannonParameters(self):
        # Determine the position vector for the end of the barrel that has the correct magnitude
        barrelPositionVectorEnd = Vector2D(mouseX, mouseY)
        displacementVector = barrelPositionVectorEnd - self.startPosition  # This is in the right direction but wrong magnitude
        lenCorrectDisplacementVector = self.barrelLength * displacementVector.getUnitVector()
        self.endPosition = self.startPosition + lenCorrectDisplacementVector
        self.directionVector = displacementVector.getUnitVector()
    
    def drawCannon(self):
        # Draw the base of the cannon
        ellipse(self.startPosition.x, self.startPosition.y, self.baseRadius * 2, self.baseRadius * 2)
        
        # Make sure to update the cannon before drawing it
        self.updateCannonParameters()
        
        # Draw the barrel of the cannon
        pushStyle()
        stroke(255, 255, 255)
        strokeWeight(30)
        line(self.startPosition.x, self.startPosition.y, self.endPosition.x, self.endPosition.y)
        popStyle()
        
