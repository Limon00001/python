# Pattern

# 1. Square Pattern
'''
* * * *
* * * *
* * * *
* * * *
'''
n = 4
for rows in range(n):
    for cols in range(n):
        print("*", end =" ")
    print()

# 2. Increasing Triangle Pattern
'''
*
* *
* * *
* * * *
'''
n = 4
for rows in range (n):
    for cols in range(rows+1):
        print("*", end=" ")
    print()



# 3. Decreasing Triangle Pattern
'''
* * * *
* * *
* *
*
'''
n = 4
for rows in range (n):
    for cols in range (rows,n):
        print("*", end= " ")
    print()


''' -------------------------------------------------------------------
 Almost all other patterns can be completed using the above patterns
 ------------------------------------------------------------------- '''


# 4.
'''
      *
    * *
  * * *
* * * *
'''
# like here using one decreasing triangle pattern with space and one increasing pattern with '*'
n = 4
for rows in range(n):
    for cols in range(rows,n):
        print(" ",end=" ")
    for cols in range(rows+1):
        print("*",end=" ")
    print()


# 5.
'''
* * * *
  * * *
    * *
      *
'''
# Here used one increasing triangle with space and one decreasing triangle with '*'
n = 4
for rows in range (n):
    for cols in range (rows+1):
        print (" ",end=" ")
    for cols in range(rows,n):
        print("*",end=" ")
    print()


# 6.
'''
        *
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
# Here used one decreasing triangle with space, one increasing triangle with '*' and one increasing triangle with '*'
n = 4
for rows in range (n):
    for cols in range(rows,n):
        print(" ",end=" ")
    for cols in range(rows):
        print("*",end=" ")
    for cols in range (rows+1):
        print("*",end=" ")
    print()


# 7.
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
# one increasing pattern with space, two in a row decreasing pattern with '*'
n = 4
for rows in range(n):
    for cols in range(rows+1):
        print(" ",end=" ")
    for cols in range(rows,n-1):
        print("*",end=" ")
    for cols in range (rows,n):
        print("*",end=" ")
    print()



# 8.
'''
        *
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
# Here one decreasing triangle with space, one increasing triangle with '*' and one increasing triangle with '*' and one increasing pattern with space, two in a row decreasing pattern with '*'
n = 4
for rows in range(n-1):
    for cols in range(rows,n):
        print(" ",end=" ")
    for cols in range(rows):
        print("*",end=" ")
    for cols in range(rows+1):
        print("*",end=" ")
    print()
for rows in range(n):
    for cols in range(rows+1):
        print(" ",end=" ")
    for cols in range(rows,n-1):
        print("*",end=" ")
    for cols in range(rows,n):
        print("*",end=" ")
    print()
# 4.
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
rows = 5
for i in range (1,rows+1):
    for j in range (1,i+1):
        print (j,end=" ")
    print (" ")

