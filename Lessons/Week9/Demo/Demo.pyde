# Python OOP
# Easy Tank AI Demo
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

topWall = Wall(10, 10, 890, 10, 10)
bottomWall = Wall(10, 890, 890, 890, 10)
leftWall = Wall(10, 10, 10, 890, 10)
rightWall = Wall(890, 10, 890, 890, 10)
walls = [topWall, bottomWall, leftWall, rightWall]

greenBallX = 450
greenBallY = 600
greenBallGoalX = 200
greenBallGoalY = 200

def setup():
    size(900, 900)
    
def draw():
    global cannon, walls, balls, squares, greenBallX, greenBallY, greenBallGoalX, greenBallGoalY

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
    
    pushStyle()
    fill(0, 255, 0)
    ellipse(greenBallX, greenBallY, 50, 50)
    popStyle()
    
    # Green Ball AI
    moves = [(0, 0), (5, 0), (-5, 0), (0, 5), (0, -5)]
    bestMove = (0, 0)
    bestScore = None
    for move in moves:
        score = 0
        newX = greenBallX + move[0]
        newY = greenBallY + move[1]
        if newX > 850 or newX < 50 or newY > 850 or newY < 50:
            continue 
        
        # Consider the bullets
        for ball in balls:
            distance = dist(newX, newY, ball.position.x, ball.position.y)
            if distance == 0:
                value = -999999
            else:
                value = -1.0 / distance
            score += value
            
        # Consider the goal
        distance = dist(newX, newY, greenBallGoalX, greenBallGoalY)
        if distance == 0:
            value = 999999
        else:
            value = 1.0 / distance
        score += value
        
        if bestScore == None or bestScore < score:
            bestScore = score
            bestMove = move
    greenBallX = greenBallX + bestMove[0]
    greenBallY = greenBallY + bestMove[1]        
    
    # Ball collision detection
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
            
def mousePressed():
    global cannon
    
    newBall = Ball(cannon.endPosition.x, cannon.endPosition.y, 15, 5, cannon.directionVector)
    balls.append(newBall)
    
