#Solution:


K = int(input())
groups = set()
testing = set()

for i in input().split(" "):
    if i not in testing:
        testing.update([i])
        groups.update([i])
    else:
        groups.discard(i)
print (*groups)
