#Solution:

def average(array):
    arrays = set(array)
    final_average= sum(arrays)/len(arrays)
    return final_average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
