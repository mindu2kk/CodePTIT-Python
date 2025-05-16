"""

"""

import math

# Hàm tính Euler's Totient Function 𝜙(N)
def euler_totient(n):
    result = n
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p  # Loại bỏ tất cả bội số của p
            result -= result // p  # Áp dụng công thức 𝜙(N)
    if n > 1:  # Nếu còn lại một số nguyên tố > sqrt(N)
        result -= result // n
    return result

# Hàm kiểm tra số nguyên tố
def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True

# Xử lý input
t = int(input())  # Số bộ test
for _ in range(t):
    n = int(input())  # Nhập N
    k = euler_totient(n)  # Tính 𝜙(N)
    print("YES" if is_prime(k) else "NO")
