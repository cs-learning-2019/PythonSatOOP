# Python OOP
# Collision Detection
# Kavan Lam
# Feb 25, 2023

from CollisionDetector import *
from Circle import *
from Point import *
from Rectangle import *

cd = CollisionDetector()

def setup():
    global cd
    
    size(900, 900)
    
    c = Circle(700, 700, 100)
    c2 = Circle(600, 600, 150)
    p = Point(400, 125)
    r = Rectangle(100, 100, 50, 50)
    
    print(cd.circleAndCircle(c, c2))
    
def draw():
    pass

"""
  - point and circle
  - point and rectangle
  - circle and circle
  - rectangle and rectangle
  - rectangle and circle
  - ball bouncing off a horizontal or vertical wall
"""
