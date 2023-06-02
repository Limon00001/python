# ------------------------------------------------- Python Super() function --------------------------------------------------------------

''' 
Definition:
* The super() function is used to give access to methods and properties of a parent or sibling class.
* The super() function returns an object that represents the parent class.
'''

# ======>
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, I\'m {self.name}. I\'m {self.age} years old.")

# Subclass 1
class Student(Person):
    def __init__(self, name, age, graduation_year):
        super().__init__(name, age)
        self.graduation_year = graduation_year

    def graduate(self):
        print(f"{self.name} will graduate in {self.graduation_year}")

bale = Student("Bale", 26, 2024)
bale.introduce()
bale.graduate()


# ======>
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, graduation_year):
        super().__init__(name, age)
        self.graduation_year = graduation_year
    
    def info(self):
        super().introduce()
        print(f"{self.name} will graduate in {self.graduation_year}")
        
bale = Student("Bale", 28, 2024)
bale.info()


# =======>
class Animals:
    def __init__(self, Animal):
        print(Animal, "is an animal.")
    
class Mammal(Animals):
    def __init__(self, mammalname):
        print(mammalname, "is a cold-bloded animal.")
        super().__init__(mammalname)

class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't fly.")
        super().__init__(NonMarineMammal)

class Cat(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print("Cat has 4 legs.")
        super().__init__("Cat")

cat = Cat()
print(" ")
bat = NonMarineMammal("Bat")