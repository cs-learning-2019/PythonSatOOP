# Python OOP
# Week 1 HW
# Kavan Lam
# Sept 24, 2022

# Question 1
for num in range(2, 1601, 2):
    print(num)
    
# Question 2
number = 10
is_prime = True
if number <= 1:
    is_prime = False
    
for num in range(2, number):
    if (number % num == 0):
        is_prime = False
        break;

if is_prime == True:
    print("It is prime")
else:
    print("It is not a prime")
    
# Question 3
"""
We covered this in class. Just change the second if to elif.
"""

# Question 4
x = 10
y = 11
z = 12

if (x >= y and x <= z) or (x % 2 == 0):
    print("Cool")
elif (x % 2 != 0):
    print("bye")
elif x == 0:
    print("boom")
