"""
Công ty XYZ mỗi năm đều cập nhật hồ sơ và gán lại mã cho nhân viên (có đúng 5 ký tự) theo quy tắc sau:
Ký tự đầu tiên là phân loại nhân viên, có 4 nhóm là A, B, C, D
Hai chữ số tiếp theo mô tả số năm công tác
Hai ký tự cuối là mã phòng ban.
Dựa trên loại nhân viên và số năm công tác, hệ số nhân để tính lương được cho trong bảng sau:
Mỗi nhân viên theo hợp đồng sẽ có một giá trị lương cơ bản có thể rất khác nhau. Lương tháng được tính bằng tích của lương cơ bản với số ngày công và hệ số nhân.
Cho trước danh sách phòng ban, gồm mã phòng và tên phòng. Cho trước các thông tin nhân viên gồm mã, tên, lương cơ bản (tính theo ngày – đơn vị nghìn VNĐ) và số ngày công. Hãy tính toán và in ra bảng lương nhân viên trong tháng.

Input
Dòng đầu ghi số phòng ban, mỗi phòng ban viết trên một dòng gồm mã phòng và tên phòng.
Tiếp theo là một dòng ghi số nhân viên, mỗi nhân viên ghi trên 4 dòng gồm mã, tên, lương cơ bản (tính theo ngày), số ngày công.

Output
Lập bảng lương của nhân viên theo đúng thứ tự nhập. Mỗi nhân viên cần ghi ra các thông tin sau đây trên một dòng:
Mã nhân viên
Tên nhân viên
Phòng ban
Lương tháng

2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
"""

class NV:
    def __init__(self,ma,ten,tien,ten_phong):
        self.ma = ma
        self.ten = ten
        self.tien = tien
        self.ten_phong = ten_phong

    def heso(self):
        nam_ct = int(self.ma[1:3])
        loai_nv = self.ma[0]

        he_so = 0
        if loai_nv == 'A':
            if 1 <= nam_ct <= 3:
                he_so = 10
            elif 4 <= nam_ct <= 8:
                he_so = 12
            elif 9 <= nam_ct <= 15:
                he_so = 14
            else:
                he_so = 20
        elif loai_nv == 'B':
            if 1 <= nam_ct <= 3:
                he_so = 10
            elif 4 <= nam_ct <= 8:
                he_so = 11
            elif 9 <= nam_ct <= 15:
                he_so = 13
            else:
                he_so = 16
        elif loai_nv == 'C':
            if 1 <= nam_ct <= 3:
                he_so = 9
            elif 4 <= nam_ct <= 8:
                he_so = 10
            elif 9 <= nam_ct <= 15:
                he_so = 12
            else:
                he_so = 14
        elif loai_nv == 'D':
            if 1 <= nam_ct <= 3:
                he_so = 8
            elif 4 <= nam_ct <= 8:
                he_so = 9
            elif 9 <= nam_ct <= 15:
                he_so = 11
            else:
                he_so = 13

        return he_so

    def luong_thang(self):
        return self.tien * self.heso()

    def toStr(self):
        return f'{self.ma} {self.ten} {self.ten_phong} {self.luong_thang() * 1000}'

n = int(input())
ds = []
phong_ban = {}

for i in range(1,n + 1):
    x = input()
    ma_phong = x[:2]
    ten_phong = x[3:]
    phong_ban[ma_phong] = ten_phong
m = int(input())

for i in range(1,m + 1):
    ma = input().strip()
    ten = input().strip()
    luong = int(input())
    ngay_cong = int(input())
    tien = luong * ngay_cong
    ma_phong = ma[3:5]
    ten_phong = phong_ban.get(ma_phong)
    ds.append(NV(ma,ten,tien,ten_phong))
for i in ds:
    print(i.toStr())
