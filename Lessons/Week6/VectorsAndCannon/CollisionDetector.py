from Vector2D import *
from Ball import *
from Wall import *

class CollisionDetector:
    # Question 2 (hit detection between a wall and ball)
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
    
    def computeReflectionVector(self, surfaceNormal, incidentDirection):
        return (2 * (surfaceNormal * incidentDirection)) * surfaceNormal - incidentDirection
            
    # Question 3 (hit detection between a wall and square)
    def wallAndSquare(self, wall, square):
        pass
        
    # Helper methods
    def isInInterval(self, start, end, position):
        return position >= start and position <= end
    
    def isTwoIntervalsOverlapping(self, a1, b1, a2, b2):
        return max(a1, a2) <= min(b1, b2)
        
    
    
