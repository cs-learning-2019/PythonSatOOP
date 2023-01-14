class SmallBullet():
    def __init__(self, x, y):
        self.x = <------ Easy one ------>
        self.y = <------ Easy one ------>
        self.speed = 7
        self.damage = 100
        self.type = "Small"
        self.length = 20
        self.width = 50
        
    def drawBullet(self):
        fill(255, 255, 255)
        rect(self.x, self.y, self.length, self.width)
    
    def moveBullet(self):
        self.y = self.y - self.speed
