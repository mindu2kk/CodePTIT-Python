"""
Cho chuỗi nhị phân S có chiều dài bằng N và số nguyên K. Chọn ngẫu nhiên 2 số nguyên i, j trong khoảng từ 1 tới N.
Xác suất để S[i], S[j] đều là bit 1 và |i-j| ≤ K là bao nhiêu?

Input
Dòng đầu tiên là số lượng bộ test T (T ≤ 100 000).
Mỗi test bắt đầu bởi 2 số nguyên N và K.
Dòng tiếp theo gồm xâu S chứa các kí tự 0 và 1.
Chú ý: Tổng giá trị của N trong tất cả các test ≤ 100 000.

Output
In ra xác suất tìm được dưới dạng phân số tối giản dạng X/Y. Nếu xác suất bằng 0, in ra 0/1.
"""
from bisect import bisect_left,bisect_right
import sys
from math import gcd

t = int(input())

for _ in range(t):
    res = []
    n,k = map(int,input().split())
    s = input()

    ones = [i for i in range(n) if s[i] == '1']
    valid_pair = 0

    for i in range(len(ones)):
        left = bisect_left(ones,ones[i] - k)
        right = bisect_right(ones,ones[i] + k)
        valid_pair += (right - left)

    if valid_pair == 0:
        res.append('0/1')
    else:
        total = n * n
        g = gcd(total,valid_pair)
        res.append(f'{valid_pair // g}/{total // g}')
    print(*res)


