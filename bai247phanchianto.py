"""
Cho dãy số A[] có N phần tử là các số nguyên dương không quá 1000. Sau khi loại bỏ tất cả các giá trị bị lặp lại ở trong A[]
ta tạo được dãy B[] có m phần tử là các giá trị khác nhau theo đúng thứ tự xuất hiện trong dãy A[].
Hãy tìm vị trí i nhỏ nhất (tính từ 0) trong dãy B[] thỏa mãn:
Tổng các phần tử từ B[0] đến B[i] là một số nguyên tố
Tổng các phần tử từ B[i+1] đến B[m-1] cũng là một số nguyên tố.

Input
Dòng đầu ghi số N (1 < N < 500).
Dòng tiếp theo ghi N số của dãy A[]

Output
Ghi ra vị trí i đầu tiên tìm được.
Nếu không có vị trí thỏa mãn thì ghi ra dòng chữ NOT FOUND

10
3 6 7 3 4 7 3 6 4 4

10
3 6 7 3 5 7 3 6 6 7
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

seen = set()
B = []

for num in A:
    if num not in seen:
        B.append(num)
        seen.add(num)
m = len(B)
tong = [0]*(m + 1)

for i in range(m):
    tong[i + 1] = tong[i] + B[i]

for i in range(m):
    sum1 = tong[i + 1]
    sum2 = tong[m] - tong[i + 1]

    if nto(sum1) and nto(sum2):
        print(i)
        break
else:
    print("NOT FOUND")
