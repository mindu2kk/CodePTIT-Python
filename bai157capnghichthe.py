"""
Cho dãy số A[] gồm có N phần tử.
Một cặp nghịch thế là một cặp số (u, v) sao cho u < v và A[u] > A[v]. Nhiệm vụ của bạn là hãy đếm số lượng cặp nghịch thế trong dãy số A[] ban đầu.

Input:
Dòng đầu tiên là N (N ≤ 1000), số lượng phần tử trong dãy số ban đầu.
Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 109).

Output:
In ra một số nguyên là số lượng dãy nghịch thế tìm được.
"""

n = int(input())
A = list(map(int,input().split()))
cnt = 0

for u in range(n - 1):
    for v in range(u + 1,n):
        if A[u] > A[v]:
            cnt += 1
print(cnt)
