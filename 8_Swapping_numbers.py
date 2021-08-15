#method 1  Swapping with temp/extra variable
a,b=5,2
print("a before is ",a," and b before is ",b)
temp=a
a=b
b=temp
print("a after is ",a," and b after is ",b)

#Method swapping wothout extra variable
c,d=5,2
print("c before is ",c," and d before is ",d)
d=c+d
c=d-c
d=d-c
print("c after is ",c," and d after is ",d)
