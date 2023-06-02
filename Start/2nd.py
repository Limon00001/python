# ------------------------------------- Formatted String -------------------------------------------
# String in multiple lines
str = '''Hey,
Wassup?
How's going?'''
print (str)
print (len(str))

str1 = "Ridiculous"
for i in str1:
    print (i, end="")
print ()                          # new line

str1 = "Ridiculous"
print (str1[0:5])
print (str1[5:])
print (str1[2:5])
print (str1.upper())
print (str1.lower())
print (str1.find("l"))
print (str1.index("l"))
print (str1.find("i"))
print (str1.index("i"))

string = "Hello. Anyone there?"
print (string.split())                                    # return list output
print (string.rpartition("Anyone"))                       # return tuple output
print (string.replace("Hello", "Hi"))

stg1 = "How"
stg2 = "are"
stg3 = "you"
stg = "{} {} {}?".format(stg1, stg2, stg3)
print (stg)

num1 = 30
num2 = 50
print (f"{num1} + {num2} = {num1 + num2}")

# syntax:
# string.format(value1, value2...)

name1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# (or)
#numbered indexes:
name2 = "My name is {0}, I'm {1}".format("John",36)
# (or)
#empty placeholders:
name3 = "My name is {}, I'm {}".format("John",36)

print(name1)
print(name2)
print(name3)


user_details = ("Jolie", "USA", 47)
f_name = user_details[0]
age = user_details[-1]
message = f"{f_name} {age}"
print(message)

''' --------------------------------- Another Type of String format --------------------------------------'''
# syntax:
# "string that we want to write %s" % "string value"
print("My name is %s" % "Abigail")

# syntax:
# "template string {}".format(arguments)
print("Hello, I am {}. I am %d years old. I am a {} turned to {}".format("Abigail", "actor", "musician") %36)

# Positional arguments
# syntax:
# "write_string {0} and {1}.".format(arguments)
print("Bale plays {0} and {1}.".format("guitar", "flute"))

# Keywords arguments
# syntax:
# "{key1} is {key2}!".format(key1=" ", key2=" ")
print("{something} is {anything}!".format(something="Today", anything="awesome"))

# Mix keyword & Positional arguments
name = "Lorem"
int = 3
book = "specimen book"

print("{name} is simply dummy text of the {0} and {1} industry. It has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type {book}. Here I have used {number} lines.".format("printing", "typesetting", name=name, book=book, number=int))
# have to use positional arguments first, then keywords arguments

# Fomatted string literals
# syntax:
'''
variable = "some value"
f"this is a string {variable}"
'''
name = "Alba"
# can use 'f' also instead of 'F'
print(F"Jessie and {name} have been friends since primary school.")


# Example
#  A dictionary which represents the top rankings for men's Football teams and how many games they won out of 9.
table = {"Arsenal": 8, "Man City": 7, "Totenhum": 6, "Chelsea": 5, "Man United": 5}

# use a 'for loop' and the 'items()' method to go through each of the key value pairs of the 'table' dictionary.
for team, score in table.items():
    print(f"{team:10} ==> {score:10d}")
# {team:10} and {score:10d} tells the computer to create a field that is 10 characters wide. This will create even columns for the data. 'd' inside here {score:10d} refers to a decimal integer.


# Template string
# import the template library -> 'from string import Template'
# Template("$placeholder").substitute(placeholder="value")
from string import Template

print(Template("I love $name!").substitute(name="python"))



# Formating types: ------------------------

#  ' :< ' Left aligns the result (within the available space)
txt1 = "We played {:<10} hours football."
print(txt1.format(5))

#  ' :> ' Left aligns the result (within the available space)
txt2 = "We played {:>15} hours football."
print(txt2.format(5))

#  ' :^ ' Center aligns the result (within the available space)
txt3 = "We played {:^8} hours football."
print(txt3.format(5))

#  ' = ' to place the plus/minus sign at the left most position
txt4 = "The temperature is {:=9} degrees celsius."
print(txt4.format(-5))

#  ' + ' to always indicate if the number is positive or negative
txt5 = "The temperature is between {:+} and {:+} degrees celsius."
print(txt5.format(-3, 7))

#  ' - ' to always indicate if the number is negative (positive numbers are displayed without any sign)
txt6 = "The temperature is between {:-} and {:-} degrees celsius."
print(txt6.format(-3, 7))

#  ' ' (a space) to insert a space before positive numbers and a minus sign before negative numbers
txt7 = "The temperature is between {: } and {: } degrees celsius."
print(txt7.format(-3, 7))

#  ' , ' to add a comma as a thousand separator
txt8 = "The universe is {:,} years old."
print(txt8.format(13800000000))

#  ' _ ' to add a underscore character as a thousand separator
txt9 = "The universe is {:_} years old."
print(txt9.format(13800000000))

#  ' b ' to convert the number into binary format
txt10 = "The binary version of {0} is {0:b}"
print(txt10.format(5))

#  ' d ' to convert a number, in this case a binary number, into decimal number format
txt11 = "We have {:d} chickens."
print(txt11.format(0b101))

#  ' e ' to convert a number into scientific number format (with a lower-case e)
txt12 = "We have {:e} chickens."
print(txt12.format(5))

#  ' E ' to convert a number into scientific number format (with an upper-case E)
txt13 = "We have {:E} chickens."
print(txt13.format(5))

#  ' f ' to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals
txt14 = "The price is {:.2f} dollars."
print(txt14.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this
txt15 = "The price is {:f} dollars."
print(txt15.format(45))

#  ' F ' to convert a number into a fixed point number, but display inf and nan as INF and NAN
x = float('inf')
txt16 = "The price is {:F} dollars."
print(txt16.format(x))

#same example, but with a lower case f
txt17 = "The price is {:f} dollars."
print(txt17.format(x))

#  ' o ' to convert the number into octal format
txt18 = "The octal version of {0} is {0:o}"
print(txt18.format(10))

#  ' x ' to convert the number into Hex format:
txt19 = "The Hexadecimal version of {0} is {0:x}"
print(txt19.format(255))

#  ' X ' to convert the number into upper-case Hex format:
txt20 = "The Hexadecimal version of {0} is {0:X}"
print(txt20.format(255))

#  ' % ' to convert the number into a percentage format:
txt21 = "You scored {:%}"
print(txt21.format(0.25))

#Or, without any decimals:

txt22 = "You scored {:.0%}"
print(txt22.format(0.25))

# [source: W3schools]