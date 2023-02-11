# Focus Learning: Python OOP
# Finishing up functions
# Kavan Lam
# Nov 12, 2022

# Default Parameters
print("-------------------------------")
def try_me(x=5, y=2):
    return x - y

print(try_me(y=10, x=2))

print("-------------------------------")
def double_me(x = 2, y = 1):
    return (x * 2) + (y * 2)

print(double_me(3))

print("-------------------------------")
def sum_of_three(x = 1, y = 10, z = 1):
    return x + y + z

print(sum_of_three(3, 1))

# Using more than one function to solve a problem
print("-------------------------------")
def part1(x):
    return x * 10 / 2

def part2(x):
    return x * x

def part3(x):
    return 4 * x * x * x

def all_together(x):
    return part1(x) + part2(x) + part3(x)

print(all_together(5))

print("--------------------------------")
grades = [100, 40, 10, 0, 100, 100, 100, 90]

def average_grade(list_of_grades):
    return sum(list_of_grades) / len(list_of_grades)

def min_grade(list_of_grades):
    return min(list_of_grades)

print(average_grade(grades))
print(min_grade(grades))

# Lets solve a few problems with functions
"""
Write a function that takes 8 numbers. The first 4 numbers are the top left position
of a rectangle followed by the length and width. The last 4 numbers is the same but for a different rectangle.
The function will return true if the rectangles hit each other and false otherwise
"""
print("--------------------------------")
def overlap(x1, y1, l1, w1, x2, y2, l2, w2):
    g1a = x1
    g1b = x1 + l1
    
    g2a = x2
    g2b = x2 + l2
    
    r1a = y1
    r1b = y1 + w1
    
    r2a = y2
    r2b = y2 + w2
    
    if max(g1a, g2a) <= min(g1b, g2b) and max(r1a, r2a) <= min(r1b, r2b):
        return True
    else:
        return False
print(overlap(100, 50, 50, 60, 50, 80, 75, 40))

"""
Write a function that takes in a string which represents a code. The function will return True if the code is valid
and False otherwise. A code is valid if it starts with a capital letter and is followed by 5 digits. No punctuation or
spaces can appear in the code. If the leading capital letter is an "A" or "B" then the 5 digits after must added up to
larger than 13 and also the digits must appear in increasing order (ie/ From left to right the 5 digits 15779 is
increasing, but 57910 is not). If the first letter is not an "A" or "B" then the 5 digits after only have to add up to
less than or equal to 23.
"""
def starts_with_capital_letter(code):
    capital_letters = ["A", "B", "C", "D", ......]
    if code[0] in capital_letters:
        return True
    else:
        return False

def has_5_digits(code):
    if len(code) == 6 and code[1:].isnumeric():
        return True
    else:
        return False

def no_spaces_no_punctuation(code):
    punctuation = [",", ".", .....]
    
    for punc in punctuation:
        if punc in code:
            return False
        
    if " " not in code:
        return True
    else:
        return False

def main_function(code):
    if starts_with_capital_letter(code) and has_5_digits(code) and no_spaces_no_punctuation(code) and blah and blah:
        return true
    else:
        return false
