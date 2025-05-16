"""
Chọn ngẫu nhiên một số X trong đoạn [A, B], sau đó chọn ngẫu nhiên một bit của X. Xác suất để bit chọn được là bit 1 bằng bao nhiêu?

Input
Dòng đầu tiên là số lượng bộ test T (T ≤ 200).
Mỗi test gồm 2 số nguyên A và B (1 ≤ A ≤ B ≤ 10^10).

Output
In ra đáp án tìm được với độ chính xác 5 chữ số sau dấu phảy.
"""
from fractions import Fraction


def probability(A, B):
    total_ones = 0  # Tổng số bit 1
    total_bits = 0  # Tổng số bit
    current = A

    while current <= B:
        length = current.bit_length()  # Số bit của số nhỏ nhất trong nhóm
        next_power = 1 << length  # 2^length (số lớn nhất có cùng số bit)
        end = min(B, next_power - 1)  # Giới hạn đoạn [current, end]

        count = end - current + 1  # Số lượng số trong nhóm
        total_bits += length * count  # Tổng số bit xuất hiện
        total_ones += (length // 2) * count  # Tổng số bit 1 trung bình

        current = end + 1  # Chuyển sang nhóm tiếp theo

    return float(Fraction(total_ones, total_bits))  # Trả về kết quả dạng số thực


# Đọc dữ liệu đầu vào
t = int(input())

for _ in range(t):
    A, B = map(int, input().split())
    print(f"{probability(A, B):.5f}")
