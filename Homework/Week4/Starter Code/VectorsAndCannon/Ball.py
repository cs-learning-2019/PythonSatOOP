from Vector2D import *

class Ball:
    # Note: the speed and directionVector together form what we call the velocity
    def __init__(self, x, y, radius, speed, directionVector):
        self.position = Vector2D(x, y)
        self.radius = radius
        self.speed = speed
        self.direction = directionVector
    
    def updatePosition(self):
        self.position.x += self.speed * self.direction.x
        self.position.y += self.speed * self.direction.y
    
    def drawBall(self):
        pushStyle()
        fill(255, 255, 0)
        ellipse(self.position.x, self.position.y, self.radius * 2, self.radius * 2)
        popStyle()
