# ------------------------------------------ OOP in Python ----------------------------------------------------------

# Classes and Instances: ------------------------------------
'''                                        'Process-01'                                                   '''

class Student:
    # use 'pass' statement to avoid error
    pass

std_1 = Student()
std_2 = Student()

print(std_1)
print(std_2)

# Now declare what the data will contain inside the 'Student' class
# Suppose Students have their first name, last name, id card, CGPA, email
std_1.first = "Johnny"
std_1.last = "Depp"
std_1.id = 252525
std_1.cg = 3.75

std_2.first = "Amber"
std_2.last = "Heard"
std_2.id = 252526
std_2.cg = 2.75

print(std_1.id, std_1.cg)
print(std_2.id, std_2.cg)

'''
'Process-01' is a very lengthy proccess. Also we need to set each data manually. If we set the data like this, we can make a lot of mistakes. That's why we use '__int__' method.
'''



''' ---------------------------------- Alternative ---------------------------'''

'''                                    'Process-02'                                               '''
                                   # Using __init__ method

class Student:

    # '__init__()' function is called automatically every time the class is being used to create a new object. 'self' parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    def __init__(self, first, last, id, cg):
        self.first = first
        self.last = last
        self.id = id
        self.cg = cg
        self.email = str(id) + "@institute.edu.bd"
        # if we create email with name & company name
        # self.email = first + '.' + last + '@company_name.com'

std_1 = Student("Christian", "Bale", 145487, 3.85)
std_2 = Student("Angelina", "Jolie", 145897, 3.90)

# print(std_1)
# print(std_2)

print(std_1.id, std_1.cg, std_1.email)
print(std_2.id, std_2.cg, std_2.email)

# What if we need to show students fullname?-----
print("{} {}".format(std_1.first, std_1.last))
print("{} {}".format(std_2.first, std_2.last))
# But if there is huge number of students then its very difficult to write all the data like this
# That's why we need to follow 'Process-03'




'''                                        'Process-03'                                               '''


class Student:
    def __init__(self, first, last, id, cg):
        self.first = first
        self.last = last
        self.id = id
        self.cg = cg
        self.email = str(id) + "@institute.edu.bd"
        # if we create email with name & company name
        # self.email = first + '.' + last + '@company_name.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)

std_1 = Student("Leonardo", "DeCaprio", 145487, 3.85)
std_2 = Student("Kate", "Winslet", 145897, 3.90)

# print(std_1)
# print(std_2)

print(std_1.id, std_1.cg, std_1.email)
print(std_2.id, std_2.cg, std_2.email)

# Have to use 'fullname()' like this. Because it is a method.
print(std_1.fullname())
print(std_2.fullname())

# We can also print the student's fullname also like this but here we need to do it manually
# std_1.fullname()
# print(Student.fullname(std_1))

# std_2.fullname()
# print(Student.fullname(std_2))


# We will use 'Process-03' to avoid this complexity
