# Python OOP
# Week 8 HW solutions
# Kavan Lam
# Nov 19, 2022

# Question 1
def draw_equilateral_triangle(height):
    total_length = 2 * (height - 1) + 1
    current_stars = 1
    for i in range(height):
        spaces = (total_length - current_stars) / 2
        print(" " * spaces + "*" * current_stars + " " * spaces)
        current_stars = current_stars + 2
    
draw_equilateral_triangle(10)

# Question 2
print("---------------------------------------------------")
def draw_p(height):
    print("*****")
    print("*   *")
    print("*****")
    for row in range(height - 3):
        print("*")    
draw_p(5)

# Question 3
print("---------------------------------------------------")
def combine_numbers(list_of_int):
    answer = ""
    for number in list_of_int:
        temp = str(number)
        answer = answer + temp
        
    return answer

result = combine_numbers([1, 2, 67, 34])
print(result)
