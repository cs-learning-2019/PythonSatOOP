# Focus Learning - OOP
# Week 1: Review if statements and loops
# Kavan Lam
# Sept 17, 2022

################ Review data types ################
# In python we have a bunch of built-in data types. Here are some of them
a = 10 #int
b = "12#$&Hello" #String
c = True # Boolean
d = False # Boolean
e = 10.5 #Float
f = [1, 2, 3, 4] #List
g = {"x" : 1, "y" : 2} #Dict

# We can convert between different data types
x = 10
x_string = str(x)

y = "20"
y_integer = int(y)

z = 10.8
z_integer = int(z)

# bad_num = int("12a")  when converting to a number you have to make sure the string represents a proper number

# String concatenation
print("Hello" + " there")

# print ("I am " + 5 + " years old") # we are not allowed to add strings with numbers. How do we fix this? Answer: we convert the number into a string.



################ Review if statements ################
print("--------------------------------------------------------------------")
# 1) Basic example of if statement with age
age = 8
if age >= 10:
    print("You are older than 9")
else: 
    print("You have an age")
    
# 2) Explain elif keyword
age = 20
if age >= 20:
    print("You are old")
elif age >= 13:
    print("You are a teen")
else: 
    print("You are young")

# 3) Logical operator (and, or, not) (look at examples involving even and odd numbers)
x = 10
y = 5
if (x % 2 == 0 and y % 2 != 0):  # if x is even and y is odd
    print("Great")
else:
    print("Wow")



################ Review for loops ################
print("--------------------------------------------------------------------")
# 1) Basic example (print "Hello" 10 times)
for i in range(10):
    print("Hello")
    
# 2) What is the range function?
# Special function that gives you the ability to create a range of numbers
print(range(10))
print(range(1, 11))
print(range(2, 16, 2))

# 3) For loop on a range of numbers
for number in range(2, 10):
    print(number)
    
# 4) For loop on a string
for character in "Hello":
    print(character)


################ Review while statements ################
print("--------------------------------------------------------------------")
# 1) Basic example (loop while cash is greater than 0)
cash = 10
while (cash > 0):
    print("buy something")
    cash = cash - 1


################ Additional questions if we have time ################
print("--------------------------------------------------------------------")
# 1) Use for loops to print out a 12x12 multiplication times table
# 2) Loop over the digits of a positive int without converting to a string
# 3) Find all the factors of a positive integer
