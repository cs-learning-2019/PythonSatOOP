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
# 7) Images and sounds: Display images and play sound effects in processing (only do if we have extra time)

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
x = [300, 100]
y = [300, 150]

def setup():
    size(600, 600)

def draw():
    global x1, y1, x2, y2
    
    # Clear everything
    background(0, 0, 0)
    
    # Draw the circles
    # Idea is to use a for loop to go through each circle
    ellipse(x1, y1, 50, 50)
    ellipse(x2, y2, 50, 50)
    
    # Move the circles
    x1 = x1 + 3
    x2 = x2 + 3
    
    
    
    
