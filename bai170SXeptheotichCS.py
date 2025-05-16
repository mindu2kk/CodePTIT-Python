"""
Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.
Hãy sắp xếp dãy số theo tích các chữ số tăng dần. Nếu tích các chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.

Input
Dòng đầu ghi số bộ test (không quá 10)
Mỗi bộ test gồm 2 dòng:
Dòng đầu là số N (N < 100)
Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.

Output
Với mỗi bộ test, ghi trên một dòng dãy số kết quả.
"""

from math import prod

def product_of_digits(x):
    return prod(int(d) for d in str(x))


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(key=lambda x: (product_of_digits(x), x))

    print(*A)  # In kết quả
