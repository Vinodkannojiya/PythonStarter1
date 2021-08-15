n=int(input("Enter a number :"))
#Method 1       InBuilt Function
import math
print("Value of factorial of",n, " with  inbuilt function is",math.factorial(n))

#Method 2 Using Recursion

def factRecursion(n):
    if n == 0:
        return 1
    else:
        return n * factRecursion(n-1)
        
print("Value of factorial of",n, " with  Recursion is",factRecursion(n))

#Method 3 Using Loop
fact=1
for i in range(n,0,-1):
    fact=fact * i
print("Value of factorial of",n, " with  Loop is",fact)

