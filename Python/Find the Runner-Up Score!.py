#Solution:

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) #To split the array in int format
    arr = list(set(list(arr)))      #To set array as a list
    ar = len(arr) 
    arr = sorted(arr)
    print(arr[ar-2])
