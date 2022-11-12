# Python OOP
# Week 7 HW solutions
# Kavan Lam
# Nov 12, 2022

# Question 1
"""
1) You are calling the function with only 1 input
2) 1z is not a proper variable name
3) We are missing :
4) We never actually use the variable 1z
"""

# Question 2
def is_all_negative(num_list):
    for number in num_list:
        if number >= 0:
            return False
    
    return True

# Question 3
def question3(str_list, num):
    for word in str_list:
        if len(word) == num:
            return True
    
    return False
    
    
print(question3(["Hi", "Bye", "Kitty"], 10))

# Question 4
def setup():
    size(800, 800)

def draw():
    draw_triangle(100, 100, 100, 20, 300, 100)

def draw_triangle(x1, y1, x2, y2, x3, y3):
    line(x1, y1, x2, y2)
    line(x2, y2, x3, y3)
    line(x3, y3, x1, y1)
