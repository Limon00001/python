# List as input from user

# 1.
n = input("Enter a text of numbers: ")                # 10 20 30 50 500
list = n.split()                                      # 10, 20, 30, 50, 500
sum = 0
for num in list:
    sum = sum + int(num)
print (sum)


# 2.
numofWords = 0
numofLetters = 0
numofDigits = 0

text = input ("Enter your text: ")

for i in text:
    i=i.lower()                                      # .lower() -> lowercase
    if i >="a" and i <="z":
        numofLetters = numofLetters + 1
    elif i >="0" and i <="9":
        numofDigits = numofDigits + 1
    elif i ==" ":
        numofWords = numofWords + 1
    
print("Number of Letters: ",numofLetters)
print("Number of Digits: ",numofDigits)
print("Number of Words: ",numofWords + 1)                    # declare [space + 1]
