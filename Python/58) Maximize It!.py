#solution:


from itertools import *
n, k = list(map(int, input().split()))
num = []
for i in range(n):
    q = list(map(int,input().split()[1:]))
    num.append(list(j**2 for j in q))
print(max(list(sum(i)%k for i in product(*num))))
