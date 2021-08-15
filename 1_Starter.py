'''
 #Write a Python program to get the Python version you are using.
import sys
print("python Version")
print( sys.version)
print("python Version Info")
print( sys.version_info)
'''
'''
python Version
3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
python Version Info
sys.version_info(major=3, minor=7, micro=7, releaselevel='final', serial=0)
'''
'''
#Write a Python program to display the current date and time.
import datetime as date
print("Normal datetime:-" + str(date.datetime.now()))
print("Formatted datetime :" + str(date.datetime.now().strftime("%Y-%m-%d %H-%M-%S")))
'''
'''
Normal datetime:-2021-08-13 22:36:23.410952
Formatted datetime :2021-08-13 22-36-23
'''
'''
#Write a Python program which accepts the radius of a circle from the user and compute the area
import math as m
radius=float(input("Enter the radius:\n"))  # for input float value typecase to int will throw error so float is used
area= m.pi * radius * radius
print("Area of circle is:"+str(area))
'''
'''
Enter the radius:
6
Area of circle is:113.09733552923255
'''
'''
#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
first=input("Enter your first name:")
last=input("Enter your last name:")
name=first + last
print("Your full name in reverse order is :"+name[::-1])
'''
'''
Enter your first name:vinod
Enter your last name:kanojiya
Your full name in reverse order is :ayijonakdoniv
'''
'''
#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

input=input("enter the data:")
list=input.split(",")
tuple=tuple(list)
print("Printing list: ", end="")
print(list)
print("Printing tuple: ",end="")
print(tuple)
'''
'''
enter the data:1,2,5,8,4,9,6,3,2,1,4,5,8,7,5,6,3,2
Printing list: ['1', '2', '5', '8', '4', '9', '6', '3', '2', '1', '4', '5', '8', '7', '5', '6', '3', '2']
Printing tuple: ('1', '2', '5', '8', '4', '9', '6', '3', '2', '1', '4', '5', '8', '7', '5', '6', '3', '2')
'''
'''
#Write a Python program to accept a filename from the user and print the extension of that
#1st method
fileName=input("Enter filename: ")
findDot=fileName.find(".")
print("Extension of file is by method 1:-" + fileName[findDot+1:])
#2nd Best method
splits=fileName.split(".")
print("Extension of file is by method 2:-" + splits[-1])
'''
'''
Enter filename: vinod.java
Extension of file is by method 1:-java
Extension of file is by method 2:-java
'''
'''
#Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print("First color in list is "+color_list[0] + " and last color is "+ color_list[-1])
'''
'''
First color in list is Red and last color is Black
'''
'''
#Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
date=exam_st_date[0]
month=exam_st_date[1]
year=exam_st_date[2]
print(f"The Examination starts from  {date} / {month} / {year}")
print("The Examination starts from  %i / %i / %i"%exam_st_date)     #check and use this syntax
'''
'''
The Examination starts from  11 / 12 / 2014
The Examination starts from  11 / 12 / 2014
'''
'''
#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n=int(input("Enter a number:"))     #input must in inteeger as per question
n=str(n)
val= int(n) + int(n + n) + int(n + n + n)
print("Value is :-"+str(val))
'''
'''
Enter a number:5
Value is :-615
'''
'''
#Write a Python program to print the calendar of a given month and year.
import calendar as c
year=int(input("enter current year :"))
month=int(input("enter current month :"))
print(c.month(year,month))
'''

'''
enter current year :2021
enter current month :8
    August 2021
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
'''

#Write a Python program to print the following 'here document

doc='''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''

#print(doc)

'''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''

'''
#Write a Python program to calculate number of days between two dates
from datetime import date 
date1=date(2021,8,15)
date2=date(1994,6,1)
dateDiff=date1 - date2
print("Date diffrence is :"+str(dateDiff.days))
'''
'''
Date diffrence is :9937
'''

'''
#Write a Python program to get the volume of a sphere with radius 6.
from math import pi
radius1=6
volume= ( 4 / 3 ) * pi * radius1 * radius1 * radius1
print("Volume of sphere is : "+str(volume))
'''
'''Volume of sphere is : 904.7786842338604'''

'''
#Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference

num1=17
num2=int(input("enter a number :"))
if num2 > num1:
    print("Absolute double diff is :"+str(abs((num2-num1)*2)))
else:
    print("Actual diff is :"+str(abs(num2-num1)))
'''
'''
enter a number :25
Absolute double diff is :16
'''

'''
#Write a Python program to test whether a number is within 100 of 1000 or 2000
num=int(input("Enter a number :"))
if num <100:
    print("Number is within 100")
elif num <1000:
    print("Number is within 1000")
elif num <2000:
    print("Number is within 2000")
else:
    print("Number is more than 1000")
'''
'''
Enter a number :50
Number is within 100

Enter a number :200
Number is within 1000

Enter a number :1520
Number is within 2000

Enter a number :22225
Number is more than 1000
'''

'''
#Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum

num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))
num3=int(input("Enter 3rd number :"))

if num1==num2 and num2==num3:
    print(3 * (num1+num2+num3))
else:
    print(num1+num2+num3)    

'''
'''
Enter 1st number :1
Enter 2nd number :2
Enter 3rd number :3
6

Enter 1st number :2
Enter 2nd number :2
Enter 3rd number :2
18
'''

'''
#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

def getString(str):
    if len(str) >2 and str[:2] == "Is":
        return str
    else:
        return "Is" + str   

print(getString("Is i am going ?? Here i am coming"))
'''
'''
Is i am going ?? Here i am coming
'''
'''
#Write a Python program to get a string which is n (non-negative integer) copies of a given string.

num=int(input("enter a Number :"))
if num % 2 ==0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is Odd number")    
'''
'''
enter a Number :151
151 is Odd number

enter a Number :6
6 is an Even number
'''
'''
 #Write a Python program to count the number 4 in a given list.

list = [1,2,5,4,7,8,9,6,5,4,1,4,8,5,4,2,6,5,4,8,5,7,4,8,5,4,3,6,5,2,2]
total_appearcance=list.count(4)
print("Total count of 4 is :" +str(total_appearcance))
'''
'''
Total count of 4 is :7
'''
'''
#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2. 

def str_copies(str,n):
    if len(str)>1:
        return str[:2] * n
    else:
        return str * 10

output1=str_copies("Hello India",12)
output2=str_copies("H",12)
print(output1)
print(output2)
'''
'''
HeHeHeHeHeHeHeHeHeHeHeHe
HHHHHHHHHH
'''
'''
#Write a Python program to test whether a passed letter is a vowel or not. 

char=input("Enter a letter :")[0]
if char in ('a','e','i','o','u'):
    print (f"{char} is a Vovel")
else:
    print (f"{char} is not a Vovel")

'''
'''
Enter a letter :j
j is not a Vovel

Enter a letter :p
p is not a Vovel

Enter a letter :i
i is a Vovel
'''
'''
#Write a Python program to check whether a specified value is contained in a group of values

list=[1,2,5,6,9,8,4,2,5,1,31,56,23,74,85,96,52,48]
val=310
if val in list:
    print(f"Input is available.")
else:
    print("Input is not found.")
    
'''
'''Input is not found.'''

'''
#Write a Python program to concatenate all elements in a list into a string and return it.

def concate(list):
    str1=""
    for i in list:
        str1 = str1 + " "+ str(i)
    return str1
output= concate([2,6,"hello",45.6,True])
print(output)
'''

''' 2 6 hello 45.6 True'''

'''
#Write a Python program to print all even numbers from a given numbers list in the same order 
# and stop the printing if any numbers that come after 237 in the sequence

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

def print_num(numbers):
    for i in numbers:
        if i == 237:
            break
        elif i % 2 ==0:
            print(i , end=" ")

print_num(numbers)
'''

'''386 462 418 344 236 566 978 328 162 758 918'''

'''
#Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
miss_color_set= set()
def check_list(list1,list2):
    for i in list1:
        if i in list2:
            continue
        else:
            miss_color_set.add(i)
check_list(color_list_1,color_list_2)            
print("Elements not present in 2nd set")
print(miss_color_set)
print("Set1 element not available in Set2") # Use DIFFRENCE method to check diff in two set
print(color_list_1.difference(color_list_2))
print("Set2 element not available in Set1")
print(color_list_2.difference(color_list_1))
'''

'''
Elements not present in 2nd set
{'White', 'Black'}
Set1 element not available in Set2
{'White', 'Black'}
Set2 element not available in Set1
{'Green'}

'''            
'''
#Write a Python program that will accept the base and height of a triangle and compute the area.
base=int(input("Enter Base of triangle :"))
height=int(input("Enter Height of triangle :"))

def areaOfTriangle(base,height):
    return (1 / 2) * base * height

area=areaOfTriangle(base,height)
print("Area of triangle is :"+str(area))

'''            
'''
Enter Base of triangle :10
Enter Height of triangle :10
Area of triangle is :50.0
'''
'''         #Method1
#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

num1=int(input("Enter 1st num :"))
num2=int(input("Enter 2nd num :"))

def hcf(num1,num2):
    counter=0
    out=1
    for i in range(num1 if num1 <num2 else num2,1,-1):
        counter += 1
        if num1 % i == 0 and num2 % i == 0:
            out=i
            break
    else:
        out=1
    print("Val of counter is :"+str(counter))
    return out
gcd=hcf(num1,num2) 
print("Value of GCD is :"+str(gcd))
'''
'''
list =[1,2,3,4,5,6,7,8,9]
for i in range (9,2,-1):
    print(i, end=" ")

'''
'''             #Method 2
def gcd(x, y):
   gcd = 1  
   counter=0 
   if x % y == 0:
       return y   
   for k in range(int(y / 2), 0, -1):
       counter += 1
       if x % k == 0 and y % k == 0:
           gcd = k
           break 
   print("value of counter is :"+str(counter))
   return gcd
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(189, 265))
'''

#Write a Python program to get the least common multiple (LCM) of two positive integers

'''to be implemented'''

'''
#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

def sum(a,b,c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b+ c
print("Sum of 5,6,4 is :"+ str(sum(5,6,4)))
print("Sum of 8,6,6 is :"+ str(sum(8,6,6)))
print("Sum of 1,2,3 is :"+ str(sum(1,2,3)))
'''
'''
Sum of 5,6,4 is :15
Sum of 8,6,6 is :0
Sum of 1,2,3 is :6
'''

'''
#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

def sum(a,b):
    return 20 if a + b >=15 and a + b <= 20  else a + b
print("Sum of 5,6 is :"+ str(sum(5,6)))
print("Sum of 6,4 is :"+ str(sum(6,4)))
print("Sum of 8,9 is :"+ str(sum(8,9)))
print("Sum of 10,8 is :"+ str(sum(10,8)))
'''
'''
Sum of 5,6 is :11
Sum of 6,4 is :10
Sum of 8,9 is :20
Sum of 10,8 is :20
'''
'''
#Write a Python program that will return true if the two given integer values are equal 
# or their sum or difference is 5

def check(a,b):
    return True if a == b or a + b == 5 or a - b == 5 else False

print(check(15,18))
print(check(25,20))
print(check(2,3))
print(check(34,70))
'''
'''
False
True
True
False
'''

'''
#Write a Python program to add two objects if both objects are an integer type.
def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):      #isinstance check object type
       return "Inputs must be integers!"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))
'''

'''
30
Inputs must be integers!
Inputs must be integers!
Inputs must be integers!
'''
'''
#Write a Python program to display your details like name, age, address in three different lines.
name='vinod'
age=27
address='Nashik'
print(name+"\n"+str(age)+"\n"+address)
'''
'''
vinod
27
Nashik
'''
'''
#Write a Python program to solve (x + y) * (x + y).

def formula(x,y):
    return (x + y) * (x + y)
print(formula(7,5))
print(formula(4,6))
print(formula(12,9))
'''
'''
144
100
441
'''

'''
#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years

principal,int_rate,years = 10000, 3.5, 7
def amount(principal,int_rate,years):
    amt= principal  * ( 1 + (int_rate / 100)) ** years
    return amt
amt=amount(principal,int_rate,years)    
print (f"Total amount of {principal} with interest rate of {int_rate} for {years} years is {amt}")
'''

'''Total amount of 10000 with interest rate of 3.5 for 7 years is 12722.792627665729'''

'''
#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
#formaula  -> \/`(x2-x1)^2 + (y2-y1)^2
import math
a = [4,0]           # x1=4, y1=5
b = [6,6]           # x2=6, y2=8
value=math.sqrt(((a[0] - b[1]) ** 2 + (a[1]-b[1]) ** 2))
print("Distance between two point is : "+str(value))
'''
''' Distance between two point is : 6.324555320336759'''

'''
#Write a Python program to check whether a file exists.
import os                       # isfile or exists both function of os.path is used to check a file exists or not
# Method 1
print(os.path.isfile('E:\\PYSPARK\\input\ContainsNull.csv'))
print(os.path.isfile('E:\\PYSPARK\\input\ContainsNull1.csv'))
# Method 2
print(os.path.exists('E:\\PYSPARK\\input\ContainsNull.csv'))
print(os.path.exists('E:\\PYSPARK\\input\ContainsNull1.csv'))
# Method 3
my_file = open('E:\\PYSPARK\\input\ContainsNull.csv')
try:
   my_file.close()
   print("File found!")
except FileNotFoundError:
   print("File not found!")
'''

'''
True
False
True
False
File found!

--> Error if file not found
FileNotFoundError: [Errno 2] No such file or directory: 'E:\\PYSPARK\\input\\ContainsNull1.csv'
'''

#Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('E:\\PYSPARK\\input') if isfile(join('E:\\PYSPARK\\input', f))]
print(files_list) 