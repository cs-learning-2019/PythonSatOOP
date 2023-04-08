# Python OOP
# Vectors and Cannon
# Kavan Lam
# March 10, 2023

from CollisionDetector import *
from Cannon import *
from Ball import *
from Wall import *

cd = CollisionDetector()
cannon = Cannon(450, 450)
balls = []

topWall = Wall(10, 10, 890, 10, 10)
bottomWall = Wall(10, 890, 890, 890, 10)
leftWall = Wall(10, 10, 10, 890, 10)
rightWall = Wall(890, 10, 890, 890, 10)
slantedWall1 = Wall(100, 100, 200, 150, 10)
walls = [topWall, bottomWall, leftWall, rightWall, slantedWall1]

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
        
    # Move objects
    for ball in balls:
        ball.updatePosition()
    
    for ball in balls:
        # Check top side
        if cd.wallAndBall(topWall, ball):
            ball.direction.y = ball.direction.y * -1.0
        # Check bottom side
        elif cd.wallAndBall(bottomWall, ball):
            ball.direction.y = ball.direction.y * -1.0
        # Check left side
        elif cd.wallAndBall(leftWall, ball):
            ball.direction.x = ball.direction.x * -1.0
        # Check right side
        elif cd.wallAndBall(rightWall, ball):
            ball.direction.x = ball.direction.x * -1.0
        
        if cd.wallAndBall(slantedWall1, ball):
            reflectionVector = cd.computeReflectionVector(slantedWall1.normal, -1 * ball.direction)
            ball.direction = reflectionVector

def mousePressed():
    global cannon
    
    newBall = Ball(cannon.endPosition.x, cannon.endPosition.y, 15, 5, cannon.directionVector)
    balls.append(newBall)
    
