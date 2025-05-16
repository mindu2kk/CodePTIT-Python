"""
Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:
Số chữ số của nó là một số nguyên tố
Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
3
1234567
22334455667
23400300489898989
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
    cnt = 0
    for char in n:
        if nto(char):
            cnt += 1
    if cnt > len(n) - cnt and nto(str(len(n))):
        return "YES"
    return "NO"
t = int(input())

for _ in range(t):
    n = input()
    print(test(n))