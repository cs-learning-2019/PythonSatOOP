# Focus Learning
# Week 3 HW Solutions
# Kavan Lam
# Oct 15, 2022

# Question 1
name_and_ages = ["Bob", 5, "James", 6, "Kate", 10]
names_to_ages = {}
for index in range(0, len(name_and_ages) - 1, 2):
    names_to_ages[name_and_ages[index]] = name_and_ages[index + 1]
    
print(names_to_ages)

# Question 2
print("-----------------------------------------------------")
names_to_ages = {"Bob": 5, "James": 6, "Kate": 10, "John": 20, "Tony": 2}
num_of_young_people = 0
for name in names_to_ages.keys():
    if names_to_ages[name] < 10:
        num_of_young_people = num_of_young_people + 1
        
print("There are " + str(num_of_young_people) + " people less than 10")

# Question 3
print("-----------------------------------------------------")
numbers = [2, 5, 1, 6, 5, 4, 3, 2, 3, 7, 8, 9, 0, 1, 2, 6]
no_dup_nums = {}
for num in numbers:
   if num in no_dup_nums:
      no_dup_nums[num] = no_dup_nums[num] + 1
   else:
      no_dup_nums[num] = 1 

print(no_dup_nums.keys())

# Question 4
print("-----------------------------------------------------")
credit_card_number = "55502386973"
nums = {}
for num in credit_card_number:
   if num in nums:
      nums[num] = nums[num] + 1
   else:
      nums[num] = 1 

# Note you could also just do nums.get("5") == 3
if "5" in nums and nums["5"] == 3 and "0" in nums and nums["0"] <= 1:
    print("It is valid")
else:
    print("It is not valid")













    
