"""
Cho dãy số A[] có N số nguyên dương. Người ta muốn biến đổi tất cả các số trong dãy về số nguyên tố. Tại mỗi bước, mỗi số chưa nguyên tố được phép tăng hoặc giảm 1 đơn vị để biến đổi dần về số nguyên tố gần nhất.
Hãy tính xem cần ít nhất bao nhiêu bước cần thực hiện để biến đổi tất cả các phần tử của dãy về nguyên tố.

Input
Dòng đầu ghi số N là số phần tử của dãy (không quá 200).
Dòng thứ 2 ghi N số của dãy, các giá trị đều nguyên dương và không quá 10000.

Output
Ghi ra số bước ít nhất tính được.

8
13 5 8 7 9 15 26 34
"""
from math import isqrt


def nto(so):
    if so < 2:
        return False
    for i in range(2,isqrt(so) + 1):
        if so % i == 0:
            return False
    return True

def nearest(num):
    if nto(num):
        return num
    lower,upper = num,num
    while not nto(lower):
        lower -= 1
    while not nto(upper):
        upper += 1

    return lower if (num - lower) <= (upper - num) else upper

def test(n,A):
    step = []
    for num in A:
        ans = nearest(num)
        steps = abs(num - ans)
        step.append(steps)
    print(max(step))

n = int(input())
A = list(map(int,input().split()))

test(n,A)
