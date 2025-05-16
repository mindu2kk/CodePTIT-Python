def solve(str_num):
    for i in range(len(str_num) - 1):
        if str_num[i] > str_num[i + 1]:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    str_num = input().strip()
    print(solve(str_num))

"""
2
12345678888888888888889
65645645465754765876857685846
"""