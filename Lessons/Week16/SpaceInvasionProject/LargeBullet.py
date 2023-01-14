class LargeBullet():
    def <----- The method name ----->(self, x, y):
        self.x = <------ Easy one ------>
        self.y = <------ Easy one ------>
        self.speed = 5
        self.damage = 300
        self.type = "Large"
        self.length = 35
        self.width = 50
        
    def drawBullet(self):
        fill(242, 27, 242)
        rect(self.x, self.y, self.length, self.width)
    
    def moveBullet(self):
        self.y = self.y - self.speed
