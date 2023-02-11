from Animal import *

class Human(Animal):
    def __init__(self, age, name):
        super(Human, self).__init__(age, name)
        self.capacity = 1000
        self.__password = "abc123" # This is private
    
    def eat(self, amount):
        print("I have no limits!!! I will eat it.")
        print(self.__password)
    
    def make_sound(self):
        print("Hi there my name is " + self.name + " and I am " + str(self.age) + " years old.")
    
    def sleep(self):
        print("Sure I'll sleep")
    
    def change_password(self, new_password):
        if (len(new_password) < 5):
            print("Invalid password")
        else:
            self.__password = new_password
        
    def getThePassword(self):
        return self.__password
    
    
