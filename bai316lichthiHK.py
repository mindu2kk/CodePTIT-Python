"""
Hệ thống quản lý lịch thi học kỳ cho nhiều Môn học, mỗi môn học có các (Có thông tin Mã môn học, tên môn học) Lịch thi học kỳ bao gồm nhiều thông tin gồm: Mã ca thi, Mã môn học, Ngày thi, Giờ thi, Nhóm thi. Mã ca thi được đánh số từ T001, T002 và tự động tăng dần.
Cho danh sách các ca thi, mỗi môn học có nhiều ca thi, hãy thực hiện sắp xếp danh sách các ca thi theo thứ tự ưu tiên như sau ngày tăng dần, giờ tăng dần, mã môn học tăng dần.

Input:
Dòng đầu tiên cho 2 số N, M lần lượt là số môn học và số ca thi.
N * 2 dòng tiếp theo là thông tin mã môn học và tên môn học.
M dòng còn lại mỗi dòng là thông tin lịch thi bao gồm Mã môn học, ngày thi (dd/mm/yyyy) giờ thi (hh:mm) và nhóm thi (dạng xâu ký có 2 ký tự bất kỳ).

Output:
Lịch thi đã sắp xếp như mẫu, mỗi lịch thi trên một dòng

2 10
INT1155
Tin hoc co so 2
INT1339
Ngon ngu lap trinh C++
INT1155 25/11/2021 08:00 01
INT1155 04/12/2021 08:00 02
INT1155 04/12/2021 13:30 03
INT1155 25/11/2021 13:30 04
INT1155 25/11/2021 15:00 05
INT1339 25/11/2021 08:00 01
INT1339 25/11/2021 08:00 02
INT1339 04/12/2021 13:30 03
INT1339 04/12/2021 13:30 04
INT1339 04/12/2021 15:00 05
"""
from datetime import datetime


class Thi:
    def __init__(self, stt, ma, ten, ngay, gio, nhom):
        self.stt = f'T{stt:03d}'
        self.ma = ma
        self.ten = ten
        self.ngay = datetime.strptime(ngay,'%d/%m/%Y')
        self.gio = datetime.strptime(gio,'%H:%M')
        self.nhom = nhom
    def toStr(self):
        return f"{self.stt} {self.ma} {self.ten} {self.ngay.strftime('%d/%m/%Y')} {self.gio.strftime('%H:%M')} {self.nhom}"


n,m = map(int,input().split())
ds = []
mon = {}

for i in range(1,n + 1):
    ma = input()
    ten = input()
    mon[ma] = ten

for i in range(1,m + 1):
    ma,ngay,gio,nhom = map(str,input().split())
    ten = mon[ma]
    ds.append(Thi(i,ma,ten,ngay,gio,nhom))
ds.sort(key = lambda x : (x.ngay,x.gio,x.ma))
for i in ds:
    print(i.toStr())