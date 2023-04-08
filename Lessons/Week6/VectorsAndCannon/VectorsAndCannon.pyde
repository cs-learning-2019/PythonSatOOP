# Python OOP
# Vectors and Cannon
# Kavan Lam
# March 10, 2023

from CollisionDetector import *
from Cannon import *
from Ball import *
from Wall import *
from Square import *

cd = CollisionDetector()
cannon = Cannon(450, 450)
balls = []


# Question 2 and 3 (Define the walls)
topWall = Wall(10, 10, 890, 10, 10)
bottomWall = Wall(10, 890, 890, 890, 10)
leftWall = Wall(10, 10, 10, 890, 10)
rightWall = Wall(890, 10, 890, 890, 10)
slantedWall1 = Wall(100, 100, 200, 150, 10)
walls = [topWall, bottomWall, leftWall, rightWall, slantedWall1]

square1 = Square(100, 100, 50, 5, Vector2D(0, 1))
squares = [square1]

def setup():
    size(900, 900)
    
def draw():
    global cannon, walls, balls, squares

    # Clear previous frame
    background(0, 0, 0)
    
    # Draw objects
    cannon.drawCannon()
    
    for ball in balls:
        ball.drawBall()
    
    for s in squares:
        s.drawSquare()
        
    for wall in walls:
        wall.drawWall()
        
    # Move objects
    for ball in balls:
        ball.updatePosition()
        
    for s in squares:
        s.updatePosition()
    
    # Question 1 (modify the direction of each ball depending on its position)
    """
    for ball in balls:
        # Check top side
        if ball.position.y <= 0:
            ball.direction.y = ball.direction.y * -1.0
        # Check bottom side
        elif ball.position.y >= 900:
            ball.direction.y = ball.direction.y * -1.0
        # Check left side
        elif ball.position.x <= 0:
            ball.direction.x = ball.direction.x * -1.0
        # Check right side
        elif ball.position.x >= 900:
            ball.direction.x = ball.direction.x * -1.0
    """
    
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
        
        if cd.wallAndBall(slantedWall1, ball):
            reflectionVector = cd.computeReflectionVector(slantedWall1.normal, -1 * ball.direction)
            ball.direction = reflectionVector

    # Question 3 (go through each square and detect if the square hits a wall and modify the direction)
    for s in squares:
        l = s.length
        ball = Ball(s.position.x + l / 2.0, s.position.y + l / 2.0, l / 2.0, 0, Vector2D(0, 0))
        # Check top side
        if cd.wallAndBall(topWall, ball):
            s.direction.y = s.direction.y * -1.0
        # Check bottom side
        elif cd.wallAndBall(bottomWall, ball):
            s.direction.y = s.direction.y * -1.0
        # Check left side
        elif cd.wallAndBall(leftWall, ball):
            s.direction.x = s.direction.x * -1.0
        # Check right side
        elif cd.wallAndBall(rightWall, ball):
            s.direction.x = s.direction.x * -1.0
        

def mousePressed():
    global cannon
    
    newBall = Ball(cannon.endPosition.x, cannon.endPosition.y, 15, 5, cannon.directionVector)
    balls.append(newBall)
    
