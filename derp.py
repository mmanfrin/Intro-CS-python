class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name + ' is sitting.')
        
        
my_dog = Dog('Thor', 8)

print(my_dog.age)