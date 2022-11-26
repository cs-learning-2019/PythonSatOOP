# Python OOP
# Week 9 HW Solutions
# Kavan Lam
# Nov 26, 2022

# Question 1
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y

my_calculator = Calculator()
print(my_calculator.add(2, 5))

# Question 2
print("----------------------------------------------------")
class Dog:
    def __init__(self, the_dog_name, age, dog_color):
        self.name = the_dog_name
        self.age = age
        self.dog_color = dog_color
    
    def increase_dog_age(self):
        self.age = self.age + 1
    
    def make_sound(self):
        print("Hello my name is " + self.name + " bark bark!")

my_dog = Dog("John", 5, "white")
my_dog.increase_dog_age()

my_other_dog = Dog("Lucy", 20, "Black")
my_other_dog.make_sound()

# Question 3
print("----------------------------------------------------------------")
x = 10
my_cal = Calculator()
x_2 = my_cal.multiply(x, x)
answer = my_cal.subtract(my_cal.add(my_cal.multiply(4, x_2), x), 5)
print(answer)      


        
        
        
