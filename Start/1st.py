# Basics

print ("Hello world")
# or
print ('Hello world')
# or
print ('''Hello world''')
# for string type we need to use quotation

#print ('Hello, I'll be there') #----> error
print ('Hello, I\'ll be there')  #  [ \ ]  means ignore ignore insider quotation

# print ("Hello world') ------>  'error'   either [" " or ' ']

print (5)  # for value
print (5+5)

# if 
print ('5+5')  # means string




# variable
N1 = 6
N2 = 7
N3 = N1 + N2
print (N3)


# Concatenation ( Differennt type variable run)
Text = "Two and two makes "        # string type variable
Num = 2 + 2                        # mathemetical/number type variable
isSmart = True                     # boolean type variable
isRich = False                     # boolean type variable

# print (Text + Num)   ----->  error  [ Different type variable]  

Sum = str (Num)          # Convert Num to string type variable
print (Text + Sum)



# Another Example
x,y,z = (6,9,2)
print (x,y)
'''
x,y = (2,4,5,6) ----->    not possible -> too many  values for two variables.
print (x)
print (y)
'''

# Taking input from users
# 1.
name = input ("What's your name? ")
print (name)
# 2.
name = input ("What's Your Favourite Food?")
print ("Favourite Food: " + name)
# Number input
age_text = input ("How old are you? ")
age = int (age_text)
print (age)
# string and number input
num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")
sum = int(num1) + int(num2)
print ("The sum is: ", sum)
# multi line comment

'''
Enjoy
1st 
lecture
'''
# or use  triple "

