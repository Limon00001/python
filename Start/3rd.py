# Lists

# (i)
# from turtle import position

data = [5, 6, 7, 8, 9, 15, 30]
print (data[2])
print (data[5])
print (data[:])
print (data[-3:])
print (data[2:5])           # index number : count from first value (where data will stop)
print (data[:3])            # After the colon (:) indicates where the data should stop
print (data[2:])            # Here will be printed from index 2
print (data[-1])            # will start printing from the reverse side
print (data[8:])            # specifying a range outside the length of a list will return an empty list
print (data[6:0])           # start index and stop data don't match, will return an empty list
print (data[1:5:2])         # start : stop : step [ step determines how python steps between start and end]
print (data[::2])           # using the step value with no start or end value. By default it will work from the start and end of the full origin.
print (data[::-1])          # printing reverse order
print (data[3::-1])
print (data[:3:2])
print (data * 2)
print (data.clear())

data = [5, 6, 7, 8, 9, 15, 30]
data2 = data.copy()
data[-4] = 90
print (data2)
print(data)


# (ii)  Knowing index number
friends = ["Rhino", "Elephant", "Snake", "Scorpion"]
print (friends.index("Snake"))


# (iii)  Replace value inside the lists
friends = ["Rhino", "Elephant", "Snake", "Scorpion"]
friends[0]="Lion"
print (friends)


# Adding items in lists
# Append - add as a last element
friends = ["Rhino", "Elephant", "Snake", "Scorpion"]
friends.append("Lion")
print (friends)

# Extend
value = [1, 2, 3]
friends = ["Rhino", "Elephant", "Snake", "Scorpion"]
value.extend(friends)
print (value)

# Insert - Can be added as desired
friends = ["Rhino", "Elephant", "Snake", "Scorpion"]
friends.insert(2, "Lion")
print (friends)

# Finding length
friends = ["Rhino", "Elephant", "Snake", "Scorpion", "Lion"]
print (len(friends))


# Removing items
friends = ["Rhino", "Elephant", "Snake", "Scorpion", "Lion"]
friends.remove("Snake")
del friends[-1]                     # 'del' keyword allows to delete objects
print (friends)

# Another is pop. It will remove last element of a list.
friends = ["Rhino", "Elephant", "Snake", "Scorpion", "Lion"]
friends.pop()
print (friends)

# Adding lists
friends = ["Rhino", "Hippo", "Lion"]
enemy = ["Snake", "Scorpion"]
print (friends + enemy)

# Split Sentence
sentence = "Hey you fool!"
print (list(sentence))

# Finding minimum elements
data = [5, 6, 7, 8, 9, 15, 30]
print (min(data))

# Finding maximun elements
data = [5, 6, 7, 8, 9, 15, 30]
print (max(data))

data = [5, 6, 7, 8, 9, 15, 30]
one, *other = data
print (one)
print (other)


''' Elements exists or doesn't exist ----------------
    If elements exist it will show true otherwise it will show false.'''
# i.
data = [5, 6, 7, 8, 9, 15, 30]
print (8 in data)

# ii.
data = [5, 6, 7, 8, 9, 15, 30]
print (100 in data)


# Sort list
# ascending orders
data = [50, 16, 700, 68, 99, 105, 3]
data.sort()
print (data)


# decending orders
data = [50, 16, 700, 68, 99, 105, 3]
data.sort(reverse=True)
print (data)

# using "key":
friends = ["Monkey", "Elephant", "Snake", "Lion"]
friends.sort(key=len)
print (friends)

# Nasted list:
data = [[5, 16], [7, 68], [9, 10], [3, 69]]
data.sort()
print (data)         # ascending by 1st element


data = [[5, 16], [7, 68], [9, 10], [3, 69]]
def sortBySec(index):
    return index[1]
data.sort(key=sortBySec)
print(data)         # ascending by 2nd element


# Range
data = list (range(10))
print (data)
print (data[5])


data = list(range(2,11))      # Here [2 = starting point, 11 = ending point + 1]
print(data)


data = list (range(5,21,3))           # Here [5 = starting point, 21 = ending point + 1, 3 = space]
print (data)


# Count
data = [50, 16, 700, 68, 99, 105, 3, 68, 51, 68]
position = data.count(68)
print (position)


# Tuples
name = ("Leonardo DiCaprio", "Tom Hardy", "Christian Bale", "Tom Hanks")
print (name)
print (name[1])
print (name[0:])
print (name[::-1])          # printing reverse order

a, b, c, d = name
print (a, b, c, d)
a, *b, c = name
print (a, b, c)

act = "Tom Hardy"
print (tuple(act))

# Converting list into tuple
lst = [1, 2, 3, 5, 5, 8, 4, 6, 1]
tpl = tuple(lst)
print (tpl)

# Nested tuples
name = (("Leonardo DiCaprio",47,"USA"), ("Tom Hardy",45,"UK"), ("Christian Bale",48,"UK"), ("Tom Hanks",66,"US"))
print (name[0])
print (name[1])
# NOTE: Tuples values can't be updated

num = [(1, 2, 3),(4, 5, 6)]
num.append(("You", "Fool"))
print (num)
num.remove((1, 2, 3))
print (num)

word = (["a", "b", "c"], ["d", "e", "f"])
word[0].append("z")
print (word)
# word.append("s")                      --> Error: Tuple cannot be upgraded.

# ----------------------------------- Sets -----------------------------
num = {1,2,3,4,5,4}
print (num)                # Automically remove duplicate numbers

num = [2,3,4,5,4]
num2 = set(num)
num2.add(7)
num2.remove(3)
print (num2)


num = {2,3,4,5,4}
num2 = set([4,5,6])
# print (num.union(num2))
print (num | num2)        # "|" = union
# print (num.intersection(num2))
print (num & num2)        # "&" = intersection
# print (num.difference(num2))
print (num - num2)        # "-" = difference


# Frozensets (Unchangable)
A = frozenset([1,2,3,4])
B = frozenset([3,4,5,6])
print(A)
print(A|B)
# A.add(9)   ----------------->  Frozen set doesn't support add(), remove() etc.


# -----------------------------------  Dictionaries ------------------------

# syntax:
# variable_name: {key1: value1, key2: value2}

students = {
    # key : value

    # "101" : "Tom Hardy",
    # "102": "JElizabeth Olsen",
    # "103": "Karren Gillan",
    101: "Tom Hardy",
    102: "Elizabeth Olsen",
    103: "Karren Gillan",
}

print(students[101])                           # print(students.get("101"))
print (students.values)                        # checking values
print(students.get(106, "Not found"))
print(students.get(103, "Not found"))

# Another method: creating dictionary
dictionary = dict([(1, "Welcome"), (2, "to"), (3, "Python")])
print (dictionary)

# Nested dictionary
d1= {"name":{"first": "Chris", "last": "Alter"}, "Age": 28}
print (d1)

# Adding ELements:
d = {}
d[0] = "Welcome"
d[1] = ("How", "are", "you")            # adding tuples
d["name"] = "Sam"
print (d)
d["name"] = {"first": "Sam", "last": "Alter"}          # updating name key
print (d)

# 'del' use in dictionary
products = {"category": "book",
            "price": 400,
            "in_stock": True}

del products["in_stock"]
print(products)


students = {
    101: "Tom Hardy",
    102: "Elizabeth Olsen",
    103: "Karren Gillan",
}
s1 = students.pop(101)
print (s1)
print (students)
s2 = students.popitem()               # delete last element
print (s2)
print (students)

# set value --> each key
keys = {"a", "b", "c", "d"}
value = 1
print(dict.fromkeys(keys, value))