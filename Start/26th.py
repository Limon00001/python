# --------------------------------------- Exceptions & Handling ---------------------------------------

# Exceptions: ------------------------------------------------------------------------------------------------------

'''
Python errors can be broadly classified into two classes:
1. Syntax errors                      -> Error caused by not following the proper structure (syntax) of the language
2. Logical errors (Exceptions)        -> Errors that occur at runtime (after passing the syntax test)

Some of the common built-in exceptions in Python programming:

    Exception Mode	                             Cause of Error
1. AssertionError	           Raised when an assert statement fails.
2. AttributeError	           Raised when attribute assignment or reference fails.
3. EOFError	                   Raised when the input() function hits end-of-file condition.
3. FloatingPointError	       Raised when a floating point operation fails.
4. GeneratorExit	           Raise when a generator's close() method is called.
5. ImportError	               Raised when the imported module is not found.
6. KeyboardInterrupt	       Raised when the user hits the interrupt key (Ctrl+C or Delete).
7. MemoryError	               Raised when an operation runs out of memory.
8. NotImplementedError         Raised by abstract methods.
9. OverflowError	           Raised when the result of an arithmetic operation is too large 
10. ReferenceError	           Raised when a weak reference proxy is used to access a garbage collected
11. RuntimeError	           Raised when an error does not fall under any other category.
12. StopIteration	           Raised by next() function to indicate that there is no further item to be returned by iterator.
13. TabError	               Raised when indentation consists of inconsistent tabs and spaces.
14. SystemExit	               Raised by sys.exit() function.
15. UnboundLocalError	       Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.

16. UnicodeError	           Raised when a Unicode-related encoding or decoding error occurs.
17. UnicodeEncodeError	       Raised when a Unicode-related error occurs during encoding.
18. UnicodeDecodeError	       Raised when a Unicode-related error occurs during decoding.
19. UnicodeTranslateError	   Raised when a Unicode-related error occurs during translating.


# Common Errors: ------------------------------------------------------------------------------------------

ValueError	                   Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError	           Raised when the second operand of division or modulo operation is zero.
IndexError	                   Raised when the index of a sequence is out of range.
KeyError	                   Raised when a key is not found in a dictionary.
NameError	                   Raised when a variable is not found in local or global scope.
OSError	                       Raised when system operation causes system related error.
SyntaxError	                   Raised by parser when syntax error is encountered.
IndentationError	           Raised when there is incorrect indentation.
SystemError	                   Raised when interpreter detects internal error.
TypeError	                   Raised when a function or operation is applied to an object of incorrect type.

'''



# Handling: ---------------------------------------------------------------------------------------------------

# try-except method
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # If user gives the value of the second number as 0, the program will not work. This is called ZeroDivisionError.
    result = num1 / num2
    print("Your result is: ",result)
except:
    print("Your second number cannot be 0. Please try again.")
print("Thank you.")


# -----------------------------------------------------

# try-except method
# If you understand that what kind of exceptions occurs, you can call it by name.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # If user gives the value of the second number as 0, the program will not work. This is called ZeroDivisionError.
    result = num1 / num2
    print("Your result is: ",result)

    myLists = [1, 4, 30, 100, 69]
    n = int(input("Enter the index number: "))
    print(myLists[n])
# also denoted by, except 'error_mode' as 'denoted_variable':
#   print(denoted_variable)
except ZeroDivisionError:
    print("Your second number cannot be 0. Please try again.")
except IndexError as error:
    print("You index cannot be greater than 4. Please try again.",error)
# Exceptions can be called in one line.
# except (ZeroDivisionError, IndexError):
#     print("Something is wrong. Please try again.")
print("Thank you.")

# -------------------------------------------------------

# try....finally method
# No matter of what if you want to show something to the user as a output either (If the program fully wrong.)
try:
    print(1/0)
finally:
    print("Thank you.")



# Raise --------------------------------------------------------------------------------------------------------
