#Solution:


from collections import deque
import re
d = deque()
n = int(input())
str_val = ''
for i in range(n):
    key = input()
    number = re.match(r'(\w+)\s?(\d+)?',key)
    if(number):
        case = number.group(1)
        add = number.group(2)
        if(case == 'append'):
            d.append(add)
        elif(case == 'appendleft'):
            d.appendleft(add)
        elif(case == 'pop'):
            d.pop()
        elif(case == 'popleft'):
            d.popleft()
for j in d:
    str_val = str_val+' '+j
str_val = re.sub(r'(^ )',"",str_val)
print(str_val)
