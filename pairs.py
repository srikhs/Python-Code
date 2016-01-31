#PAIRS Problem Statement
#Given N integers, count the number of pairs of integers whose difference is K.

#Input Format

#The first line contains N and K. 
#The second line contains N numbers of the set. All the N numbers are unique.

#Output Format

#An integer that tells the number of pairs of integers whose difference is K.

#Constraints: 
#N≤105 
#0<K<109 
#Each integer will be greater than 0 and at least K smaller than 231−1.

#Sample Input

#5 2  
#1 5 3 4 2  
#Sample Output

#3

#!/usr/bin/py
# Head ends here
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    test=[]
    count=0
    test1=[]
    for i in a:
        
        b=i       
        
        for j in a:
            if b!=j:
                test.append(j)
        
        test.sort()
       
       # for k in test:
       # print test    
        for kk in test:
            for j in test:
                ss=abs(kk-j)
                temp1=[]
                if ss==k:
                    temp1.extend([kk,j])
                    temp1.sort()
                    if temp1 not in test1:
                      #  print "alre"
                        test1.append(temp1)
                        count=count+1
                    
                    
                    #print kk,j,ss
                    #print "count",count
                
         
        #print temp1
        #print test1   
        
        
            
            
        
        
    #answer = 0
    return count
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)