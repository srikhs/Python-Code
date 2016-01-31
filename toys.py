#!/bin/python
# This is my solution for https://www.hackerrank.com/challenges/jim-and-the-orders
import sys
a=sys.stdin
abcd=[]
total=[]
count=0
sum=0
for i in a:
    i=i.rstrip()
    ad=i
    count=count+1
    ad1= ad.split(' ')
   
    if(len(ad1)>1):
        
        total.append(int(ad1[0])+int(ad1[1]))
        abcd.append(count-1)

total, abcd = zip(*sorted(zip(total, abcd)))


for item in abcd:
    print item,
