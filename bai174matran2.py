"""
Cho ma trận vuông cấp N*N chỉ bao gồm các số nguyên dương.
Với đường chéo phụ, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo phụ (không tính các phần tử nằm trên đường chéo phụ).
Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy tổng giá trị các phần tử ở nửa trên trừ đi tổng giá trị các phần tử ở nửa dưới.
Nhập thêm một giá trị K gọi là ngưỡng cân đối của ma trận.  Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.
Hãy xác định độ chênh lệch và tính cân đối của ma trận.

Input
Dòng đầu ghi số N (2 < N < 50)
N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.
Dòng cuối ghi số K (0 < K <100)

Output
Dòng đầu ghi chữ YES hoặc NO
Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận
"""

n = int(input())

matrix =[list(map(int,input().split())) for i in range(n)]
k = int(input())

def calc_diff(matrix,n,k):
    low = 0
    upper = 0
    for i in range(n):
        for j in range(n):
            if i < n - j - 1:
                low += matrix[i][j]
            elif i > n - j - 1:
                upper += matrix[i][j]
    return abs(low - upper)

diff = calc_diff(matrix, n, k)
if diff <= k:
    print("YES")
else:
    print("NO")
print(diff)