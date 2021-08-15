def armstrongNumber(range_val):
    for i in range(range_val):
        
        num=i
        result=0
        n=len(str(i))
        while i>0:
            digit=i%10
            result += digit ** n
            i= i//10
        if result == num:
            print(f"Number {num} is an armstrong number")

armstrongNumber(2000)

