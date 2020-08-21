#Solution:

import re
pattern = re.compile('(?<= )(&&|\|\|)(?= )')

def substitution(match):
    string = str(match.group(0))
    if string == '&&':
        return 'and'
    else:
        return 'or'

for _ in range(int(input())):
    print(re.sub(pattern,substitution,input()))
