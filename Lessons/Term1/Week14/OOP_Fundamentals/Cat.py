from Animal import *

class Cat(Animal):
    def __init__(self, age, name):
        super(Cat, self).__init__(age, name)
        self.capacity = 10
    
    # This is an example of method overriding which is under Polymorphism
    def eat(self, amount):
        if amount > self.capacity:
            print("The cat will not eat it")
        else:
            print("Ok cat will happily eat it")
    
    # This is an example of method overriding which is under Polymorphism
    def make_sound(self):
        print("Meow!")
       
    # This is an example of Polymorphism since Human class also has this but this is not method overriding 
    def sleep(self):
        print("Meow.... meow.... me...")
