from Vector2D import *
from Ball import *
from Wall import *
from Bullet import *

class CollisionProcessor:
    # Collision detector methods
    def wallAndBall(self, wall, ball):
        # First check to see if the ball is even in the rectangle spanned by the line
        x = [wall.startPosition.x, wall.endPosition.x]
        x.sort()
        y = [wall.startPosition.y, wall.endPosition.y]
        y.sort()
        tolerance = wall.thickness + 20
        if not self.isInInterval(x[0] - tolerance, x[1] + tolerance, ball.position.x) or \
        not self.isInInterval(y[0] - tolerance, y[1] + tolerance, ball.position.y):
            return False
        
        # Find the distance between the position of the ball and the wall
        displacementFromWallStartToBall = ball.position - wall.startPosition
        projectionOfDisplacementOntoWallDirection = (displacementFromWallStartToBall * wall.direction) * wall.direction
        distance = (displacementFromWallStartToBall - projectionOfDisplacementOntoWallDirection).getMagnitude()
        if distance <= (ball.radius * 0.7 + wall.thickness / 2.0):
            return True
        return False
    
    def ballAndBall(self, ball1, ball2):
        return dist(ball1.position.x, ball1.position.y, ball2.position.x, ball2.position.y) <= (ball1.radius + ball2.radius - 5)
    
    def wallAndTankBody(self, wall, bodyLength, bodyX, bodyY):
        boundingBall = Bullet(bodyX, bodyY, bodyLength / 2.0 , 0, None, None, None)
        return self.wallAndBall(wall, boundingBall)
    
    def bulletAndTankBody(self, bodyLength, bodyX, bodyY, bullet):
        boundingBall = Bullet(bodyX, bodyY, bodyLength / 2.0, 0, None, None, None)
        return self.ballAndBall(boundingBall, bullet)
    
    def cannonLaserAndWallPoc(self, laserStartPosition, laserDirection, wall):
        a1 = laserStartPosition.x
        b1 = laserStartPosition.y
        x1 = laserDirection.x
        y1 = laserDirection.y
        
        a2 = wall.startPosition.x
        b2 = wall.startPosition.y
        x2 = wall.direction.x
        y2 = wall.direction.y
        
        det = (x1 * y2) - (x2 * y1)
        if det == 0:
            return None
        
        t = (1.0 / det) * ((y2 * (a2 - a1)) + ((-1.0 * x2) * (b2 - b1)))
        if t < 0:
            return None
        
        poc = laserStartPosition + (t * laserDirection)
        x = [wall.startPosition.x, wall.endPosition.x]
        x.sort()
        y = [wall.startPosition.y, wall.endPosition.y]
        y.sort()
        if self.isInInterval(x[0], x[1], poc.x) and self.isInInterval(y[0], y[1], poc.y):
            squaredDistToPoc = (poc.x - laserStartPosition.x) ** 2 + (poc.y - laserStartPosition.y) ** 2
            return (poc, wall, squaredDistToPoc)
        
        return None
    
    # Collision resolution methods
    def computeReflectionVector(self, surfaceNormal, incidentDirection):
        return (2 * (surfaceNormal * incidentDirection)) * surfaceNormal - incidentDirection
        
    # Helper methods
    def isInInterval(self, start, end, position):
        return position >= start and position <= end
    
    def isTwoIntervalsOverlapping(self, a1, b1, a2, b2):
        return max(a1, a2) <= min(b1, b2)

        
    
    
