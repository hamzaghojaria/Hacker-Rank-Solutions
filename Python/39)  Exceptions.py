#solution:

for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as error:
        print("Error Code:",error)
