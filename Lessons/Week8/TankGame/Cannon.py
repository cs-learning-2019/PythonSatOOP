from Vector2D import *
from Color import *
from CollisionProcessor import *

class Cannon:
    def __init__(self, x, y, cannonColor, laserColor, isPlayerTank):
        self.baseRadius = 20
        self.barrelLength = 70
        self.startPosition = Vector2D(x, y)
        self.cannonColor = cannonColor
        self.laserColor = laserColor
        self.cp = CollisionProcessor()
        self.isPlayerTank = isPlayerTank
        
        # We also initialize the end position and direction with default values
        self.endPosition = Vector2D(x + self.barrelLength, y)
        self.directionVector = Vector2D(1, 0)
        self.laserPoc = Vector2D(x, y)
        self.laserEndPosition = Vector2D(x, y)
    
    def updateCannonParameters(self, walls):
        # Determine the position vector for the end of the barrel that has the correct magnitude
        barrelPositionVectorEnd = Vector2D(mouseX, mouseY)
        displacementVector = barrelPositionVectorEnd - self.startPosition  # This is in the right direction but wrong magnitude
        lenCorrectDisplacementVector = self.barrelLength * displacementVector.getUnitVector()
        self.endPosition = self.startPosition + lenCorrectDisplacementVector
        self.directionVector = displacementVector.getUnitVector()
        
        # Update the laser positions
        minPoc = (None, None, -1)
        for wall in walls:
            result = self.cp.cannonLaserAndWallPoc(self.endPosition, self.directionVector, wall)
            if result is not None and (minPoc[2] == -1 or minPoc[2] > result[2]):
                minPoc = result
        
        if (minPoc[0] is None) or (minPoc[1] is None):
            return
        
        self.laserPoc = minPoc[0]
        reflectionDirection = self.cp.computeReflectionVector(minPoc[1].normal, -1 * self.directionVector)
        self.laserEndPosition = self.laserPoc + (200 * reflectionDirection)

                
    def drawCannon(self, walls):
        # Make sure to update the cannon before drawing it
        if (self.isPlayerTank):
            self.updateCannonParameters(walls)
        
        # Draw the base of the cannon
        pushStyle()
        fill(self.cannonColor.r, self.cannonColor.g, self.cannonColor.b)
        stroke(self.cannonColor.r, self.cannonColor.g, self.cannonColor.b)
        ellipse(self.startPosition.x, self.startPosition.y, self.baseRadius * 2, self.baseRadius * 2)
        popStyle()
        
        # Draw the barrel of the cannon
        pushStyle()
        stroke(self.cannonColor.r, self.cannonColor.g, self.cannonColor.b)
        strokeWeight(15)
        line(self.startPosition.x, self.startPosition.y, self.endPosition.x, self.endPosition.y)
        popStyle()
        
        # Draw the laser
        if (self.isPlayerTank):
            pushStyle()
            stroke(self.laserColor.r, self.laserColor.g, self.laserColor.b)
            strokeWeight(3)
            line(self.endPosition.x, self.endPosition.y, self.laserPoc.x, self.laserPoc.y)
            line(self.laserPoc.x, self.laserPoc.y, self.laserEndPosition.x, self.laserEndPosition.y)
            popStyle()
        
        
