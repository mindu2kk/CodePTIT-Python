"""
Cho dãy số A[], B[] và C[] là dãy không giảm và có lần lượt N, M, K phần tử.
Nhiệm vụ của bạn là hãy tìm các phần tử chung của 3 dãy số này.

Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm số nguyên N, M và K (1≤ N, M, K ≤ 100 000).
Dòng tiếp theo gồm N số nguyên A[i], rồi M số nguyên B[i] và K số nguyên C[i].
(0 ≤ A[i], B[i], C[i] ≤ 109).

Output:
Với mỗi test, in ra trên một dòng là đáp án thu được. Nếu không tìm được đáp án, in ra “NO”.

3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9
"""
from collections import Counter

t = int(input())

for _ in range(t):
    exits = False

    m,n,k = map(int,input().split())
    arr1 = Counter([int(i) for i in input().split()])
    arr2 = Counter([int(i) for i in input().split()])
    arr3 = Counter([int(i) for i in input().split()])

    for x in arr1.keys():
        if x in arr2.keys() and x in arr3.keys():
            for i in range(min(arr1[x],min(arr2[x],arr3[x]))):
                exits = True
                print(x,end = ' ')
    print('' if exits == True else "NO")