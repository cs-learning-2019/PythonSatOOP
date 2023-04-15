from Vector2D import *
from Ball import *
from Wall import *

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
        if distance <= (ball.radius + wall.thickness / 2.0):
            return True
        return False
    
    def ballAndBall(self, ball1, ball2):
        return dist(ball1.position.x, ball1.position.y, ball2.position.x, ball2.position.y) <= (ball1.radius + ball2.radius - 5)
    
    def wallAndSquare(self, wall, square):
        l = square.length
        boundingBall = Ball(square.position.x + l / 2.0, square.position.y + l / 2.0, l / 2.0, 0, Vector2D(0, 0))
        return self.wallAndBall(wall, boundingBall)
    
    # Collision resolution methods
    def computeReflectionVector(self, surfaceNormal, incidentDirection):
        return (2 * (surfaceNormal * incidentDirection)) * surfaceNormal - incidentDirection
        
    # Helper methods
    def isInInterval(self, start, end, position):
        return position >= start and position <= end
    
    def isTwoIntervalsOverlapping(self, a1, b1, a2, b2):
        return max(a1, a2) <= min(b1, b2)

        
    
    
