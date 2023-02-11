# Focus Learning
# Week 5 HW solutions
# Kavan Lam
# Nov 5, 2022

# Question 1
"""
x = [100, 100, 100]
y = [100, 200, 300]

def setup():
    size(800, 800)
    
def draw():
    background(0, 0, 0)
    
    for index in range(0, len(x)):
        ellipse(x[index], y[index], 50, 50)
    
    for index in range(0, len(x)):
        x[index] = x[index] + random(-3, 3)
        y[index] = y[index] + random(-3, 3)
"""

# Question 2
"""
clicked = False
def setup():
    size(800, 800)
    
def draw():
    background(0, 0, 0)
    
    if clicked == False:
        pushStyle()
        fill(0, 0, 200)
        rect(300, 350, 200, 50)
        popStyle()
        
        pushStyle()
        fill(255, 0, 0)
        text("Click me", 380, 380)
        popStyle()

def mousePressed():
    global clicked
    clicked = True
"""

# Question 3
x = [100, 300, 500]
y = [100, 200, 300]
direction = [1, -1, 1]

def setup():
    size(800, 800)
    
def draw():
    global x, y, direction
    background(0, 0, 0)
    
    for index in range(0, len(x)):
        ellipse(x[index], y[index], 50, 50)
    
    for index in range(0, len(x)):
        y[index] = y[index] + (direction[index] * 3)
        
    for index in range(0, len(x)):
        if y[index] <= 0:
            direction[index] = 1
        elif y[index] >= 800:
            direction[index] = -1

def mousePressed():
    global x, y, direction
    new_x = []
    new_y = []
    new_direction = []
    for index in range(0, len(x)):
        distance = dist(mouseX, mouseY, x[index], y[index])
        if distance > 50:
            new_x.append(x[index])
            new_y.append(y[index])
            new_direction.append(direction[index])
    x = new_x
    y = new_y
    direction = new_direction
    
    
    
    
