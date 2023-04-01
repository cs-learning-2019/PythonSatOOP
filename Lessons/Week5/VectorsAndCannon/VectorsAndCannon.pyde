# Python OOP
# Vectors and Cannon
# Kavan Lam
# March 10, 2023

from Cannon import *
from Ball import *
from Wall import *

cannon = Cannon(450, 450)
balls = []
walls = [Wall(100, 100, 200, 200, 5)]

def setup():
    size(900, 900)
    
def draw():
    global cannon, walls, balls

    # Clear previous frame
    background(0, 0, 0)
    
    # Draw objects
    cannon.drawCannon()
    
    for ball in balls:
        ball.drawBall()
        
    for wall in walls:
        wall.drawWall()
        wall.drawNormal()
        
    # Move objects
    for ball in balls:
        ball.updatePosition()
    
def mousePressed():
    global cannon
    
    newBall = Ball(cannon.endPosition.x, cannon.endPosition.y, 15, 5, cannon.directionVector)
    balls.append(newBall)
    
    
    
    
    
    
    
    
