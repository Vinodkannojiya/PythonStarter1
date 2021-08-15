n=int(input("Enter no of steps :"))
#pattern 1
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Pattern 2
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#Pattern 3
'''
*
* *
* * *
* * * *
* * * * *
'''
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()

#Pattern 4
'''
*
* *
*   *
*     *
* * * * *
'''
for row in range(n):
    for col in range(n):
        if col==0 or row==(n-1) or row==col:
            print('*',end="")
        else:
            print(end=" ")
    print()

#Pattern 5 
'''
*****
 *  *
  * *
   **
    *
'''     

for row in range(n):
    for col in range(n):
        if col==(n-1) or row==0 or row==col:
            print('*',end="")
        else:
            print(end=" ")
    print()


#Pattern 6
'''
1
2 3
4 5 6
7 8 9 10
'''
k=0
for i in range(n):
    for j in range(i):
        k+=1
        print(k,end=" ")
    print()    

#Pattern 7
'''
P
PY
PYT
PYTH
PYTHO
PYTHON
'''
'''
name=input("Enter string value :")    
n=len(name)
for i in range(n+1):
    for j in range(i):
        print(name[j],end="")
    print()
'''

#Pattern 8
'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

#Pattern 9
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()

#Pattern 10
'''
     *
    * *
   *   *
  *     *
 *       *
***********     
'''

for row in range(1,n+1):
    for col in range(1,2*n):
        if row==n or col+row==n+1 or col-row==n-1:
            print('*',end="")
        else:
            print(end=" ")
    print()    

#Pattern 11
'''
     *
    * *
   *   *
  *     *
 *       *
* * * * * *
'''
k=2
for row in range(1,n+1):
    for col in range(1,2*n):
        if col+row==n+1 or col-row==n-1:
            print('*',end="")
        elif row==n and col!=k:
            print("*",end="")
            k +=2
        else:
            print(end=" ")
    print()        

    