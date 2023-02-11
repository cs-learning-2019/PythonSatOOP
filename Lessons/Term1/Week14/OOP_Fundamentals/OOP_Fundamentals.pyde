# Python OOP
# Inheritance, Encapsulation, and Polymorphism Example
# Kavan Lam
# Dec 28, 2022

from Animal import *
from Cat import *
from Human import *

def setup():
    size(100, 100)

def draw():
    background(0, 0, 0)

my_animal = Animal(1, "Bob")
my_cat = Cat(10, "John")
my_human = Human(100, "Dude")

print("----------------------------------------------------")
my_animal.age_by_one_year()
my_animal.change_name("Bobby")
my_animal.make_sound()
my_animal.eat(10000000)

print("----------------------------------------------------")
my_cat.age_by_one_year()
my_cat.change_name("Jonny")
my_cat.make_sound()
my_cat.eat(10000000)

print("----------------------------------------------------")
my_human.age_by_one_year()
my_human.change_name("Duuddeee")
my_human.make_sound()
my_human.eat(10000000)

my_human.change_password("12xdcfhvgb34abcd")
print(my_human.getThePassword())
