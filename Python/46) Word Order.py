#Solution:

from collections import Counter

n = int(input())
words = [input().strip() for i in range(n)]
counts = Counter(words)

print(len(counts))
print(*counts.values())
