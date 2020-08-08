#Solution:

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
from collections import Counter
c = Counter(sorted(s))
for i in c.most_common(3):
    print(*i) 
