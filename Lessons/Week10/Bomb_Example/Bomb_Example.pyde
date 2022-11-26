# Python OOP
# Mid-term presentation Bomb example
# Kavan Lam
# Nov 26, 2022

class Bomb:
    def __init__(self, x, y, r, g, b, size, fuse):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.size = size
        self.fuse = fuse
        self.direction = 1 # 1 = Grow and -1 = Shrink
        self.didExplode = False
    
    def description(self):
        print("I am a bomb with a fuse time of " + str(fuse))
    
    def draw_bomb(self):
        fill(self.r, self.g, self.b)
        ellipse(self.x, self.y, self.size, self.size)
    
    def animate_bomb(self):   
          
        # Make the bomb pulse
        if self.didExplode == False:
            if self.direction == 1:
                self.size = self.size + 2
            else:
                self.size = self.size - 2
        
        if self.size > 100 and self.didExplode == False:
            self.direction = -1
        
        if self.size < 50 and self.didExplode == False:
            self.direction = 1
        
        # Process the fuse
        self.fuse = self.fuse - 1
        
        # Do this if this is the start of the explosive
        if self.fuse <= 0 and self.didExplode == False:
            self.size = 300
            self.r = 255
            self.didExplode = True
        # Do this if the bomb already exploded
        elif self.fuse <= 0 and self.didExplode == True and self.size > 0:
            self.size = self.size - 1
            self.r = self.r - 1
 
my_bomb = Bomb(400, 400, 0, 0, 0, 50, 100)
def setup():
    size(800, 800)

def draw():
    background(255, 255, 255)
    
    my_bomb.draw_bomb()
    my_bomb.animate_bomb()
