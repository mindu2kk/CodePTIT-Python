"""
Ma trận kernel trong ví dụ trên có kích thước bằng 5. Với ma trận kernel có kích thước L = 2k + 1, giá trị điểm ảnh (i,j) của ma trận mới sẽ bằng tổng của (2k + 1) x (2k + 1) phần tử (i+u, j+v) với mọi –k ≤ u,v ≤ k, sau đó chia cho (2k + 1) x (2k + 1). Kết quả điểm ảnh mới thu được sau khi thực hiện phép chia sẽ được làm tròn xuống.
Cho ma trận ảnh đầu vào và kích thước L của ma trận kernel, nhiệm vụ của bạn là hãy in ra ma trận ảnh sau khi được làm mịn.

Dữ liệu vào:
Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
Mỗi test bắt đầu bởi hai số nguyên N, M và L (3 ≤ N,M ≤ 500; L ≤ min(n,m)). L được đảm bảo là một số nguyên lẻ.
Kế tiếp là N dòng, mỗi dòng gồm M số nguyên mô tả ma trận ảnh đầu vào, có giá trị trong phạm vi từ 0 tới 255.

Kết quả:
Với mỗi test, hãy in ra ma trận ảnh sau khi đã được làm mịn.
"""

t = int(input())
for z in range(t):
    n, m, l = [int(x) for x in input().split()]
    a = [[0] * (m + 1)] * (n + 1)
    for i in range(1, n + 1):
        a[i] = [0] + [int(x) for x in input().split()]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a[i][j] += a[i][j - 1] + a[i - 1][j] - a[i - 1][j - 1]
    for i in range(1, n - l + 2):
        for j in range(1, m - l + 2):
            k = int((a[i + l - 1][j + l - 1] - a[i - 1][j + l - 1] - a[i + l - 1][j - 1] + a[i - 1][j - 1]) / (l * l))
            print(k, end=' ')
        print()
