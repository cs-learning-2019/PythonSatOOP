class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def render(self):
        pushStyle()
        strokeWeight(10)
        point(self.x, self.y)
        popStyle()
