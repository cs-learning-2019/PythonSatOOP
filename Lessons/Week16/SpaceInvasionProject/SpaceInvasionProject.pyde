# Python OOP
# Space Invasion Project
# <------ Your name here ------->
# <------ The date here ------->

#############################
# If you finish the project early I challenge you to do the following...
# 1) Add a game over screen to the game that has a play again button
# 2) Make the aliens spawn faster as the player gets more score
# 3) Add a nuke to the game that kills all alien ships
# 4) Make the small alien ships move in a non straight line so it is harder to hit (need to make sure the ship does not leave the screen)
#########

from <------ Import something -------> import *
from <------ Import something -------> import *
from SmallAlienShip import *
from <------ Import something -------> import *

# Setup game objects and variables
earth = <------ Create a Earth object ------->
humanShip = HumanShip(350, 800, 300)
bullets = []
alienShips = []
score = <------ Variable to keep track of the score ------->
smallAlienSpawnTimer = 45
largeAlienSpawnTimer = 400
isGameOver = <------ Whether or not the game is over. This is a boolean. ------->

def setup():
    # The screen size should have a width of 950 and length of 700 (note length is horizontal)
    size(<---- A number ---->, <---- A number ---->)

def draw():
    global earth, humanShip, bullets, alienShips, score, smallAlienSpawnTimer, largeAlienSpawnTimer, isGameOver
    
    # Clear the previous frame by setting the background to black
    background(<---- A number ---->, <---- A number ---->, <---- A number ---->)
    
    if isGameOver is <---- Fill this in ---->:
        # Draw Earth
        earth.drawEarth()
        
        # Draw the ammo count, score and human ship health
        fill(255, 255, 255)
        textSize(20)
        text("Score: " + str(<----- The score ----->), 10, 30)
        text("Small Ammo: " + str(<----- The ammount of small ammo we have ----->), 10, 60)
        text("Large Ammo: " + str(<----- The ammount of large ammo we have ----->), 10, 90)
        text("Ship Health: " + str(<----- The ammount of health we have ----->), 10, 120)
        
        # Draw the human ship
        humanShip.x = mouseX
        <------ Draw the human ship (remeber this should be one line of code) ------>
        
        # Draw the alien ships
        for alienShip in alienShips:
            <------ Draw the alien ship ------>
        
        # Draw the bullets
        for <------ Fill this in ------>:
            <------ Draw the bullet ------>
        
        # Process bullets hitting aliens
        # Note: there are much better ways to do this but we do it like this for simplicity
        newBullets = []
        for bullet in bullets:
            didBulletHit = <-------- A boolean --------->
            newAlienShips = []
            for alienShip in alienShips:
                if isOverlapping(bullet.x, bullet.x + bullet.length, alienShip.x, alienShip.x + alienShip.size) and isOverlapping(bullet.y, bullet.y + bullet.width, alienShip.y, alienShip.y + alienShip.size):
                    alienShip.takeDamage(bullet.damage)
                    didBulletHit = <-------- A boolean --------->
                    if alienShip.health > 0:
                        <------- Do something so that the alien ship does not disappear ------->
                    else:
                        <------ Increase the score by 100 ------>
                    if bullet.type == "Large":
                        humanShip.largeAmmo = humanShip.largeAmmo + 1
                    else:
                        <------- This should be obvious ------->
                else:
                    newAlienShips.append(alienShip)
            alienShips = newAlienShips
            if didBulletHit == <------ A boolean ------>:
              newBullets.append(bullet)  
        bullets = newBullets
        
        # Process aliens hitting Earth
        # An alien ship has hit Earth if it's y position is equal to or more than 860
        <--------------- A bunch of code here ------------------>
        
        # Process aliens hitting human ship
        newAlienShips = []
        for alienShip in alienShips:
            if isOverlapping(humanShip.x - 40, humanShip.x + 40, alienShip.x, alienShip.x + alienShip.size) and isOverlapping(humanShip.y + 20, humanShip.y + 40, alienShip.y, alienShip.y + alienShip.size):
                humanShip.takeDamage(alienShip.damage)
            else:
                newAlienShips.append(alienShip)
        alienShips = newAlienShips
        
        # Process if the game is over (human ship or Earth has 0 or less than 0 health)
        if <----------- Fill this in ------------------>:
            isGameOver = <------- A boolean ------->
        
        # Move bullets
        newBullets = []
        for bullet in bullets:
            <-------- Move the bullet -------->
            if bullet.y > 0:
                newBullets.append(bullet)
            else:
                # In this case the bullet has not hit anything and has left the screen
                if bullet.type == "Large":
                    <---- Add back 1 large ammo to the human ship ---->
                else:
                    <---- Add back 1 small ammo to the human ship ---->
        bullets = newBullets
        
        # Move alien ships
        for <----- Fill this in ------>:
            <------- Move the alien ship ------->
        
        # Spawn aliens
        smallAlienSpawnTimer = smallAlienSpawnTimer - 1
        largeAlienSpawnTimer = largeAlienSpawnTimer - 1
        if smallAlienSpawnTimer <= 0:
            x = random(0, 680)
            newSmallAlienShip = SmallAlienShip(x, -10, 3, 100)
            alienShips.append(<------ Fill this in ------->)
            smallAlienSpawnTimer = 45
        
        if <------ Fill this in -------> <= 0:
            x = random(0, 620)
            newLargeAlienShip = LargeAlienShip(x, -10, 2, 400)
            alienShips.append(<------ Fill this in ------->)
            largeAlienSpawnTimer = 400
    
def keyPressed():
    global <--- Fill this in --->

    if <---- If the Z button is pressed on the keyboard ---->:
        humanShip.fireSmallBullet(bullets)
    elif <---- If the X button is pressed on the keyboard ---->:
        humanShip.fireLargeBullet(bullets)

# Helpful function to figure out if two intervals overlap
def isOverlapping(a1, b1, a2, b2):
    <--- Write some code here to make this function work (I can do it in one line but you can use more lines if you need) --->
    
