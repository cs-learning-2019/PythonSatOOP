from Vector2D import *
from Ball import *
from Wall import *

class CollisionDetector:
    def wallAndBall(self, wall, ball):
        # First check to see if the ball is even in the rectangle spanned by the line
        if not self.isInInterval(wall.startPosition.x - wall.thickness, wall.endPosition.x + wall.thickness, ball.position.x) or \
        not self.isInInterval(wall.startPosition.y - wall.thickness, wall.endPosition.y + wall.thickness, ball.position.y):
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
        
    # Helper methods
    def isInInterval(self, start, end, position):
        return position >= start and position <= end
    
    def isTwoIntervalsOverlapping(self, a1, b1, a2, b2):
        return max(a1, a2) <= min(b1, b2)
        
    
    
