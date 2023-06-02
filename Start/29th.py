'''                                          Classes & instances                               '''


# Examples: ----------------------------------------


# 1. Assume a login page, if the users name, email password is working properly, it shows login successful otherwise failed. If login successful then it will show the user's profile properly.

# Answer ==>
class User:
    # we can declare the attributes  as a default ->
    # name = ''
    # email = ''
    # password = ''
    # login = False
 
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # login method
    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
 
        if email == self.email and password == self.password:
            self.login = True
            print("Login Successful!")
        else:
            print("Login Failed!")

    # logout method
    def logout(self):
        self.login = False
        print("Logged Out!")

    # To show profile
    def isLoggedIn(self):
        if self.login == True:
            return True
        else:
            return False
 
    def profle(self):
        if self.isLoggedIn():
            print(self.name,"-",self.email)
        else:
            print("User is not Logged in!")
 
 
user1 = User("Adam", "adam@testmail.com", "12345")
 
user1.login()
user1.profle()



# 2. The base and height of a triangle are given. Find the area of triangle.

# Answer ==>
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area: ",area)
        
t1 = Triangle(10, 20)
t1.calculate_area()

t2 = Triangle(20, 30)
t2.calculate_area()



# 3. Show the specification of two computers:

# Answer ==>
class Computer:
    def __init__(self, size, storage):
        self.size = size
        self.storage = storage
    def spec(self):
        print("Display Size: ", self.size)
        print("Computer Storage: ", self.storage)

computer1 = Computer("15", "1TB")
computer2 = Computer("13.5", "500GB")

print("Computer 1 specification-----> ")
computer1.spec()

print("Computer 2 specification-----> ")
computer2.spec()



# 4. Book series:
# Answer ==>
class Book_series:
    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.num_books = len(books)
        
    def print_name(self):
        print(self.name)
        
    def print_books(self):
        print("The \"Hunger Games\" Books series: ", self.books)
        
hg = Book_series("Hunger Games", ["The Hunger Games", "Catching Fire", "Mockingjay"])

hg.print_books()
print(hg.num_books)