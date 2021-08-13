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
