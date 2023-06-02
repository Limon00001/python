# ---------------------------------------- Matrix ------------------------------------------------

# Creating matrix ---------------->
# (i) Output 1:-->
row = int(input("Enter Rows: "))
col = int(input("Enter Columns: "))
main = []                                # For main matrix
s = 0
for i in range(row):
    row_mat = []                             # matrix for rows
    for j in range(col):
        s = s + 1
        k = int(input("Elements " + str(s) + ": "))
        row_mat.append(k)
    main.append(row_mat)
print(main)


# (ii) Output 2:-->
row = int(input("Enter Rows: "))
col = int(input("Enter Columns: "))
main = []                                # For main matrix
s = 0
for i in range(1, row+1):
    row_mat = []                             # matrix for rows
    for j in range(1, col+1):
        s = s + 1
        k = int(input("Enter %d * %d Elements " %(i, j) + ": "))
        row_mat.append(k)
    main.append(row_mat)
print(main)



# Adding matrix ------------------>
row = int(input("Enter the number of Rows: "))
col = int(input("Enter the number of Columns: "))

# Matrix1:
print("Components of the Matrix 1:")
matrix_1 = []
for i in range(row):
    row_mat1 = []
    for j in range(col):
        k = int(input("Enter %d * %d Element " %(i, j) + ": "))
        row_mat1.append(k)
    matrix_1.append(row_mat1)
print("Matrix 1: ")
print(matrix_1)

# Matrix2:
print("Components of the Matrix 2:")
matrix_2 = []
for i in range(row):
    row_mat2 = []
    for j in range(col):
        k = int(input("Enter %d * %d Element " %(i, j) + ": "))
        row_mat2.append(k)
    matrix_2.append(row_mat2)
print("Matrix 2 is: ")
print(matrix_2)

# sum of two matrices:
result = []
for i in range(row):
    row_res = []
    for j in range(col):
        k = matrix_1[i][j] + matrix_2[i][j]
        row_res.append(k)
    result.append(row_res)
print("Sum of two matrices: ")
print(result)


# Other operations for Matrix ----------------->
'''
⦿ Subtracting Matrix -->

Same as 'adding matrix'. Inside the result portion loop, we need to use '-' instead of '+'.
like this -->  k = matrix_1[i][j] - matrix_2[i][j]

⦿ Multiply the Matrices -->

Same as 'adding matrix'. Inside the result portion loop, we need to use '*' instead of '+'.
like this -->  k = matrix_1[i][j] * matrix_2[i][j]
'''


# 2. Adding Matrices [Another format] -------------->
row = int(input("Enter rows: "))
col = int(input("Enter columns: "))

x = []
z = []
for i in range(0, row):
    for j in range(0, col):
        z.insert(j, int(input("Enter the %d * %d element: " %(i,j))))
    x.insert(i,z)
    z = []

y = []
for i in range(0, row):
    for j in range(0, col):
        z.insert(j, int(input("Enter the %d * %d element: " %(i,j))))
    y.insert(i,z)
    z = []

sum = []
for i in range(0, row):
    for j in range(0, col):
        z.insert(j, x[i][j] + y[i][j])
    sum.insert(i,z)
    z = []
print(sum)


# 3. Matrix Transpose ------------------->

# (i) Matrix Transpose using Nested Loop:
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

# Matrix:
matrix = []
for i in range(row):
    row_mat1 = []                             # matrix for rows
    for j in range(col):
        k = int(input("Enter %d * %d Elements " %(i, j) + ": "))
        row_mat1.append(k)
    matrix.append(row_mat1)

print("Matrix: ")    
for i in matrix:
        print(i)

# Transpose matrix
result = []
for i in range(col):
    r = []
    for j in range(row):
        k = matrix[j][i]
        r.append(k)
    result.append(r)
print("Transpose Matrix:")
for i in result:
    print (i)


# (ii) Matrix Transpose using List Comprehention:
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

# creating matrix
print("Enter the element of matrix:")
matrix = [[int(input("Enter %d * %d Elements " %(i, j) + ": ")) for i in range(col)]for j in range(row)]
print ("Matrix:")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
    
# transpose matrix
result = [[0 for i in range(row)]for j in range(col)]
for i in range(col):
    for j in range(row):
        result[i][j] = matrix[j][i]
print("Transpose Matrix:")
for i in range(col):
    for j in range(row):
        print(result[i][j], end=" ")
    print()