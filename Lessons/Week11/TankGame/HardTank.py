from Cannon import *
from Bullet import *
from Tank import *
from Vector2D import *

class HardTank(Tank):
    def __init__(self, x, y, cannonColor, bodyColor, bulletColor, laserColor):
        super(HardTank, self).__init__(x, y, cannonColor, bodyColor, bulletColor, laserColor)
        self.bullets = 2
        self.cannon = Cannon(x, y, cannonColor, laserColor, False)
        self.aimTolerance = 400  # Feel free to modify this
        self.fireChance = 1 # Percentage of how often the tank will shoot
        self.speed = 4
    
    def computeNextMove(self, walls, bullets, playerTank):
        # Compute the movement of the tank to dodge bullets (maximize profit)
        # Since this is an easy tank we don't want it to perfectly avoid bullets so no need to consider the bullet's direction
        # Make sure the tank does not go through walls so we can use self.isTankTouchingWall() to help us
        moves = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]
        bestMove = [0, 0, 0, 0]
        bestScore = None
        for move in moves:
            score = 0
            newBodyX = self.position.x + self.speed * (move[1] * -1 + move[3])
            newBodyY = self.position.y + self.speed * (move[0] * -1 + move[2])
            if self.isTankTouchingWall(walls, newBodyX, newBodyY):
                continue
            for bullet in bullets:
                # First check to see if the bullet is moving away from you. If it is then we can just ignore it
                d1 = dist(self.position.x, self.position.y, bullet.position.x, bullet.position.y)
                newBulletX = bullet.position.x + bullet.speed * bullet.direction.x
                newBulletY = bullet.position.y + bullet.speed * bullet.direction.y
                d2 = dist(self.position.x, self.position.y, newBulletX, newBulletY)
                if d2 > d1:
                    continue
                
                d = dist(newBodyX, newBodyY, newBulletX, newBulletY)
                if d < 50:
                    score += -9999999999
                elif d <= 800:
                    score += -1.0 / d
    
                if move != [0, 0, 0, 0] and d <= 600:  # We only really care about the direction if the bullet gets close enough
                    v1 = bullet.direction
                    v2 = Vector2D(newBodyX - self.position.x, newBodyY - self.position.y).getUnitVector()
                    n = abs((v1 * v2) / (v1.getMagnitude() * v2.getMagnitude()))
                    score += (1 - n) * 5000
                    
                # We also need to avoid moving into the direction of a bullet
                displacementFromBulletStartToTank = Vector2D(newBodyX, newBodyY) - bullet.position
                projectionOfDisplacementOntoBulletDirection = (displacementFromBulletStartToTank * bullet.direction) * bullet.direction
                distance = (displacementFromBulletStartToTank - projectionOfDisplacementOntoBulletDirection).getMagnitude()
                score += distance * 500
                
            if move != [0, 0, 0, 0]:
                score += 100
            
            # We want the tank to be around 300 distance away from the player (aggression)
            d = dist(newBodyX, newBodyY, playerTank.position.x, playerTank.position.y)
            distanceToGoal = abs(d - 300)
            if distanceToGoal == 0:
                distanceToGoal = 0.00001
            score += 1.0 / distanceToGoal * 2.0
            
            if bestScore is None or bestScore < score:
                bestScore = score
                bestMove = move
        self.wasd = bestMove
        
        # Calculate the end position of the tank's cannon
        # We don't want the AI to have aimbot since that would be unfair so we need to add some aim tolerance
        # The idea is to use the tank's aim tolerance so that the cannon is not always pointing directly at the player
        # Hint: you can re-use some of the code from updateCannonParameters in the Cannon class
        shouldFire = random(0, 100) <= self.fireChance
        if shouldFire:
            x = random(-1.0 * self.aimTolerance , self.aimTolerance) + playerTank.position.x
            y = random(-1.0 * self.aimTolerance , self.aimTolerance) + playerTank.position.y
        else:
            x = self.cannon.endPosition.x
            y = self.cannon.endPosition.y
        barrelPositionVectorEnd = Vector2D(x, y)
        displacementVector = barrelPositionVectorEnd - self.cannon.startPosition  # This is in the right direction but wrong magnitude
        lenCorrectDisplacementVector = self.cannon.barrelLength * displacementVector.getUnitVector()
        self.cannon.endPosition = self.cannon.startPosition + lenCorrectDisplacementVector
        self.cannon.directionVector = displacementVector.getUnitVector()
        
        # Calculate if the tank should shoot
        # Since this is the easy tank we only give it 1 bullet
        # The tank will take a shoot with a chance of self.fireChance regardless of where the cannon is pointed
        # Generate a random number between [0, 100]
        if shouldFire:
            newBullet = self.shoot()
            if newBullet is not None:
                bullets.append(newBullet)
    
