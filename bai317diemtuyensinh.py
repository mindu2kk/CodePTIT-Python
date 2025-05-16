"""
Theo quy định mới, điểm tuyển sinh vào trường đại học XYZ sau khi tính tổng sẽ được cộng ưu tiên, cụ thể:
Thí sinh khu vực 1 ưu tiên 1.5 điểm
Thí sinh khu vực 2 ưu tiên 1 điểm
Thí sinh khu vực 3 không ưu tiên
Thí sinh dân tộc Kinh không ưu tiên
Thí sinh các dân tộc khác ưu tiên 1.5 điểm
Hãy tính tổng điểm đã ưu tiên và xác định tình trạng trúng tuyển. Biết điểm chuẩn của trường năm nay là 20.5 điểm.

Input
Dòng đầu ghi số thí sinh.
Mỗi thí sinh ghi trên 4 dòng gồm:
Họ tên: có thể chưa chuẩn hóa
Điểm thi: giá trị số thực không quá 30
Dân tộc
Khu vực

Output
Ghi ra danh sách đã sắp xếp theo tổng điểm (đã tính ưu tiên) giảm dần, nếu tổng điểm bằng nhau thì sắp xếp theo mã thí sinh tăng dần. Các thông tin cần liệt kê gồm:
Mã thí sinh (tính theo thứ tự nhập từ TS01)
Họ tên đã chuẩn hóa
Tổng điểm với đúng 1 chữ số phần thập phân
Trạng thái: Do hoặc Truot

2
Nguyen  hong ngat
22
Kinh
1
  Chu thi MINh
14
Dao
3
"""
class TS():
    def __init__(self,stt,ten,diem,dantoc,khuvuc):
        self.stt = f'TS{stt:02d}'
        self.ten = ten
        self.diem = diem
        self.dantoc = dantoc
        self.khuvuc = khuvuc

    def tongdiem(self):
        diem_uu_tien = 0
        if self.dantoc != 'Kinh':
            diem_uu_tien += 1.5
        if self.khuvuc == '1':
            diem_uu_tien += 1.5
        elif self.khuvuc == '2':
            diem_uu_tien += 1
        return self.diem + diem_uu_tien
    def trangthai(self):
        if self.tongdiem() >= 20.5:
            return 'Do'
        else:
            return 'Truot'
    def chuanhoa(self):
        return ' '.join(x.capitalize() for x in self.ten.split())
    def toStr(self):
        return f'{self.stt} {self.chuanhoa()} {self.tongdiem():.1f} {self.trangthai()}'
n = int(input())
ds = []

for i in range(1,n + 1):
    ten = input().strip()
    diem = int(input().strip())
    dantoc = input().strip()
    khuvuc = input().strip()
    ds.append(TS(i,ten,diem,dantoc,khuvuc))
ds.sort(key = lambda x: (-x.tongdiem(),x.stt))
for i in ds:
    print(i.toStr())