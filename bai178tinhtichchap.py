"""
Phép tích chập (convolution) là kỹ thuật quan trọng trong xử lý ảnh. Kết quả phép tích chập giữa ma trận x[] và ma trận kernel h[] được xác định bằng công thức:
Trong đó ma trận kernel có kích thước bằng 2k+1. Với kernel 3x3 thì -1 ≤ u,v ≤ 1, do đó, giá trị các phần tử của ma trận kết quả có dạng:
Cho ma trận ảnh và ma trận kernel 3x3. Nhiệm vụ của bạn là hãy thực hiện phép nhân tích chập của 2 ma trận, sau đó tính tổng tất cả các phần tử của ma trận thu được.

Dữ liệu vào:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test bắt đầu bởi hai số nguyên N và M (3 ≤ N,M ≤ 300).
Kế tiếp là N dòng, mỗi dòng gồm M số nguyên mô tả ma trận ảnh.
3 dòng tiếp theo, mỗi dòng gồm 3 số nguyên mô tả ma trận kernel.
Giá trị các phần tử của hai ma trận có giá trị tuyệt đối không vượt quá 100.

Kết quả:
Với mỗi test, hãy in ra tổng các phần tử của ma trận mới tìm được.

2
4 4
2 1 0 0
3 2 1 1
4 3 2 1
2 2 1 0
-1 -1 -1
-1 8 -1
-1 -1 -1
3 3
1 2 3
4 5 6
7 8 9
1 1 1
1 1 1
1 1 1
"""

import sys


def solve():
    N, M = map(int, sys.stdin.readline().split())

    image = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    kernel = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

    total_sum = 0
    for i in range(N - 2):
        for j in range(M - 2):
            current_convolution_val = sum(
                kernel[ki][kj] * image[i + ki][j + kj]
                for ki in range(3) for kj in range(3)
            )
            total_sum += current_convolution_val

    print(total_sum)

num_tests = int(sys.stdin.readline())
for _ in range(num_tests):
    solve()
