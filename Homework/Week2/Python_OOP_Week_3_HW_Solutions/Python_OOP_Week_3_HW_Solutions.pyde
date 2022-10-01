# Python OOP Week 2 HW solution
# Kavan Lam
# Oct 1, 2022

# Question 1 
nums = [2, 6, 1, 8, 4, 5, 6, 9, 1, 10]
for index in range(0, len(nums)):
    if (index - 1 < 0 or nums[index] > nums[index - 1]) and (index + 1 > len(nums) - 1 or nums[index] > nums[index + 1]):
        print(nums[index])
        break

# Question 2
names_and_ages = [["John", "Bob", "Sam"], [5, 8, 10]]
names = names_and_ages[0]
ages = names_and_ages[1]
for index in range(0, len(names)):
    print("Hello " + names[index] + ", you are " + str(ages[index]) + " years old")
    
# Question 3
names = ["Sally", "Bob", "Mila"]
for name in names:
    if "A" in name or "a" in name:
        print("Hello " + name + ", you have the letter eh in your name")

# Question 4
numbers = [[1, 2, 3, 4, 0], [3, 3, 3, 3, 3], [10, 12], [7]]
for sublist in numbers:
    total = 0
    for number in sublist:
        total = total + number
    print(total / len(sublist))

        
