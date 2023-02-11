add_library("minim")
from SoundManager import *

minim = Minim(this)
sm = SoundManager(minim)

def setup():
    size(900, 900)
    minim = Minim(this)
    sound1 = minim.loadFile("Deep Logic.wav")
    sm = SoundManager(sound1)
    sm.playMainMusic()
    
def draw():
    rect(100, 100, 60, 50)

def mouseWheel(e):
    print(e.getCount())
