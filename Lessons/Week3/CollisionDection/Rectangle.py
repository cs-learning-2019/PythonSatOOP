class Rectangle:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
    
    def render(self):
        rect(self.x, self.y, self.length, self.width)
