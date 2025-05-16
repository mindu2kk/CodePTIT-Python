"""
2
12341
123456789123456789
"""
def calc(n):
    return sum(int(i) for i in n)

t = int(input())
for _ in range(t):
    n = input()
    if calc(n) % 3 == 0:
        print("YES")
    else:
        print("NO")

