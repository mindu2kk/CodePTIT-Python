def max_smaller_number(n_str):
    n = list(n_str)
    length = len(n)
    i = -1
    for idx in range(length - 2, -1, -1):
        if n[idx] > n[idx + 1]:
            i = idx
            break
    if i == -1:
        return "-1"
    j = max((j for j in range(i + 1, length) if n[j] < n[i]), key=lambda x: n[x])
    n[i], n[j] = n[j], n[i]
    return "-1" if n[0] == '0' else "".join(n)

T = int(input().strip())
for _ in range(T):
    n_str = input().strip()
    print(max_smaller_number(n_str))

"""
4
354
999
100
11101
"""