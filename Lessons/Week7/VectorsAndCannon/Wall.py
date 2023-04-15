from Vector2D import *

class Wall:
    def __init__(self, startX, startY, endX, endY, thickness):
        self.startPosition = Vector2D(startX, startY)
        self.endPosition = Vector2D(endX, endY)
        self.thickness = thickness
        self.direction = Vector2D(endX - startX, endY - startY).getUnitVector()
        self.normal = self.direction.getNormalVector()
        
    def drawWall(self):
        pushStyle()
        strokeWeight(self.thickness)
        stroke(255, 0, 0)
        line(self.startPosition.x, self.startPosition.y, self.endPosition.x, self.endPosition.y)
        popStyle()
    
    # We should only use this method for testing
    def drawNormal(self):
        pushStyle()
        strokeWeight(self.thickness)
        stroke(0, 255, 0)
        line(self.startPosition.x, self.startPosition.y,\
             self.startPosition.x + (self.normal.x * 100), self.startPosition.y + (self.normal.y * 100))
        popStyle()
    
