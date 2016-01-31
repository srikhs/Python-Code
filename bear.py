# This is solution to https://www.hackerrank.com/contests/worldcodesprint/challenges/bear-and-cryptography
import sys
import math
import operator

def divisors(a,b,c):
    #aaa=0
    for n in reversed(range(b)): 
        count=2 
        i=2
        while(i**2 < n):
            if(n%i==0):
                count+=2
            i+=1
        count+=(1 if i**2==n else 0)
        countfinal=count
        #print (countfinal)
        if countfinal==c:
            return n
            break
           
   # return aaa                  
T = int(input().strip())
if T>=1 and T<=50:
    for a0 in range(T):
        A,B = input().strip().split(' ')
        A,B = [int(A),int(B)]
        if A>=1 and A<=10**12:
            if B>=1 and B<=40:
               # print(A)
                aaaa=divisors(1,A+1,B)  
                if aaaa is None:
                    print('-1')
                else:     
                    print (aaaa)
            else:
                print('-1')    
        else:
            print('-1')         
else:
    print('-1')

