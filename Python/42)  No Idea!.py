#Solution:

n,m = input().split(' ')
my_array = list(input().split(' '))
A = set(input().split(' '))
B = set(input().split(' '))

res = 0

for i in my_array:
    res += (i in A) - (i in B)

print(res)
