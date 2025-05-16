"""
Cho dãy số A[] gồm có N phần tử. Các phần tử trong dãy số đều xuất hiện với tần suất chẵn, chỉ có duy nhất 1 số có số lần xuất hiện là số lẻ. Nhiệm vụ của bạn là hãy tìm số này.

Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu. N là một số lẻ.
Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 1 000 000).

Output:
Với mỗi test in ra trên mỗi dòng một số nguyên là đáp án của bài toán.

2
7
1 2 3 2 3 1 3
5
1 1 3 3 2
"""
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))

    count = Counter(A)
    for d in A:
        if count[d] % 2 == 1:
            print(d)
            break