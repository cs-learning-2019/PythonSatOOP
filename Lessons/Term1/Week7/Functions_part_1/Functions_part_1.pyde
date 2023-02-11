# Focus Learning Python OOP
# Functions part 1
# Kavan Lam
# Nov 5, 2022

# Ex 1
# Think of a function as a factory which will make something or do something.
# What the factory (function) produces or does is the output
# What the factory takes in is the input
# Every function start with a def also do not forget the brackets and :
def someStuff():
    print("Hello"*4)
    print("What's up!")
    
# To call the function simply use the name of the function
someStuff()
someStuff()

# print("dcsdchsbhdjcs")   print is also a function


# Ex 2
print("-----------------------------------------")
def multiply(num):
    print(num*7)
    
multiply(3)
multiply(5)
multiply(7)

print("-----------------------------------------")
def printLine(num_hash):
    print("#" * num_hash)
    
printLine(2)
printLine(4)
printLine(12)
printLine(12)
printLine(6)
printLine(2)

# Skill 3 Returning
print("-----------------------------------------")
def areaRect(l, w):
    print(l*w)
    return l*w

result = areaRect(2, 3)
print(result)

# Practice
def box_maker(num):
    # First row
    print("* " * num)
    
    # In between the first and last rows
    for i in range(num - 2):
        print("*" + " " * (num - 2) + "*")
    
    # Last row
    print("* " * num)
    
box_maker(8)
    
