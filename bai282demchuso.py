"""
Cho 2 số nguyên A, B. Nhiệm vụ của bạn là hãy đếm xem mỗi chữ số sẽ xuất hiện bao nhiêu lần nếu như liệt kê tất cả các số từ A đến B.

Input

Số đầu tiên là số lượng bộ test T (T ≤ 5000). Mỗi test gồm 2 số nguyên A và B.
Output

Với mỗi test, hãy in ra trên một dòng 10 số nguyên, là tần số xuất hiện của các chữ số từ 0 đến 9.

3
1 9
10 456
123 2437
"""
def count_digits(N):
    if N < 0:
        return [0] * 10

    count = [0] * 10
    factor = 1

    while factor <= N:
        left = N // (factor * 10)
        current = (N // factor) % 10
        right = N % factor

        for d in range(10):
            if d < current:
                count[d] += (left + 1) * factor
            elif d == current:
                count[d] += left * factor + (right + 1)
            else:
                count[d] += left * factor

            if d == 0:
                count[d] -= factor

        factor *= 10

    return count


def count_range(A, B):
    count_B = count_digits(B)
    count_A_minus_1 = count_digits(A - 1)

    result = [count_B[i] - count_A_minus_1[i] for i in range(10)]
    return result


# Đọc input
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(*count_range(A, B))
