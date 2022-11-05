# Focus Learning
# Object-oriented programming in Python
# Kavan Lam
# Oct 22, 2022

# Contents
# 1) How to draw rectangles, circles, lines, text (font size and color) and colors
# 2) Animations: simple ball moving left to right
# 3) Animations: simple ball moving randomly
# 4) Animations: using list to animate multiple objects
# 5) User Interactions: move rectangle using WASD and arrow keys
# 6) User Interactions: make a circle change location when clicked on

# 1
"""
def setup():
    size(400, 500)
    
def draw():
    pushStyle()
    fill(95, 241, 247)
    rect(150, 50, 200, 60)
    ellipse(300, 300, 100, 50)
    text("Hello", 200, 200)
    popStyle()
    
    pushStyle()
    stroke(255, 0, 0)
    line(150, 50, 300, 300)
    popStyle()
""" 

# 2
"""
x = 50
y = 300

def setup():
    size(600, 600)

def draw():
    global x, y
    
    # Clear everything
    background(0, 0, 0)
    
    # Draw the circle
    ellipse(x, y, 50, 50)
    
    # Move the circle
    x = x + 3  # 3 is the speed (the bigger the number the fast the ball moves)
"""


# 3
"""
x = 300
y = 300

def setup():
    size(600, 600)

def draw():
    global x, y
    
    # Clear everything
    background(0, 0, 0)
    
    # Draw the circle
    ellipse(x, y, 50, 50)
    
    # Move the circle
    x = x + random(-15, 15)
    y = y + random(-15, 15)
"""

# 4
"""
x = [300, 100, 50]
y = [300, 150, 60]

def setup():
    size(600, 600)

def draw():
    global x, y
    
    # Clear everything
    background(0, 0, 0)
    
    # Draw the circles
    # Idea is to use a for loop to go through each circle
    for index in range(len(x)):
        ellipse(x[index], y[index], 50, 50)
    
    # Move the circles
    for index in range(len(x)):
        x[index] = x[index] + 1
        y[index] = y[index] + 1
"""

# 5
"""
x = 100
y = 100

def setup():
    size(600, 600)

def draw():
    background(0, 0, 0)
    
    rect(x, y, 50, 50)
    
def keyPressed():
    global x, y
    
    if key == "w" or key == "W":
        y = y - 7
    elif key == "s" or key == "S":
        y = y + 7
    elif key == "a" or key == "A":
        x = x - 7
    elif key == "d" or key == "D":
        x = x + 7
        
    
    if keyCode == UP:
        y = y - 7
    elif keyCode == DOWN:
        y = y + 7
    elif keyCode == LEFT:
        x = x - 7
    elif keyCode == RIGHT:
        x = x + 7
"""
# 6
x = 100
y = 100

def setup():
    size(800, 800)

def draw():
    background(0, 0, 0)
    ellipse(x, y, 50, 50) 

def mousePressed():
    global x, y
    if dist(mouseX, mouseY, x, y) <= 50:
        x = random(100, 700)
        y = random(100, 700)
        
        
    
        












    
    
    
    
