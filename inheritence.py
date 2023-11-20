# Parent class : this is abstract
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
       pass  

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    

    def animalSpeak(self):
        super().speak()

# Child class
class Cat(Animal):
    # This piece of code is not needed. It will be done by default
    def __init__(self, name):
        super().__init__(name)  

    # @override
    def speak(self):        
        return f"{self.name} says Meow!"


# Create instances of the subclasses
my_dog = Dog("Dog Name")
my_cat = Cat("Cat Name")

any_animal = Animal("RandomName")
print(any_animal.speak())
# Call the speak method on the instances
print(my_dog.speak())  # Output: Buddy says Woof!
print(my_cat.speak())  # Output: Whiskers says Meow