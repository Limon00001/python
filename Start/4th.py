# --------------------------------------------------- Modules ----------------------------------------------------------------


# Math related library functions

from math import *  # we can use all math terms using this libraries

print (max(50, 10))
print (min(50, 10))
print (abs(-7))
print (pow(2, 3))              # pow(base number, power number)
print (sqrt(25))
print (round(3.8))
print (floor(3.7))              # rounds decimal down to the nearest integer number
print (ceil(3.7))               # rounds decimal up to the nearest integer number
print (complex(2,5))
print (exp(10))
print (e)
print (pi)




# for all mathematical terms
import math

pie = math.pi
print(f"Value of pi is: {pie}")


import statistics

scores = [4, 4, 3, 6, 1, 2, 8, 4]
mean = statistics.mean(scores)
print(f"Mean score is: {mean}")


# multiple different modules in the same file by adding comma
'''
import statistics, math

diameters = [9, 7, 4, 6]
result = statistics.mean(diameters)
print(f"Mean diameter is: {result}")

pie = math.pi
print(f"Value of pi is: {pie}")
'''


# use the keyword 'from' to exact only the functionality ------------->
# 1.
from math import pi

print("Value of pi is: ", pi)
# print(pi)

# 2.
from statistics import mean

test_score = [33, 7, 4, 6]
result = mean(test_score)
print(f"Mean result is: {result}")




# Modify the modules name (renamed modules) ------------>
# 1.
import statistics as stats

sales = [23, 43, 26, 26, 29, 18, 24]
median = stats.median(sales)
print(median)

# 2.
import statistics as stats

ids = [33, 123, 22, 798, 23, 33]
mode = stats.mode(ids)                            # 'mode' -> appears most often
print(mode)

# 3.
import math as math_cons

math = "Grade constant: "
print(math)
print(f"pi: {math_cons.pi}")
print(f"Euler's number: {math_cons.e}")





# Type Function
num = 30
print (type(num))

num = 30.5
print (type(num))

name = "Rat"
print (type(name))

do = True
print (type(do))