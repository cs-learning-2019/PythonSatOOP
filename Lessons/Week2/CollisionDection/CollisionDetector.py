class CollisionDetector:
    # Main collision detector methods
    def circleAndPoint(self, circle, point):
        return dist(circle.x, circle.y, point.x, point.y) <= circle.radius

    def rectangleAndPoint(self, rectangle, point):
        return self.isInInterval(rectangle.x, rectangle.x + rectangle.length, point.x) and self.isInInterval(rectangle.y, rectangle.y + rectangle.width, point.y)
    
    def circleAndCircle(self, circle1, circle2):
        return dist(circle1.x, circle1.y, circle2.x, circle2.y) <= (circle1.radius + circle2.radius)
          
        
    # Helper methods
    def isInInterval(self, start, end, position):
        return position >= start and position <= end
    
    def isTwoIntervalsOverlapping(self, a1, b1, a2, b2):
        return max(a1, a2) <= min(b1, b2)
        
