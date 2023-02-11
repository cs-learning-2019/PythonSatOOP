# Object oriented programming in Python
# Week 3: Python Dictionaries
# Kavan Lam
# Oct 1, 2022

################# Basics of Dictionaries #################
print("--------------------------------------------------------------------------")
name = ["Bob", "Kelly", "James"]
age = [5, 8, 7]

# Instead of using two list to hold the data we can use a dictionary to hold it all on one object.
name_to_age = {"Bob": 5, "Kelly": 8, "James": 7}
print(name_to_age)
print(name_to_age["Bob"])
#print(name_to_age["bob"])  --> Dictionaries are case-sensitive so this won't work
name_to_age["Bob"] = 55
print(name_to_age["Bob"])
name_to_age.pop("Bob")
print(name_to_age)
print(name_to_age.keys())

print("--------------------------------------------------------------------------")
# Looks easy right? Well there are a couple things we need to cover.
# First, some basic terminology. Each thing in the dictionary is called
# a key-value pair. For example, "a": 1 is a key-value pair. The key is "a"
# and 1 is the value. To get to the 1 you must have/know the key which is "a".
# Second, the keys in a dictionary must be unique so this means no duplicates.
# If there are duplicates then the latest one is used and previous one is removed.
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.keys(), " Ok so far it makes sense.")
my_dict["hello"] = 12
my_dict["bye"] = 1
my_dict["abc"] = 99
print(my_dict)
print(my_dict.keys(), " Still good!!")
print("--------------------------------------------------------------------------")

################# Looping through a Dictionaries #################
print("--------------------------------------------------------------------------")
name_to_age = {"Bob": 5, "Kelly": 8, "James": 7}
for name in name_to_age.keys():
    print("Hi my name is " + name + " and I am " + str(name_to_age[name]) + " years old.")
    
# Notice how the order is James, Kelly and then Bob? This is usually the case when you work with dictionaries, hash maps and etc.
# Bob should be first but instead James is printed first.
# You will learn more about this in my advanced course Python course.

################# Converting data into a dictionary #################
print("--------------------------------------------------------------------------")
town = ["A", "B", "C"]
people = [100, 200, 300]
town_to_people = {}
for index in range(0, len(town)):
    town_to_people[town[index]] = people[index]

print(town_to_people)

################# Determine all the duplicates letters in a string #################
print("--------------------------------------------------------------------------")
sentence = "hello james, i am very scared of python"
letters = {}

for character in sentence:
    if character == " " or character == ",":
        continue
    
    if character in letters:
        letters[character] = letters[character] + 1
    else:
        letters[character] = 1

print(letters)
