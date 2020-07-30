#Solution:

from itertools import permutations

word, numb = input().split(" ")
permutations = list(permutations(word, int(numb)))
permutations.sort()

for i in permutations:
    print("".join(i))
