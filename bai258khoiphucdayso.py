"""
Bình có sẵn dãy số A có N phần tử và tạo ra ma trận B kích thước N*N theo quy tắc:

B[i][i] = 0
B[i][j] = A[i] + A[j] (với i#j)
Bình đưa cho Nam ma trận B và đố Nam khôi phục dãy số A ban đầu.

Hãy giúp Nam nhé.

Input

Dòng đầu ghi số N (1 < N <= 1000).

N dòng tiếp theo ghi ma trận B, các số đều nguyên dương và không quá 100.000.

Output

Ghi ra dãy số A tìm được trên một dòng, mỗi số cách nhau 1 khoảng trống.

2
0 2
2 0
"""


n = int(input())
b = []
for _ in range(n):
    b.append([int(i) for i in input().split()])
if n == 2:
    print(*[b[0][1] // 2] * 2)
else:
    a = [(b[0][1] + b[0][2] - b[1][2]) // 2]
    for i in range(1, n):
        a.append(b[0][i] - a[0])
    print(*a)