# Enter your code here. Read input from STDIN. Print output to STDOUT
# This is solution to : https://www.hackerrank.com/challenges/mark-and-toys
def max_toys(prices, rupees):
  #Compute and return final answer over here
  answer = 0
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
 # print max_toys(prices, k)

count=0
sum=0
prices1=[]
prices2=[]
for i in prices:
    if i<k:
        
         prices1.append(int(i))
prices1.sort()
    
   

for j in prices1:
    if sum<k and j<k and sum+j<k:
         count=count+1
         sum=sum+j


print count