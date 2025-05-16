"""
Cho N số nguyên. Nhiệm vụ của bạn là phân tích các số nguyên đã cho dưới dạng tích của các thừa số nguyên tố, sau đó tính tổng các ước số nguyên tố này.

Input:
Dòng đầu tiên số nguyên N (1 ≤≤ N ≤ 106).
N dòng tiếp theo, mỗi dòng gồm một số nguyên có giá trị không vượt quá 2*106.

Output
In ra một số nguyên là đáp án tìm được.

5
7
9
10
13
100
"""
from sys import stdin
from math import isqrt

def tach(n):
    summ = 0
    while n % 2 == 0:
        n //= 2
        summ += 2
    for d in range(3, isqrt(n) + 1, 2):
        while n % d == 0:  # Chia hết nhiều lần
            n //= d
            summ += d
    if n > 1:  # Nếu còn lại số nguyên tố
        summ += n
    return summ

def main():
    n = int(stdin.readline().strip())  # Đọc nhanh hơn input()
    tong = 0
    for _ in range(n):
        a = int(stdin.readline().strip())
        tong += tach(a)
    print(tong)

if __name__ == "__main__":
    main()
