# ------------------------------------- Functions -------------------------------------------------


def sampleFunction():             # "def" is a keyword for creating python function
    print("Your Sum is: ")
    x, y = 154, 69
    sum = x + y
    print (sum)
    
sampleFunction()




# ----------------- Function Parameters ----------------

def total(n1, n2, n3):
    total = n1 + n2 + n3
    print (total)

total(3, 4, 5)
total(248, 448, 5475)
total(50, 500, 5000)



# --------------- Function Parameters value ---------------
# 1.
def cart(personName, itemName = "Badminton"):
    print (personName, "booked", itemName)

cart("Chris")

# 2.
def cart(personName, itemName = "Badminton"):
    print (personName, "booked", itemName)

cart("Chris", "Football")              # Here "itemName" update in cart function. If don't update then it shows 1st one.



# ------------------- Global & Local Variable uses -------------------
''' Global Variable: outside the function 
    Local Variable: Inside the function '''

# Wrong
var = 100
def normal ():
    # var = var + 1    [ error. var is a global variable. Can't convert a global variable into local variable like that.
    print(var)

normal()

# Right
var = 100
def normal ():
    loc = var
    loc = loc + 1
    print(var)

normal()



# ------------------------- Returning value from function -----------------------
def large(x,y):
    if x>y:
        return x
    else:
        return y
result = large(121,699)
print(result)



# ------------------------------- x arguments / xargs -------------------------------------
# xargs -> receive any number of parameters -> acts like tuples
# 1.
def actors(*details):
    print(details)
    print(details[1])

actors(101, "Tom Hardy")
actors(102, "Tom Hanks", 54)


# 2.
def add(*total):
    sum = 0
    for x in total:
        sum += x
    print(sum)

add(10,20)
add(200,300,50)
add(50,80,70,152)


# xx arguments / xxargs
# xxargs -> receive any number of parameters -> acts like dictionaries -> key, value
def actor(**details):
    print(details)
    print(details["Name"])

actor(Name = "Anisul Islam", Age = 54)



# ------------------------- lambda function / anonymous function (without name) ---------------------------
# 1.
'''
# named function
def calculate(a,b):
    result = (a*a) + 2*a*b + b*b
    return result
'''
# lambda parameter : expression
sum = (lambda a,b : a*a + 2*a*b + b*b) (2,3)
print(sum)


# 2.
'''
# named function
def cube(x):
    return x * x * x
'''
# lambda parameter : expression
cube = (lambda x : x * x * x) (5)
print(cube)



# ------------------------------ Map Functions & Filter Functions ----------------------------

# map function -> works with iterable object (list)
#              -> works with a function


# lists
numbers = [1,2,3,4,5]

# function
def square(a):
    return a*a

result = list(map(square, numbers))
print(result)


# filter functions -> returns an iterator were the items are filtered through a function to test if the item is accepted or not.
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# another example of filter functions
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)



# ----------------------------------- List comprehensions ----------------------------------

# finding square without using comprehension list
'''
# lambda function
num = [1,2,3,4,5]
result = list(map(lambda x: x*x, num))
print(result)
'''
num = [1,2,3,4,5]
# [expression for item in list]
result2 = [x*x for x in num]
print(result2)

# result3 = list(filter(lambda x : x%2==0, num))    ->      filter function
result3 = [x for x in num if x%2==0]
print(result3)




# ---------------------------------------- Zip Functions -----------------------------------------
name = ["Tom Hardy", "Tom Hanks", "Johnny Depp", "Christian Bale"]
age = [51, 64, 54, 55]

result = list(zip(name, age))
print(result)



# ------------------------------------------------------------------------------------------------
fullNames = ["Jhon Teddy", "Angelina Jolie", "Chirstian Bale"]

def full_name(n):
    devide = n.split(" ")
    return devide[1] + "," + devide[0]
    
final_output = [full_name(n) for n in fullNames]
print (final_output)



# ------------------------------------------------------------------------------------------------
scores = [156, 70, 100, 265]

def passed(score):
    bonus = score +10
    return bonus > 90

passing_scores = [passed(score) for score in scores]
print(passing_scores)