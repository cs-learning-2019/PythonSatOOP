# Focus Learning
# Object oriented programming in Python
# Kavan Lam
# Oct 15, 2022

############# Set and Tuples #############
# A set is like a dictionary but only the keys
# Sets do not use index
# Sets are unordered
# Sets do not have duplicates
# Sets have very fast lookup times when compared to a list
print("------------------------------------------------------------------------")
names = {"John", "Kelly", "Mark"}
names.add("Bob")
names.discard("Kelly")
print(names)
print("Is Mark in the set? --> " + str("Mark" in names))

# We can do intersections, union and difference operations
print("------------------------------------------------------------------------")
ages1 = {1, 2, 3, 4, 5, 6, 1, 2}
ages2 = {5, 6, 7, 8}
print(ages1)
print(ages2)
print("The intersection is " + str(ages1.intersection(ages2)))
print("The union is " + str(ages1.union(ages2)))
print("The difference is between ages1 and ages2 " + str(ages1.difference(ages2)))
print("The difference is between ages2 and ages1 " + str(ages2.difference(ages1)))

# Tuples
# Basically a list but we can not add, remove or change items in the tuple
# Tuples can have duplicates
# Tuples are faster than List
# Tuples are great for ensuring that a given collection of data is protected and read-only
print("------------------------------------------------------------------------")
things = (2, 6, "John", True, "John", 2, 7, 9)
print(things)
print("Is John in things? --> " + str("John" in things))
print(things[1])
#things[1] = 100 # This will not work since we can not change items in a tuple

# List Comprehension
# Basically it is shortcuts when working with list, specifically making list
print("------------------------------------------------------------------------")
# This is the normal way to create a list of square numbers
nums = []
for number in range(11):
    nums.append(number ** 2)
print(nums)

# This is the same thing but using list comprehension
print("------------------------------------------------------------------------")
better_nums = [number ** 2 for number in range(11)]
print(better_nums)

# We can even do a simple if statement in the list comprehension
print("------------------------------------------------------------------------")
more_nums = [number ** 2 for number in range(11) if number % 2 == 0]
print(more_nums)

# The general form is...
# newlist = [<result> for <item> in <iterable> if <condition>]

# Here is a more complicated example involving nested list comprehension
print("------------------------------------------------------------------------")
multiply = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i * j)
    multiply.append(row)

print(multiply)

print("------------------------------------------------------------------------")
better_multiply = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(better_multiply)

# Here is another example of nested list comprehension
print("------------------------------------------------------------------------")
big_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = []
for row in big_list:
    for number in row:
        flat_list.append(number)
print(flat_list)
        
print("------------------------------------------------------------------------")
big_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [number for row in big_list for number in row]
print(flat_list)

# Sample problems to work on
print("------------------------------------------------------------------------")
# Dogs like even numbers between 2 and 10 inclusive
# Cats like all numbers between 0 and 100
# Birds like the number 4, 5 and 20
# Rats like all numbers between 4 and 19 inclusive
# Find all the numbers that are liked by all animals


print("------------------------------------------------------------------------")
# For each case decide if we should use a tuple or list to store the collection
# A bunch of age groups that will be used for an experiment -->
# The planets in our solar system -->
# Live information about a user's failed login attempt -->
# Live information about the enemies in a game -->
# The primary colors -->

print("------------------------------------------------------------------------")
# We have a 2D list of numbers
# We want to go through the whole list and collect all the positive numbers into a 1D list
# Please use list comprehension
sample_2d_list = [[-1, 2, 6, 4], [0, -5, -2, 1], [5, 9], [0, -9, -7]]












    
    
    
