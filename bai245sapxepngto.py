"""
Cho dãy số nguyên dương A[] có N phần tử. Các giá trị trong dãy không quá 1000.
Hãy sắp xếp các số nguyên tố trong dãy theo thứ tự tăng dần. Các giá trị không nguyên tố vẫn giữ nguyên vị trí như lúc đầu.
Xem ví dụ để hiểu rõ hơn yêu cầu bài toán.

Input
Dòng đầu ghi số N (1 < N < 100), dòng thứ 2 ghi N số của dãy A[].

Output
Ghi ra dãy số kết quả trên một dòng.

8
4 6 3 8 7 2 5 9
"""
from math import isqrt


def nto(num):
    if num < 2:
        return False
    for i in range(2,isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
A = list(map(int,input().split()))
prime = list(sorted(num for num in A if nto(num)))
idx = 0
res = []
for i in range (0,len(A)):
    if nto(A[i]):
        res.append(prime[idx])
        idx += 1
    else:
        res.append(A[i])
print(*res)
