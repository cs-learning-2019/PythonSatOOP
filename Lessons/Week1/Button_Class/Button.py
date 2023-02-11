class Button:
    def __init__(self, x, y, l, w, r, g, b):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.r = r
        self.g = g
        self.b = b
    
    def drawButton(self):
        fill(self.r, self.g, self.b)
        rect(self.x, self.y, self.l, self.w)
    
    def didClick(self, x, y):
        return x >= self.x and x <= self.x + self.l and y >= self.y and y <= self.y + self.w
        
