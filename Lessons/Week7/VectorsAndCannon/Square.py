from Vector2D import *

class Square:
    # Note: the speed and directionVector together form what we call the velocity
    def __init__(self, x, y, length, speed, directionVector):
        self.position = Vector2D(x, y)
        self.length = length
        self.speed = speed
        self.direction = directionVector
    
    def updatePosition(self):
        self.position.x += self.speed * self.direction.x
        self.position.y += self.speed * self.direction.y
    
    def drawSquare(self):
        pushStyle()
        fill(255, 255, 0)
        rect(self.position.x, self.position.y, self.length, self.length)
        popStyle()
