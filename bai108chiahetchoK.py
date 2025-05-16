def solve(a,K,N):
    du = a % K
    start_b = K - du if du != 0 else 0
    res = []

    for b in range(start_b,N - a + 1,K):
        if b > 0:
            res.append(str(b))
    print(" ".join(res) if res else -1)

a,K,N = map(int,input().split())
solve(a,K,N)
