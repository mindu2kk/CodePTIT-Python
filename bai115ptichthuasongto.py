def phantich(n):
    res = ["1"]
    d = 2
    while d * d <= n:
        cnt = 0
        while n % d == 0:
            cnt += 1
            n //= d
        if cnt > 0:
            res.append(f"{d}^{cnt}")
        d += 1 if d == 2 else 2
    if n > 1:
        res.append(f"{str(n)}^1")
    return " * ".join(res)

t = int(input())

for _ in range(t):
    n = int(input())
    print(phantich(n))
