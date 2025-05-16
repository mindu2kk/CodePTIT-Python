"""
Phép toán trên thao tác bit OR lấy 2 dãy bit có độ dài bằng nhau và thực hiện phép toán lý luận bao hàm OR trên mỗi cặp bit tương ứng. Kết quả ở mỗi vị trí sẽ là 0 nếu cả 2 bit là 0, ngược lại kết quả là 1. Trong C, C++, Java toán tử thao tác bit OR được biểu diễn bằng kí hiệu "|" (vạch đứng )
Ví dụ : 10|17 = 01010|10001=11011=27
Cho một mảng a gồm n phần tử. Một dãy con liên tiếp của a được định nghĩa là một dãy a[l], a[l+]),a[l+2],...,a[r] với 1 ≤ l ≤ r ≤ n
Ta định nghĩa phép toán OR của 1 dãy con liên tiếp của mảng a là việc thực hiện phép toán thao tác bit OR của toàn bộ các phần tử trong dãy con đó.
OR(l,r) = a[l] | a[l+1] | a[l+2]|...|a[r]
Nhiệm vụ của bạn là tính giá trị OR của toàn bộ các dãy con của một mảng a cho trước và đếm xem có bao nhiêu giá trị khác nhau.

Input:
Dòng thứ 1 gồm 1 số n (1 ≤ n ≤ 1e5): số phần tử của mảng a
Dòng thứ 2 gồm n số a[1], a[2], ..., a[n] ( 0 ≤ a[i] ≤ 1e9)

Output:
Với mỗi testcase, in ra kết quả trên 1 dòng.
"""

import sys
import math


def can_form_k(n, k, arr):
    # Sắp xếp để chọn phần tử đầu tiên làm gốc
    arr.sort()
    base = arr[0]

    # Tính GCD của các hiệu số |arr[i] - base|
    g = 0
    for i in range(1, n):
        g = math.gcd(g, arr[i] - base)

    # Kiểm tra xem (k - base) có chia hết cho GCD không
    return "YES" if (k - base) % g == 0 else "NO"


# Đọc input nhanh
input = sys.stdin.read
data = input().split()
t = int(data[0])  # Số bộ test
index = 1

results = []
for _ in range(t):
    n, k = int(data[index]), int(data[index + 1])
    arr = list(map(int, data[index + 2: index + 2 + n]))
    index += 2 + n
    results.append(can_form_k(n, k, arr))

sys.stdout.write("\n".join(results) + "\n")

