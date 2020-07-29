#Solution:

from collections import Counter
x=int(input())
sum=0
shoes =  Counter(map(int, input().split()))
n=int(input())
for i in range(n):
    sn ,sp = map(int,input().split())
    if(shoes[sn]>0):
            sum = sum+sp
            shoes[sn] -= 1

print(sum)
