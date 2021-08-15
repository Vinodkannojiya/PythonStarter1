#Method 1  Print Prime numbers between two numbers
lower=int(input("Enter lower level :"))
upper=int(input("Enter upper level :"))

for i in range(lower,upper+1):
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

#Method 2  to check one number is prme or not
num=int(input("Enter a number :"))
if num > 1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not an prime number.")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not an prime number.")    
