T = int(input())
for _ in range(T):
    n = input().strip()
    if len(n) >= 4 and n[:2] == n[-2:]:
        print("YES")
    else:
        print("NO")