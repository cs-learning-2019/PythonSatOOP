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

# Question 2 and 3 (Define the walls)
topWall = Wall(10, 10, 890, 10, 10)
bottomWall = 0 # You can figure this out
leftWall = 0 # You can figure this out
rightWall = 0 # You can figure this out
walls = [topWall, bottomWall, leftWall, rightWall]

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
    
    # Question 1 (modify the direction of each ball depending on its position)

    
    # Question 2 (go through each ball and detect if the ball hits a wall and modify the direction)
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
    
    # Question 3 (go through each square and detect if the square hits a wall and modify the direction)

def mousePressed():
    global cannon

    newBall = Ball(cannon.endPosition.x, cannon.endPosition.y, 15, 5, cannon.directionVector)
    balls.append(newBall)
    
