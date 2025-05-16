"""
Các hộ gia đình trong thành phố X được chia thành 3 loại A, B, C với định mức sử dụng điện như sau:

Loại A: Định mức 100 kWh
Loại B: Định mức 500 kWh
Loại C: Định mức 200 kWh

Hãy tính toán số tiền phải thanh toán theo quy tắc:
Tính tiền trong định mức:
Nếu số điện (Số cuối - Số đầu) nhỏ hơn định mức thì bằng số điện * 450
Nếu số điện lớn hơn hoặc bằng định mức thì bằng định mức *450

Tiền vượt định mức
Nếu số điện lớn hơn định mức thì bằng (số điện - định mức) *1000

Ngược lại thì bằng 0
Thuế VAT = 5% số tiền vượt định mức.
Chú ý: tiền thuế VAT cũng là số nguyên dương nên có thể lấy số tiền vượt định mức chia phần nguyên cho 20.
Số tiền phải nộp = Tiền trong định mức + Tiền vượt định mức + Thuế VAT

Input
Dòng đầu ghi số khách hàng (không quá 50).
Mỗi khách hàng ghi trên 2 dòng:
Họ tên: có thể chưa chuẩn hóa
Loại hộ gia đình, chỉ số đầu, chỉ số cuối. Mỗi thông tin cách nhau một khoảng trống.

Output
Ghi ra danh sách đã sắp xếp theo tổng số tiền phải trả giảm dần gồm các thông tin:
Mã khách hàng: tính từ KH01 theo thứ tự nhập
Họ tên đã chuẩn hóa
Tiền trong định mức
Tiền vượt định mức
Thuế VAT
Tổng số tiền phải nộp.
Dữ liệu đảm bảo không có hai hộ gia đình nào có cùng số tiền nộp bằng nhau.

2
 nGuyEn Hong Ngat
C 200 278
 Chu thi    minh
A 120 240
"""
class HoaDon:
    def __init__(self,stt,ten,so_dien,loai):
        self.stt = f'KH{stt:02d}'
        self.ten = ten
        self.so_dien = so_dien
        self.loai = loai
        if loai == 'A':
            self.dinhmuc = 100
        elif loai == 'B':
            self.dinhmuc = 500
        else:
            self.dinhmuc = 200
        self.tien2 = self.tinhtien2()
        self.tien1 = self.tinhtien1()
        self.thuevat = self.tien2 // 20
        self.tong = self.tien1 + self.tien2 + self.thuevat
    def chuanhoa(self):
        return ' '.join(x.capitalize() for x in self.ten.split())
    def tinhtien1(self):
        if self.so_dien < self.dinhmuc:
            return self.so_dien * 450
        else:
            return self.dinhmuc * 450

    def tinhtien2(self):
        if self.so_dien > self.dinhmuc:
            return (self.so_dien - self.dinhmuc) * 1000
        return 0

    def toStr(self):
        return f'{self.stt} {self.chuanhoa()} {self.tien1} {self.tien2} {self.thuevat} {self.tong}'

n = int(input())
ds = []

for i in range(1,n + 1):
    ten = input().strip()
    loai,dau,cuoi = map(str,input().split())
    so_dien = int(cuoi) - int(dau)
    ds.append(HoaDon(i,ten,so_dien,loai))

ds.sort(key = lambda x : -x.tong)

for i in ds:
    print(i.toStr())