# -------------------------------------------- Recursion ----------------------------------------------------------

# recursion -> call by itself & we need to use a base case to stop this.
# 1. Factorial Problems:
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)                                 #  fact formula: n*fact(n-1)

print(fact(5))
