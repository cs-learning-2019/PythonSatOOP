# https://code.compartmental.net/minim/

add_library("minim")
from SoundManager import *

sm = SoundManager()
keysAndFileNames = [("mainMusic", "Deep Logic.wav"), ("endMusic", "End Game.wav"), ("score", "Score.wav")]

def setup():
    global keysAndFileNames, sm
    
    # Set the screen size
    size(900, 900)
    
    # Load all sound files and initialize the sound manager
    minim = Minim(this)
    for keyAndFileName in keysAndFileNames:
        sound = minim.loadFile(keyAndFileName[1])
        sm.addSound(keyAndFileName[0], sound)
    
    # Start playing the main music
    sm.playMainMusic()
    
def draw():
    rect(100, 100, 60, 50)

def mousePressed():
    global sm
    sm.playScore()

def keyPressed():
    global sm
    
    # Press W to go to the game over sound and S to go back to main music
    if key == "W":
        sm.stopMainMusic()
        sm.playSound("endMusic")
    elif key == "S":
        sm.stopEndMusic()
        sm.playMainMusic()
    
        
    
    
    
