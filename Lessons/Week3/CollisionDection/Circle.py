class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def render(self):
        ellipse(self.x, self.y, 2*self.radius, 2*self.radius)
