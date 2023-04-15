from Cannon import *
from Bullet import *

class Tank:
    def __init__(self, x, y, cannonColor, bodyColor, bulletColor):
        self.position = Vector2D(x, y)
        self.bodyLength = 75
        self.speed = 2
        self.cannon = Cannon(x, y, cannonColor)
        self.bodyColor = bodyColor
        self.bulletColor = bulletColor
        self.wasd = [0, 0, 0, 0]
        self.bullets = 3
    
    def drawTank(self):
        pushStyle()
        fill(self.bodyColor.r, self.bodyColor.g, self.bodyColor.b)
        rect(self.position.x - self.bodyLength / 2, self.position.y - self.bodyLength / 2, self.bodyLength, self.bodyLength)
        popStyle()
        
        self.cannon.drawCannon()
    
    def moveTank(self):
        self.position.x = self.position.x + self.speed * (self.wasd[1] * -1 + self.wasd[3])
        self.position.y = self.position.y + self.speed * (self.wasd[0] * -1 + self.wasd[2])
        self.cannon.startPosition.x = self.cannon.startPosition.x + self.speed * (self.wasd[1] * -1 + self.wasd[3])
        self.cannon.startPosition.y = self.cannon.startPosition.y + self.speed * (self.wasd[0] * -1 + self.wasd[2])
    
    def shoot(self):
        if self.bullets <= 0:
            return
        else:
            self.bullets -= 1
            
        return Bullet(self.cannon.endPosition.x, self.cannon.endPosition.y, 12, 10, self.cannon.directionVector, self.bulletColor, self)
        
        
