# While loop & For loop

x = 1
x = 110
x = 69
#now
print (x)
# output will be 69
# In pyhton, It thinks that value updated that's why it prints last value

# 1.
i = 1                                       # initialization
while i<=10:                                # condition
    print ('You\'re a funny person')        # statements
    i+=1  #or use -> i = i + 1              # update

# 2.
i = 1
while i<=10:
    print (i)
    i+=1

# 3.Print even number
i = 1
while i<=100:
    if i%2 == 0:
        print (i)
    i+=1


# 4. Print odd number
i = 1
while i<=100:
    if i%2 == 0:
        print (i + 1)
    i+=1

# 5.
data = [5, 6, 7, 8, 9, 15, 30]
i = 0
while i<=6:
    print (data[i])
    i+=1

# Here we need to track the index number. That's why "For Loop" is better than "While Loop".

# 6.
user = int(input("Enter last number: "))
sum = 0
i = 1
while i <= user:
    sum += i
    i += 1
print ("Sum is", sum)

# 7.
val = int(input("Enter a multiple of 7: "))
while val%7 != 0:
    val = int(input("Enter a multiple of 7: "))
else:
    print ("%d is multiple of 7" %val)


# Break & Cntinue
''' "Break and Continue" will work under the if-else condition
 #  Break refers to remove everything else from that item
 #  Continue refers to skip that item '''

# Break
i = 1
while i <= 100:
    if i == 20:
        break
    print(i, end =" ")
    i += 1
print("Congratulations!!")


# Continue
for i in range(1,10):
    if i == 7:
        continue
    print(i, end =" ")
    i+=1
print("Congratulations!!")


x = [1, 13, 15, 4, 9, 19, 21]
for i in x:
    if i>10:
        continue
    print(i)



# ----------------------------------------- For Loop -----------------------------------------------

data = [5, 6, 7, 8, 9, 15, 30]
for x in data:
    print (x)


# ---------------------------------------
prices = [10, 38, 40, 58, 62]

in_Line = [price/2 for price in prices]
print(in_Line)

# or
multi_Line = []
for price in prices:
    half_price = price/2
    multi_Line.append(half_price)

print(multi_Line)

# or
def half(num):
    return num/2
halfed = [half(price) for price in prices]
print(halfed)

# -------------------------------------------------------------------
names = ["Smith", "Jackson", "Robert"]

add = ["Mr." + name for name in names]
print(add)