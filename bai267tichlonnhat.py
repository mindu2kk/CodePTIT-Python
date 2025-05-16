"""
Cho dãy số A gồm N phần tử là các số nguyên. Hãy tính tích lớn nhất của 2 hoặc 3 phần tử trong dãy.

Input
Dòng đầu tiên ghi số N (3 ≤ N ≤ 10000)
Dòng thứ 2 ghi N số của dãy A (|Ai| ≤ 1000)

Output
Ghi ra kết quả trên một dòng

6
5 10 -2 3 5 2
"""

n = int(input())
A = list(map(int,input().split()))

A = sorted(A)
max1 = A[0] * A[1]
max2 = max1 * A[-1]
max3 = A[-3] * A[-2] * A[-1]

maxs1 = max(max1,max2,max3)
print(maxs1)