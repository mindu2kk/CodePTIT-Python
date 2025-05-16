from math import sqrt,gcd
def nto(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def tong(n):
    return sum(int(digit) for digit in str(n))

def test(a,b):
    g = gcd(a,b)
    return "YES" if nto(tong(g)) else "NO"
T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    print(test(a,b))