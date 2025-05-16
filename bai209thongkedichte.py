"""
Trước diễn biến phức tạp của dịch bệnh, thành phố đang có chủ chương thống kê dịch tễ các trường hợp liên quan đến bệnh nhân mắc COVID-19.
Thông tin về bệnh nhân được biểu diễn trên ma trận. Bạn hãy thực hiện thống kê nhanh các trường hợp có nguy cơ lây nhiễm. Nguyên tắc tính là đếm các trường hợp xung quanh bệnh nhân đã tiếp xúc (8 ô xung quanh).

Input:
Dòng đầu tiên là 2 số M, N là các số nguyên <= 100, cho biết kích thước của ma trận.
Tiếp theo là ma trận M x N, các số nguyên A[i][j] có giá trị < 10. Vị trí của mỗi bệnh nhân được đánh số -1. Các ô mang giá trị >= 0 thể hiện số trường hợp có nguy cơ lây nhiễm (không tính các bệnh nhân).

Output:
Tổng số các ca có nguy cơ lây nhiễm trên toàn thành phố.
"""


n, m = [int(i) for i in input().split()]
res = 0

move_i = [-1, -1, -1, 0, 0, 1, 1, 1]
move_j = [-1, 0, 1, -1, 1, -1, 0, 1]

vs = [[False for j in range(m+2)] for i in range(n+2)]
a = [[0]*(m+2)]
for i in range(n):
    a += [[0] + [int(i) for i in input().split()] + [0]]
a += [[0]*(m+2)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i][j] == -1:
            for k in range(8):
                if not vs[i+move_i[k]][j+move_j[k]]:
                    res += a[i+move_i[k]][j+move_j[k]]
                    vs[i+move_i[k]][j+move_j[k]] = True
print(res)