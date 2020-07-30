#Solutions:

from itertools import combinations

s , numb  = input().split()

for i in range(1, int(numb)+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))
