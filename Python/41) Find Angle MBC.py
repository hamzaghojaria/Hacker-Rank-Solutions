#Solution:

import math
ab = int(input())
bc = int(input())

ac = math.sqrt((ab**2) +(bc**2)) # hypotenuse 


acos = ((bc*bc) + (ac*ac) - (ab*ab)) / (2*(bc*ac))
result = math.degrees(math.acos(acos))
print (str(int((round(result)))) + '°')
