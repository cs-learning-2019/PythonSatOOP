from Cannon import *
from Bullet import *

class Tank(object):
    def __init__(self, x, y, cannonColor, bodyColor, bulletColor, laserColor):
        self.position = Vector2D(x, y)
        self.bodyLength = 75
        self.speed = 2
        self.cannon = Cannon(x, y, cannonColor, laserColor, True)
        self.bodyColor = bodyColor
        self.bulletColor = bulletColor
        self.wasd = [0, 0, 0, 0]
        self.bullets = 3
        self.cp = CollisionProcessor()
    
    def drawTank(self, walls):
        pushStyle()
        fill(self.bodyColor.r, self.bodyColor.g, self.bodyColor.b)
        rect(self.position.x - self.bodyLength / 2, self.position.y - self.bodyLength / 2, self.bodyLength, self.bodyLength)
        popStyle()
        
        self.cannon.drawCannon(walls)
    
    def moveTank(self, walls):
        newBodyX = self.position.x + self.speed * (self.wasd[1] * -1 + self.wasd[3])
        newBodyY = self.position.y + self.speed * (self.wasd[0] * -1 + self.wasd[2])
        
        # We need to check if the new position would place the tank in a wall
        if (self.isTankTouchingWall(walls)):
            return
        

        # Only do the code below if the tank is not touching a wall
        self.position.x = newBodyX
        self.position.y = newBodyY
        self.cannon.startPosition.x = self.cannon.startPosition.x + self.speed * (self.wasd[1] * -1 + self.wasd[3])
        self.cannon.startPosition.y = self.cannon.startPosition.y + self.speed * (self.wasd[0] * -1 + self.wasd[2])
    
    def shoot(self):
        if self.bullets <= 0:
            return
        else:
            self.bullets -= 1
            
        return Bullet(self.cannon.endPosition.x, self.cannon.endPosition.y, 12, 10, self.cannon.directionVector, self.bulletColor, self)
    
    def isTankTouchingWall(walls):
        # PLEASE DO THIS FOR HW (Hint: approximate the body of the tank using a circle and use self.cp.wallAndBall)
        return False
        
        
        
