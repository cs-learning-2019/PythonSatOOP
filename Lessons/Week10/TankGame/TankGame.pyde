# Python OOP
# Tanks
# Kavan Lam
# April 16, 2023

from CollisionProcessor import *
from Tank import *
from Cannon import *
from Ball import *
from Wall import *
from Square import *
from Color import *
from EasyTank import *
from HardTank import *

# Pre-defined colors
darkGreen = Color(95, 155, 28)
lightGreen = Color(168, 240, 87)
yellow = Color(255, 255, 0)
blue = Color(97, 184, 252)
red = Color(255, 0, 0)
brown = Color(196, 145, 14)
lightBrown = Color(240, 177, 17)
lightRed = Color(250, 103, 103)

# Define the walls
topWall = Wall(10, 10, 1690, 10, 20, blue)
bottomWall = Wall(10, 890, 1690, 890, 20, blue)
leftWall = Wall(10, 10, 10, 890, 20, blue)
rightWall = Wall(1690, 10, 1690, 890, 20, blue)
wall1 = Wall(1200, 200, 1400, 600, 20, blue)
walls = [topWall, bottomWall, leftWall, rightWall, wall1]

# Define everything else
cp = CollisionProcessor()
playerTank = Tank(200, 450, darkGreen, lightGreen, yellow, red)
bullets = []

#tank1 = EasyTank(1000, 450, brown, lightBrown, yellow, red)
tank2 = HardTank(1000, 650, red, lightRed, yellow, red)
badTanks = [tank2]

def setup():
    size(1700, 900)
    
def draw():
    global walls, cp, playerTank, bullets
    
    # Clear previous frame
    background(0, 0, 0)
    
    # Draw game objects
    playerTank.drawTank(walls)
    
    for wall in walls:
        wall.drawWall()
    
    for bullet in bullets:
        bullet.drawBullet()
        
    for tank in badTanks:
        tank.drawTank(walls)
        
    # Move game objects
    playerTank.moveTank(walls)
    
    for bullet in bullets:
        bullet.moveBullet()
    
    for tank in badTanks:
        tank.moveTank(walls)
        
    # Compute the next moves for AI tanks
    for tank in badTanks:
        tank.computeNextMove(walls, bullets, playerTank)
    
    # Hit detection between bullets and walls
    deadBullets = set()
    for i in range(len(bullets)):
        bullet = bullets[i]
        for wall in walls:
            if cp.wallAndBall(wall, bullet):
                bullet.numberOfBounces += 1
                if bullet.numberOfBounces >= 2:
                    deadBullets.add(i)
                    break
                else:    
                    bullet.direction = cp.computeReflectionVector(wall.normal, -1 * bullet.direction)
    computeNewBullets(deadBullets)
    
    # Hit detection between bullets themselves
    deadBullets = set()
    for i in range(len(bullets)):
        for j in range(len(bullets)):
            if i != j and cp.ballAndBall(bullets[i], bullets[j]):
                deadBullets.add(i)
                deadBullets.add(j)
    computeNewBullets(deadBullets)
    
def computeNewBullets(deadBullets):
    global bullets
    global playerTank
    
    newBullets = []
    for k in range(len(bullets)):
        if not k in deadBullets:
            newBullets.append(bullets[k])
        else:
            bullets[k].bulletOwner.bullets += 1
            
    bullets = newBullets
                
def keyPressed():
    global playerTank
    
    if type(key) == type(0):
        return
    
    if key.lower() == "w":
        playerTank.wasd[0] = 1
    elif key.lower() == "a":
        playerTank.wasd[1] = 1
    elif key.lower() == "s":
        playerTank.wasd[2] = 1
    elif key.lower() == "d":
        playerTank.wasd[3] = 1

def keyReleased():
    global playerTank
    
    if type(key) == type(0):
        return
    
    if key.lower() == "w":
        playerTank.wasd[0] = 0
    elif key.lower() == "a":
        playerTank.wasd[1] = 0
    elif key.lower() == "s":
        playerTank.wasd[2] = 0
    elif key.lower() == "d":
        playerTank.wasd[3] = 0
        
def mousePressed():
    global bullets
    
    bullet = playerTank.shoot()
    if bullet is not None:
        bullets.append(bullet)
    
    
