"""
Trong đó, phụ phí được hiểu là số tiền tính thêm (theo phần trăm) trên tổng số tiền nước tiêu thụ.
Cho danh sách khách hàng và chỉ số đồng hộ. Hãy sắp xếp danh sách hóa đơn theo tổng số tiền giảm dần.

Input
Dòng đầu ghi số khách hàng (không quá 20).
Mỗi khách hàng viết trên 3 dòng gồm:
Tên khách hàng (xâu ký tự độ dài không quá 50)
Chỉ số cũ
Chỉ số mới
Trong đó chỉ số mới lớn hơn hoặc bằng chỉ số cũ, cả hai đều không quá 4 chữ số.

Output
Ghi ra danh sách khách hàng đã sắp xếp theo tổng tiền giảm dần gồm các thông tin
Mã khách hàng (tự động gán tăng dần theo thứ tự nhập, bắt đầu từ KH01)
Tên khách hàng
Tổng số tiền (được làm tròn ở dạng số nguyên)

3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
"""

class HoaDon:
    def __init__(self,stt,ten,sonuoc):
        self.stt = f'KH{stt:02d}'
        self.ten = ten
        self.sonuoc = sonuoc

    def tinh(self):
        if self.sonuoc <= 50:
            tong_tien = self.sonuoc * 100
            phu_phi = tong_tien * 0.02
        elif self.sonuoc <= 100:
            tong_tien = 50 * 100 + (self.sonuoc - 50) * 150
            phu_phi = tong_tien * 0.03
        else:
            tong_tien = 50 * 100 + 50 * 150 + (self.sonuoc - 100) * 200
            phu_phi = tong_tien * 0.05

        return round(tong_tien + phu_phi)

    def toStr(self):
        return f"{self.stt} {self.ten} {self.tinh()}"


n = int(input())
ds = []
for i in range(1,n + 1):
    ten = input()
    cu = int(input())
    moi = int(input())
    sonuoc = moi - cu
    ds.append(HoaDon(i,ten,sonuoc))
ds.sort(key = lambda x: x.tinh(),reverse = True)
for i in ds:
    print(i.toStr())