# Focus Learning: Python 1 Cont Mon
# Finishing up functions
# Kavan Lam
# March 15, 2021

# Default Parameters
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
