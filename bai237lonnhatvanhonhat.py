"""
Cho dãy số có N số nguyên dương. Các số trong dãy có thể tới 100 chữ số.
Hãy tìm số nhỏ nhất và số lớn nhất trong dãy. Nếu cả dãy bằng nhau thì in ra BANG NHAU.

Input
Có nhiều bộ test. Mỗi bộ test bắt đầu với số N (không quá 20). Tiếp theo là N dòng, mỗi dòng ghi một số trong dãy, giá trị đều nguyên dương nhưng có thể có chữ số 0 ở đâu, và có thể tới 100 chữ số.
Input kết thúc khi N = 0.

Output
Với mỗi test, ghi ra trên một dòng số nhỏ nhất và lớn nhất. Nếu tất cả dãy bằng nhau thì ghi ra BANG NHAU.
"""
import sys


def remove_leading_zeros(s):
    return s.lstrip('0') or '0'  # Nếu toàn bộ là '0' thì trả về '0'


def process():
    while True:
        N = int(sys.stdin.readline().strip())
        if N == 0:
            break

        numbers = [remove_leading_zeros(sys.stdin.readline().strip()) for _ in range(N)]

        min_num = min(numbers)
        max_num = max(numbers)

        if min_num == max_num:
            print("BANG NHAU")
        else:
            print(min_num, max_num)


if __name__ == "__main__":
    process()

"""
3
001
22
33333333333333333333333333333333333
"""