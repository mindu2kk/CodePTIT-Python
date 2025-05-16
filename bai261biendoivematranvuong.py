"""
Cho ma trận A kích thước N*M chỉ bao gồm các số nguyên dương.
Trong trường hợp N # M, hãy biến đổi ma trận A về dạng ma trận vuông theo quy tắc sau:
Nếu N > M, hãy loại bỏ các hàng có thứ tự lẻ trong ma trận ban đầu (thứ tự hàng tính từ 1) cho đến khi N = M. Ví dụ N = 6, M = 4 thì cần loại bỏ hàng thứ 1 và hàng thứ 3.
Nếu M > N, hãy loại bỏ các cột có thứ tự chẵn trong ma trận ban đầu (thứ tự cột tính từ 1). Ví dụ: N = 4, M = 6 thì cần loại bỏ cột thứ 2 và cột thứ 4.
In ra ma trận kết quả sau khi biến đổi.

Input
Dòng đầu ghi hai số N và M (1 < N,M < 50).
N dòng tiếp theo ghi các phần tử của ma trận A, các giá trị đều nguyên dương và không quá 1000.

Output
Ghi ra ma trận vuông sau khi biến đổi.

6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9
"""

def transform(matrix,n,m):
    if n > m:
        remove = 0
        new_matrix = []
        for i in range(n):
            if i % 2 == 0 and remove < n - m:
                remove += 1
            else:
                new_matrix.append(matrix[i])
        matrix = new_matrix
    elif m > n:
        remove = 0
        keep_idx = []
        for j in range(m):
            if j % 2 == 1 and remove < m - n:
                remove += 1
            else:
                keep_idx.append(j)
        matrix = [[row[j] for j in keep_idx] for row in matrix]
    return matrix

n,m = map(int,input().split())

matrix = list(map(int,input().split()) for i in range(n))
result = transform(matrix,n,m)
for row in result:
    print(*row)
