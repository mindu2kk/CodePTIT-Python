"""
Khách sạn XYZ có đơn giá (theo ngày) được quy định khác nhau theo từng tầng. Khách hàng đến thuê phòng sẽ được tính tổng số tiền ở theo đơn giá cộng thêm chi phí dịch vụ phát sinh nếu có.
Hãy giúp khách sạn tính tiền phải trả cho từng khách hàng và sắp xếp theo thứ tự tổng tiền giảm dần.

Input
Dòng đầu ghi số khách hàng (không quá 20)
Mỗi khách hàng ghi trên 4 dòng gồm:
Tên khách hàng (xâu ký tự độ dài không quá 100)
Số phòng
Ngày nhận phòng (định dạng dd/mm/yyyy)
Ngày trả phòng (định dạng dd/mm/yyyy)
Tiền dịch vụ phát sinh (số nguyên dương nhỏ hơn 100)

Output
Ghi ra danh sách đã được sắp xếp theo tổng tiền giảm dần bao gồm lần lượt các thông tin:
Mã khách hàng (tự động tăng theo thứ tự nhập, tính từ KH01)
Tên khách hàng
Số phòng
Số ngày ở
Thành tiền

3
Huynh Van Thanh
103
05/06/2010
05/06/2010
15
Le Duc Cong
106
08/03/2010
01/05/2010
220
Tran Thi Bich Tuyen
207
10/04/2010
21/04/2010
96
"""
from datetime import datetime

class HoaDon:
    def __init__(self,stt,ten,sophong,nhan,tra,ps):
        self.stt = f'KH{stt:02d}'
        self.ten = ten
        self.sophong = sophong
        self.nhan = nhan
        self.tra = tra
        self.ps = ps
    def tinhngay(self):
        return (datetime.strptime(self.tra, '%d/%m/%Y') - datetime.strptime(self.nhan, '%d/%m/%Y')).days + 1
    def tien(self):
        if self.sophong[0] == '1':
            return 25
        elif self.sophong[0] == '2':
            return 34
        elif self.sophong[0] == '3':
            return 50
        else:
            return 80

    def total(self):
        return self.tien()*self.tinhngay() + self.ps

    def toStr(self):
        return f'{self.stt} {self.ten} {self.sophong} {self.tinhngay()} {self.total()}'

n = int(input())
ds = []

for i in range(1,n + 1):
    ten = input().strip()
    sophong = input().strip()
    nhan = input().strip()
    tra = input().strip()
    ps = int(input().strip())
    ds.append(HoaDon(i,ten,sophong,nhan,tra,ps))
ds.sort(key = lambda x: -x.total())
for i in ds:
    print(i.toStr())