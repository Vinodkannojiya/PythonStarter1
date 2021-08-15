#Method 1
import math
print("GCD of 4,18 is: ",math.gcd(4,18))
print("GCD of 64,48 is: ",math.gcd(64,48))

#Method 2 Using recuresion with Eucloid's method

def ComputeGCD(num1,num2):
    if num2==0:
        return num1
    else:
        return ComputeGCD(num2,num1%num2)
num1,num2=4,18
print(f"GCD of {num1} and {num2} is :",ComputeGCD(num1,num2))
num1,num2=64,48
print(f"GCD of {num1} and {num2} is :",ComputeGCD(num1,num2))       

#Method 3  general method  dont use this
def hcf(num1,num2):
    out=1
    for i in range(num1 if num1 <num2 else num2,1,-1):
        if num1 % i == 0 and num2 % i == 0:
            out=i
            break
    else:
        out=1
    return out
gcd=hcf(num1,num2) 
print("Value of GCD of {num1} and {num2} is :"+str(gcd))