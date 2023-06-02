# -------------------------------- Problems -----------------------------------


# 1. Remove duplicate characters from string
userInput = input("String name: ")
result = ""
for char in userInput:
    if char not in result:
        result += char
print("Original string: ",userInput)
print("Removing duplicates: ",result)
