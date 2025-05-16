"""
Cho dãy số nguyên dương A[] có N phần tử.
Hãy viết chương trình liệt kê các số nguyên tố khác nhau và số lần xuất hiện của số đó trong dãy ban đầu.
Các số được liệt kê theo thứ tự xuất hiện.

Input
Dòng đầu ghi số N (không quá 500).
Dòng sau ghi N số của dãy (không quá 6 chữ số).

Output
Ghi ra các số nguyên tố khác nhau trong dãy theo thứ tự xuất hiện và số lần xuất hiện. Mỗi số liệt kê trên 1 dòng.
10
2 4 7 5 7 8 9 3 7 2
"""
from collections import Counter
from math import isqrt

def nto(x):
    n = int(x)
    if n == 1:
        return False
    for i in range(2,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
A = list(map(int,input().split()))

freq = Counter(A)

for num,cnt in freq.items():
    if(nto(num)):
        print(num,cnt)
