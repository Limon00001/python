# if-else condition

# Examples ----------
# 1.
price = 500
if price < 500:                    # after the condition must use [ : ]
    print ("I will buy the food")
else:
    print ("I will buy a drink")



# 2.
age = 18
if (age >= 18):
    print ("You are an adult")
else:
    print ("You are not an adult")

# Note: after applying the condition press [TAB] means it's inside the condition


# 3.
Age = 20
if (Age <= 10):
    print ("You\'re in a Golden age")
elif (Age <= 16):
    print ("You'\re lucky")
else:
    print ("You\'re Gollay geso [lol]")


# Nasted if-else
age1 = 70
age2 = 50
age3 = 100
if age1 > age2:
    if age1 > age3:
        print ("Opps!! You have to grow up.")
    else:
        print ("Congratulations! You are available to enter now.")
else:
    if age2 < age3:
        print ("Hi There!! Enter now.")
    else:
        print ("Sorry!!!")


# Ternary Operator
# It refers to the 3 operands.
num1 = 40
num2 = 10
print (num1 if num1>num2 else num2)               # 3 operands code

# or
num1 = 40
num2 = 10
max = num1 if num1>num2 else num2
print ("Maximum Value is: ", max)



# Logical Operators (and, or, not)
# 1.
salary = 5000
vacation_day = 4
if salary > 4500 and vacation_day > 3:
    print ("I will do the job")
else:
    print ("Give it to the others")


# 2.
ch = "z"
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print ("Vowel")
else:
    print ("Consonent")



# Letter Grade example
marks = float(input("Enter the marks: "))
if marks>=90 and marks<=100:
    print("Grade is: A")
elif marks>=85 and marks<=89:
    print("Grade is: A-")
elif marks>=80 and marks<=84:
    print("Grade is: B+")
elif marks>=75 and marks<=79:
    print("Grade is: B")
elif marks>=70 and marks<=74:
    print("Grade is: B-")
elif marks>=65 and marks<=69:
    print("Grade is: C+")
elif marks>=60 and marks<=64:
    print("Grade is: C")
elif marks>=55 and marks<=59:
    print("Grade is: C-")
elif marks>=50 and marks<=54:
    print("Grade is: D")
else:
    print("Grade is: F")
