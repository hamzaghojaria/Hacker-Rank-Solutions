#Solution:

import numpy
N,M = map(int,input().split(" "))
print(numpy.product(numpy.sum(numpy.array([input().split() for _ in range(M)],int), axis = 0), axis = 0))
