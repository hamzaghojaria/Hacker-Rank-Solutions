#Solution:

import re
n=int(input())
for i in range(n):
    x=re.findall(r'#[A-Fa-f0-9]{3,6}[^\s]',input())
    if x==[]:
        continue
    else:
        for i in x:
            a=0
            while a<len(i)-1:
                print(i[a], end='')
                a=a+1
            print(end='\n')
