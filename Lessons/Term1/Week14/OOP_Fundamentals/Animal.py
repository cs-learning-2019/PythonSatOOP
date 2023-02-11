class Animal(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.capacity = 100
        self.__god_secret = "It was a mistake"
    
    def age_by_one_year(self):
        self.age = self.age + 1
    
    def change_name(self, new_name):
        self.name = new_name
    
    def eat(self, amount):
        if amount > self.capacity:
            print("Unable to eat it")
        else:
            print("Ok the animal will eat it")
            
    def make_sound(self):
        print("Generic animal noise...")
    
