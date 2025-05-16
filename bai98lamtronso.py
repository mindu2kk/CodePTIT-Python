"""
7
15
14
5
99
12345678
44444445
1445
"""

def round_number(n):
    factor = 10  # Bắt đầu làm tròn từ hàng chục
    while n >= factor:
        remainder = n % factor
        n -= remainder  # Bỏ phần dư
        if remainder >= factor // 2:  # Nếu phần dư >= 5, làm tròn lên
            n += factor
        factor *= 10  # Chuyển sang bậc tiếp theo (trăm, nghìn, ...)

    return n

t = int(input())  # Số bộ test
for _ in range(t):
    n = int(input())  # Nhập số nguyên dương
    print(round_number(n))
