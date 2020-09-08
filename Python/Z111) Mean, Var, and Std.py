#Solution:

import numpy
N,M = map(int,input().split(" "))
array =numpy.array([input().split() for _ in range(M)],int)
numpy.set_printoptions(sign=" ")
print(numpy.mean(array,axis=1),numpy.var(array,axis=0),numpy.around(numpy.std(array,axis=None),decimals=12),sep="\n")
