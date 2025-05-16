"""
Cho ma trận A[] cỡ N*M chỉ bao gồm các số nguyên dương không quá 1000. Hãy kiểm tra các số trong ma trận, nếu giá trị nào là số nguyên tố thì thay thế bằng số 1, không phải thì thay thế bằng số 0.

Input
Dòng đầu ghi 2 số N và M là kích thước ma trận (1 < N,M < 20)
N dòng tiếp theo mỗi dòng có M số mô tả ma trận

Output
Ghi ra ma trận kết quả
"""
from math import isqrt

def nto(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(1 if nto(matrix[i][j]) else 0,end = " ")
    print()