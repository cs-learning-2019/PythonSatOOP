# Focus Learning OOP
# Week 12 HW Solutions
# Kavan Lam
# Dec 17, 2022

class Computer:
    def __init__(self, the_brand, the_memory, the_speed, the_color):
        self.brand = the_brand
        self.memory = the_memory
        self.speed = the_speed
        self.color = the_color
    
    def change_brand(self, new_brand):
        self.brand = new_brand
    
    def swap_memory_speed(self):
        temp = self.memory
        self.memory = self.speed
        self.speed = temp
    
    def __len__(self):
        return self.memory + self.speed
    
    def __str__(self):
        return "This is a computer from " + self.brand
    
    def __eq__(self, other):
        if self.brand == other.brand and self.memory == other.memory and self.speed == other.speed and self.color == other.color:
            return True
        else:
            return False
        
my_computer = Computer("Apple", 5, 6, "White")
my_computer.change_brand("Razer")
my_computer.swap_memory_speed()
print(my_computer.brand)
print(my_computer.speed)
my_other_computer = Computer("HP", 6, 5, "White")
if my_computer == my_other_computer:
    print("The computers are the same")
else:
    print("The computers are not the same")

    
        
