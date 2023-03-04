from Rectangle import *

class CollisionDetector:
    # Main collision detector methods
    def circleAndPoint(self, circle, point):
        return dist(circle.x, circle.y, point.x, point.y) <= circle.radius

    def rectangleAndPoint(self, rectangle, point):
        return self.isInInterval(rectangle.x, rectangle.x + rectangle.length, point.x) and self.isInInterval(rectangle.y, rectangle.y + rectangle.width, point.y)
    
    def circleAndCircle(self, circle1, circle2):
        return dist(circle1.x, circle1.y, circle2.x, circle2.y) <= (circle1.radius + circle2.radius)
    
    def rectangleAndRectangle(self, rect1, rect2):
        isOverlappingInXdirection = self.isTwoIntervalsOverlapping(rect1.x, rect1.x + rect1.length, rect2.x, rect2.x + rect2.length)
        isOverlappingInYdirection = self.isTwoIntervalsOverlapping(rect1.y, rect1.y + rect1.width, rect2.y, rect2.y + rect2.width)
        return isOverlappingInXdirection and isOverlappingInYdirection
          
    def rectangleAndCircle(self, rectangle, circle):
        # Create a bounding rectangle for the circle
        boundingBox = Rectangle(circle.x - circle.radius, circle.y - circle.radius, 2 * circle.radius, 2 * circle.radius)
        
        # Check if the rectangle is touching the bounding box
        return self.rectangleAndRectangle(rectangle, boundingBox)
        
    # Helper methods
    def isInInterval(self, start, end, position):
        return position >= start and position <= end
    
    def isTwoIntervalsOverlapping(self, a1, b1, a2, b2):
        return max(a1, a2) <= min(b1, b2)
        
