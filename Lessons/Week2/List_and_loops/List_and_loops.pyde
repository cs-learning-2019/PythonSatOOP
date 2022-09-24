# Object oriented programming in Python
# Week2: Python List and more loops
# Kavan Lam
# Sept 24, 2022

################# Simple 1D List and the basics #################
print("-----------------------------------------------------------------------------")
ages = [8, 9, 1, 5]
print(ages[0])
print(ages[-1])
print(ages[2])
ages[2] = 1000
print(ages[2])
# print(ages[10]) not good since we don't have index 10

for num in ages:
    print("Hi my age is " + str(num))  # Remeber to convert num into a string since you are adding it with a string
    
print("-----------------------------------------------------------------------------")

names = ["John", "Kelly", "Bob", "Kate"]
for index in range(0, 4):  # ----> Is there a better way to setup this for loop?
    print("Hi my name is " + names[index] + " and I am " + str(ages[index]) + " years old")
    
    
    
# Practice Question for you to work on in class
print("-----------------------------------------------------------------------------")
"""
You have a 1D list of numbers. Write some code that changes the list so every number is doubled.
"""
numbers = [1, 2, 3, 4, 5, 6, 7]

# SOME CODE HERE TO DOUBLE THE NUMBERS

print(numbers)  #--> We expect to see [2, 4, 6, 8, 10, 12, 14]



# How can we delete and insert into a Python List?
print("-----------------------------------------------------------------------------")
animals = ["Dog", "Cat", "Fish"]
animals.append("Rat")
animals.insert(1, "Spider")
print(animals)

animals.pop(2)
print(animals)


########################## 2D Python List ##########################
print("-----------------------------------------------------------------------------")
students_per_room = [["A", "B", "C"], ["X", "Y", "Z"], ["F", "G", "H"]]
print(students_per_class[1][2])
print(students_per_class[0][0])
print(students_per_class[-1][-1])

# How can we print every letter out?
for room in students_per_room:
    for student in room:
        print("Hi I am student: " + student)


########################## Solving Problems ##########################
print("-----------------------------------------------------------------------------")
"""
Given a 1D list of positive integers create a 2D list with 2 sublist. The first sublist contains the even
numbers and the second contains the odd numbers.
"""
numbers = [2, 3, 4, 5, 6, 7, 8, 9]





print("-----------------------------------------------------------------------------")
"""
Given a 2D list of integers determine if the number at a given position is a peak
The number is a peak if it is greater than or equal to its top, bottom, left and right neighbours
"""
numbers = [[3, 1, 7, 2], [2, 9, 10, 5], [11, 12, 13, 0]]
row = 1
col = 2
