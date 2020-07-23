#Solution:

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1,number + 1):
        o = str(oct(i))
        h = str(hex(i).upper())
        b = str(bin(i))
        print(str(i).rjust(width,' '),o[2:].rjust(width,' '),h[2:].rjust(width,' '),b[2:].rjust(width,' '))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
