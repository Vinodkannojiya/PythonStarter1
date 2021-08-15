#Method 1 

def reverseString(str):
    revStr=""
    for i in str:
        revStr=i+revStr
    return revStr

string="vinod"
print("Input string is :",string)
outStr=reverseString(string)
print("Reverse string is: ",outStr)

#Method 2
string="vinod"
print("Input string is :",string)
outStr=string[::-1]
print("Reverse string is: ",outStr)