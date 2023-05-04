from Vector2D import *
from Color import *

class Wall:
    def __init__(self, startX, startY, endX, endY, thickness, wallColor):
        self.startPosition = Vector2D(startX, startY)
        self.endPosition = Vector2D(endX, endY)
        self.thickness = thickness
        self.direction = Vector2D(endX - startX, endY - startY).getUnitVector()
        self.normal = self.direction.getNormalVector()
        self.wallColor = wallColor
        
    def drawWall(self):
        pushStyle()
        strokeWeight(self.thickness)
        stroke(self.wallColor.r, self.wallColor.g, self.wallColor.b)
        line(self.startPosition.x, self.startPosition.y, self.endPosition.x, self.endPosition.y)
        popStyle()

    
