#solution:

def print_rangoli(size):
        my_str = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(size-1, -size, -1):
        
            print ('-'.join(my_str[size-1:abs(i):-1]+my_str[abs(i):size]).center(4*size-3,'-'))
            
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
