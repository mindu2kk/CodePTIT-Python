"""
4 3 2
3 2 2
2
1 2
2
1 3
"""


def solve():
    N, M, K = map(int, input().split())
    prices = list(map(int, input().split()))
    A, B = set(map(int, input().split()[1:])), set(map(int, input().split()[1:]))

    both, only_ti, only_teo, neither = [], [], [], []
    for i, price in enumerate(prices):
        if i + 1 in A and i + 1 in B:
            both.append(price)
        elif i + 1 in A:
            only_ti.append(price)
        elif i + 1 in B:
            only_teo.append(price)
        else:
            neither.append(price)

    both.sort(), only_ti.sort(), only_teo.sort(), neither.sort()
    if len(both) + min(len(only_ti), len(only_teo)) < K:
        print(-1)
        return

    selected = both[:K] + sum(zip(only_ti, only_teo), ())[:2 * max(0, K - len(both))]
    remaining = M - len(selected)
    selected += sorted(only_ti + only_teo + neither + both[K:])[:remaining]

    print(sum(selected) if len(selected) >= M else -1)


solve()
