from Vector2D import *
from Color import *

class Bullet:
    # Note: the speed and directionVector together form what we call the velocity
    def __init__(self, x, y, radius, speed, directionVector, bulletColor, bulletOwner):
        self.position = Vector2D(x, y)
        self.radius = radius
        self.speed = speed
        self.direction = directionVector
        self.bulletColor = bulletColor
        self.bulletOwner = bulletOwner
        self.numberOfBounces = 0
    
    def drawBullet(self):
        pushStyle()
        fill(self.bulletColor.r, self.bulletColor.g, self.bulletColor.b)
        ellipse(self.position.x, self.position.y, self.radius * 2, self.radius * 2)
        popStyle()
    
    def moveBullet(self):
        self.position.x += self.speed * self.direction.x
        self.position.y += self.speed * self.direction.y
