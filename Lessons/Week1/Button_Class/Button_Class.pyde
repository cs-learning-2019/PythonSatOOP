from Button import *

myButton = Button(200, 200, 300, 100, 255, 255, 0)

def setup():
    size(900, 900)
    
def draw():
    global myButton
    myButton.drawButton()
    
def mousePressed():
    global myButton
    
    if myButton.didClick(mouseX, mouseY):
        print("Yes we clicked on the button")
    else:
        print("You missed")
