import sys
from math import gcd

def check(n, k, A):
    min_length = n + 1

    for l in range(n):
        curr = A[l]
        for r in range(l, n):
            curr = gcd(curr, A[r])
            if curr == k:
                min_length = min(min_length, r - l + 1)
                break
            if curr < k:
                break

    return "-1" if min_length == n + 1 else min_length

data = sys.stdin.read().split()
index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n, k = map(int, data[index:index+2])
    index += 2
    A = list(map(int, data[index:index+n]))
    index += n
    print(check(n, k, A))

