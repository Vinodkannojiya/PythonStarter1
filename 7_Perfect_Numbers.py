#Method 1  check perticualr number is Perfect or not

num=int(input("Enter a number :"))
result=0
for i in range(1,num):
    if num%i==0:
        result += i
if num==result:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect lowerr")


#Method 2  check list of all  Perfect numbers between a range 
lower=int(input("Enter lower limit :"))
upper=int(input("Enter upper limit :"))

for i in range(lower,upper+1):
    result=0
    for j in range(1,i):
        if i%j==0:
            result+=j
    if result==i:
        print(i)
    
