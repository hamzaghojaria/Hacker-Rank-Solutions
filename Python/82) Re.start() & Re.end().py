#Solution:

import re
S,K = input(),input()
m = re.search(K, S)
pattern = re.compile(K)
if not m: print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(),m.end()-1))
    m = pattern.search(S,m.start()+1)
