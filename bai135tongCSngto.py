"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

Hãy kiểm tra xem tổng các chữ số của N có phải là một số nguyên tố hay không.

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test ghi số N (không quá 500 chữ số)

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
"""

from math import isqrt

def nto(x):
    n = int(x)
    if n == 1:
        return False
    for i in range(2,isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def test(n):
    tong = sum(int(digit) for digit in n)
    if nto(tong):
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n = input()
    print(test(n))