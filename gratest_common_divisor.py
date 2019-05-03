# Uses python3
import sys

def gcd_naive(a, b):
    
    if a%b == 0:
        return b
    else:
        return gcd_naive(b, a%b)
    

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(max(a, b), min(a,b)))
