#Solution:

import re
result = ''
for _ in range(int(input())):
    uid = input()
    if len(set(uid)) == 10 and len(re.findall("[A-Z]",uid)) > 1 and len(re.findall("[0-9]",uid)) > 2 and len(re.findall("[^[A-Za-z0-9]]",uid)) == 0:
        result += "Valid\n"
    else:
        result += "Invalid\n"
print(result)
