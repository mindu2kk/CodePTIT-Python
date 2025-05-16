"""
Cho một lưới hình vuông kích thước N*N. Trên một số ô của lưới người ta đặt các đồng xu (ký hiệu bằng chữ cái C (coin)).
 Hãy đếm xem có thể lấy ra bao nhiêu cặp đồng xu ở cùng một hàng hoặc cùng một cột.

Input
Dòng đầu tiên ghi số N (1 ≤ N ≤ 100)
N dòng tiếp theo mô tả trạng thái của lưới, chữ cái C ứng với vị trí có đồng x, dấu chấm tương ứng với ô trống)

Output
Ghi ra số cặp đồng xu đếm được.

4
CC..
C..C
.CC.
.CC.
"""
from itertools import count


def cnt(n,grid):
    total_pair = 0

    for row in grid:
        cnt = row.count('C')
        total_pair += (cnt*(cnt-1)) // 2

    for col in range(n):
        cnt = sum(1 for row in grid if row[col] == 'C')
        total_pair += (cnt*(cnt-1)) // 2
    return total_pair
n = int(input())
grid = [input().strip() for _ in range(n)]

print(cnt(n,grid))