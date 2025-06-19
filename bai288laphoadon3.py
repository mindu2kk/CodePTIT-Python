"""
Cửa hàng điện máy – điện lạnh cần lập hóa đơn tính tiền cho khách hàng. Mỗi mặt hàng sẽ có đơn giá và một số tiền được gọi là chiết khấu trên tổng hóa đơn. Số tiền phải thanh toán sẽ bằng đơn giá * số lượng sau đó trừ đi tiền chiết khấu.

Hãy tính tiền cho từng hóa đơn và sắp xếp theo số tiền giảm dần.

Input

Dòng đầu ghi số lượng hóa đơn. Không quá 20.
Mỗi thông tin hóa đơn gồm 5 dòng:
Mã mặt hàng (xâu ký tự độ dài không quá 10, không có khoảng trống)
Tên mặt hàng (xâu ký tự độ dài không quá 100, có thể có khoảng trống)
Số lượng mua (không quá 50)
Đơn giá (số nguyên dương có thể đến 10 chữ số)
Tiền chiết khấu của hóa đơn (có thể đến 9 chữ số).

Output
Ghi ra danh sách hóa đơn đã sắp xếp, trong đó mỗi dòng gồm đầy đủ 6 thông tin: mã mặt hàng, tên mặt hàng, số lượng mua, đơn giá, chiết khấu và tổng tiền. Mỗi thông tin cách nhau một khoảng trống.

3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
"""

class HoaDon:
    def __init__(self,ma,ten,sl,dongia,ck):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.dongia = dongia
        self.ck = ck
    def tien(self):
        return self.dongia * self.sl - self.ck
    def toStr(self):
        return f"{self.ma} {self.ten} {self.sl} {self.dongia} {self.ck} {self.tien()}"

n = int(input())
ds = []

for i in range(1,n+1):
    ma = input()
    ten = input()
    sl = int(input())
    dongia = int(input())
    ck = int(input())
    ds.append(HoaDon(ma,ten,sl,dongia,ck))

ds.sort(key = lambda x : -x.tien())

for i in ds:
    print(i.toStr())

