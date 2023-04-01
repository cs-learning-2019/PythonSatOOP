import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getMagnitude(self):
        return float(math.sqrt(self.x ** 2 + self.y ** 2))
    
    def getUnitVector(self):
        magnitude = self.getMagnitude()
        return Vector2D(self.x / magnitude, self.y / magnitude)
    
    def getNormalVector(self):
        return Vector2D(self.y, -1.0 * self.x)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    # We will use the * operator to represent dot product.
    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return (other.x * self.x) + (other.y * self.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2D(self.x * other, self.y * other)
    __rmul__ = __mul__
    
    def __str__(self):
        return str(self.x) + " " + str(self.y)
    
    
