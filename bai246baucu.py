"""
Khu dân cư ABC tiến hành bầu tổ trưởng dân phố. Có M ứng viên và N cử tri.
Người dân trong khu dân cư đã chán ngấy với việc các ứng viên vận động tranh cử,
câu kéo phiếu bầu trong các nhiệm kỳ trước nên họ quyết định đặt ra quy định mới như sau:
Các ứng viên được đánh số từ 1 tới M. Mỗi cử tri sẽ viết ra đúng 1 số thứ tự ứng viên mình muốn chọn
và bỏ vào hòm phiếu.
Người trúng cử là người có số phiếu bầu nhiều thứ hai
Nếu không có người đứng thứ hai thì kết quả bầu cử sẽ bị hủy bỏ
Nếu có nhiều hơn 1 người cùng có số phiếu nhiều thứ hai thì người nào có số thứ tự nhỏ nhất sẽ được chọn.
Viết chương trình xác định người trúng cử.

Input
Dòng đầu ghi hai số N và M (1 < M < 10, 5 < N < 500).
Dòng thứ 2 ghi N giá trị trong các phiếu bầu. Các giá trị đảm bảo hợp lệ (tức là từ 1 đến M).

Output
Ghi ra số thứ tự của người trúng cử.
Hoặc nếu không có ai trúng cử thì ghi ra NONE

10 4
2 3 1 2 3 4 1 2 3 2
"""

N, M = map(int, input().split())
votes = list(map(int, input().split()))

count = [0] * (M + 1)
for v in votes:
    count[v] += 1

max1, max2 = 0, 0
for c in count:
    if c > max1:
        max2, max1 = max1, c
    elif max1 > c > max2:
        max2 = c

if max2 == 0:
    print("NONE")
else:
    for i in range(1, M + 1):
        if count[i] == max2:
            print(i)
            break



