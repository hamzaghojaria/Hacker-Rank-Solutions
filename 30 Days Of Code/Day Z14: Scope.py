#Solution:


class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        a.sort()
        
        mini=a[0]
        maxi=a[-1]
        maximumDifference=maxi-mini
        self.maximumDifference=maximumDifference
        return maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
