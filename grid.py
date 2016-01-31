# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
import operator
import sys
a=sys.stdin
abcd=[]
total=[]
count=0
sum=0
new=[]
new1=[]
new1list=[]
new2list=[]
new2=[]
a.next()
a.next()
count=0
for i in a:
    count=count+1
    if i>1:
         i=i.rstrip()
         abcd.append(i)
         abcd.sort()

for word in abcd:
    word1=list(word)
    word1.sort()
    new.append(word1)
        
    #print word1
#print new
for t in range(0,count):
    new1=zip(*new)[t]
    new1=list(new1)
    new1.sort()
    new1list.append(new1)
    #print new1
#print new1list

for g in range(0,count):
    
   
    print1= zip(*new1list)[g]
    new23=list(print1)
    #print new23
    new2list.append(new23)
#print new2list
if new==new2list:
    print 'YES'
else:
    print 'NO'
#print count
