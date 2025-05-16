"""
Cho ba số nguyên dương L, R và N. Viết chương trình đếm số lượng các số thỏa mãn cả hai điều kiện:

Nằm trong đoạn [L, R].
Không chia hết cho bất kỳ số nào trong đoạn [2, N].

Input
Với mỗi bộ test:
Dòng đầu gồm 2 số nguyên dương L, R (1 ≤ L, R ≤ 1018).
Dòng thứ 2 chứa số nguyên dương N (2 ≤ N ≤ 50).
Input kết thúc với một dòng chứa số nguyên -1.

Output
Với mỗi bộ test, in ra kết quả trong một dòng.
"""


def count_valid_numbers(L, R, N):
    valid_count = 0

    for num in range(L, R + 1):
        is_valid = True

        for div in range(2, N + 1):
            if num % div == 0:
                is_valid = False
                break

        if is_valid:
            valid_count += 1

    return valid_count


while True:
    # Đọc input
    L, R = map(int, input().split())
    if L == -1:
        break
    N = int(input())

    print(count_valid_numbers(L, R, N))

