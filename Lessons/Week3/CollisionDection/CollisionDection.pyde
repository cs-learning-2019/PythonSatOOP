# Python OOP
# Collision Detection
# Kavan Lam
# Feb 25, 2023

from CollisionDetector import *
from Circle import *
from Point import *
from Rectangle import *

cd = CollisionDetector()
circle1 = Circle(190, 190, 50)
circle2 = Circle(600, 600, 85)
p = Point(550, 600)
rectangle1 = Rectangle(100, 100, 50, 50)
rectangle2 = Rectangle(50, 50, 100, 55)
objects = [circle1, rectangle1]

# point and circle
print(cd.circleAndPoint(circle2, p))

# point and rectangle
print(cd.rectangleAndPoint(rectangle1, p))

# circle and circle
print(cd.circleAndCircle(circle1, circle2))

# rectangle and rectangle
print(cd.rectangleAndRectangle(rectangle1, rectangle2))

# rectangle and circle
print(cd.rectangleAndCircle(rectangle1, circle1))

def setup():
    global cd
    size(900, 900)
    
def draw():
    global objects
    
    for object in objects:
        object.render() 
