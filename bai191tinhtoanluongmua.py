"""
Trong một ngày mưa nhiều, các trạm đo mưa hoạt động hết công suất. Tại mỗi trạm đo, các cơn mưa được ghi nhận thời điểm bắt đầu, thời điểm kết thúc và lượng mưa đo được. Một trạm mưa có thể có nhiều lần mưa trong ngày.
Hãy tính lượng mưa trung bình trong 1 giờ (60 phút) của từng trạm theo đúng thứ tự trong danh sách ban đầu. Chú ý để tính lượng mưa trung bình thì cần tính tất các lần đo mưa tại trạm đó.

Input
Dòng đầu ghi số lượt đo lượng mưa.
Thông tin về một lần đo lượng mưa gồm 4 dòng:
Tên trạm
Thời điểm bắt đầu mưa (hh:mm)
Thời điểm kết thúc mưa (hh:mm)
Lượng mưa đo được
Số trạm đo khác nhau nhỏ hơn 10.

Output
Ghi ra danh sách các trạm khác nhau trong danh sách đo mưa và lượng mưa trung bình của từng trạm.
Thông tin trên mỗi dòng lần lượt gồm:
Mã trạm đo (tính từ T01). Chú ý: nếu cùng tên trong danh sách đo thì cũng sẽ cùng mà trạm.
Tên trạm đo mưa
Lượng mưa trung bình trong 1 giờ tại mỗi trạm (tính chính xác đến 2 số phần thập phân).
Các thông tin ghi cách nhau một khoảng trống.


Input

Output

10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
"""
def tinh(s):
    tmp = [int(i) for i in s.split(':')]
    return tmp[0] * 60 + tmp[1]

class LuongMua:
    def __init__(self,id,tem,bd,kt,mua):
        self.id = 'T' + '%02d' % id
        self.ten = tem
        self.bd = bd
        self.kt = kt
        self.mua = mua
        self.tg = tinh(kt) - tinh(bd)

    def tinhtg(self,bd,kt):
        self.tg += tinh(kt) - tinh(bd)

    def tinhmua(self,mua):
        self.mua += mua

    def toStr(self):
        return f'{self.id} {self.ten} {(self.mua / self.tg * 60):.2f}'
l = []
dem = 1
t = int(input())

for _ in range(t):
    ok = 0
    ten = input()
    for i in l:
        if i.ten == ten:
            ok = 1
            i.tinhtg(input(),input())
            i.tinhmua(int(input()))
            break
    if ok == 0:
        l.append(LuongMua(dem,ten,input(),input(),int(input())))
        dem += 1
for i in l:
    print(i.toStr())

