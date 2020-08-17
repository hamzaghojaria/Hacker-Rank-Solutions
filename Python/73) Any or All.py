#Solution:

N = int(input())
array = [int(_) for _ in input().split()]
array1 = list(map(str,array))
if all(item>0 for item in array):
    if any(item==item[::-1] for item in array1):
        print("True")
    else:
        print("False")
else:
    print("False")
