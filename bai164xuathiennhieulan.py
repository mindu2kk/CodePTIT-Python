"""
Cho dãy số A[] gồm có N phần tử. Nhiệm vụ của bạn là hãy tìm một số có tần số xuất hiện nhiều nhất, yêu cầu lớn hơn N/2 lần xuất hiện trong dãy số.
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu.
Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 1 000 000).

Output:
Với mỗi test in ra đáp án của bài toán trên một dòng. Nếu có nhiều số cùng có tần số xuất hiện nhiều nhất như nhau và đều thỏa mãn số lần lớn hơn N/2 thì in ra số nhỏ nhất.
Nếu không tìm được đáp án, in ra “NO”

2
9
3 3 4 2 4 4 2 4 4
8
3 3 4 2 4 4 2 4
"""
from collections import Counter


def test(n,a):
    freq = Counter(a)
    half = n // 2
    res = float('inf')

    for num,cnt in freq.items():
        if cnt > half:
            res = min(res,num)
    return res if res != float('inf') else "NO"

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(test(n,a))
