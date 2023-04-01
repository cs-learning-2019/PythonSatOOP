from Vector2D import *
from Ball import *
from Wall import *

class CollisionDetector:
    # Question 2 (hit detection between a wall and ball)
    def wallAndBall(self, wall, ball):
        return False
            
    # Question 3 (hit detection between a wall and square)
    def wallAndSquare(self, wall, square):
        pass
        
    # Helper methods
    def isInInterval(self, start, end, position):
        return position >= start and position <= end
    
    def isTwoIntervalsOverlapping(self, a1, b1, a2, b2):
        return max(a1, a2) <= min(b1, b2)
        
    
    
