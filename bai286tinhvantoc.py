"""
Cuộc đua xe đạp bắt đầu từ 6h00 với độ dài quãng đường đua là 120 Km. Các cua-rơ sẽ được ghi nhận thành tích dựa trên thời điểm đến đích. Hãy xếp hạng theo thứ tự thành tích giảm dần.

Input
Dòng đầu ghi số cua-rơ tham gia cuộc đua.
Mỗi cua-rơ ghi trên 3 dòng:
Họ tên (xâu ký tự độ dài không quá 50)
Đơn vị (xâu ký tự độ dài không quá 20)
Thời điểm đến đích theo định dạng h:mm

Output
Ghi ra danh sách đã sắp xêp theo thành tích, tốt hơn xếp trước, kém hơn xếp sau.
Thông tin mỗi cua-rơ bao gồm:
Mã (là chữ cái đầu tiên của các từ trong tên đơn vị ghép với chữ cái đầu tiên các từ trong họ tên – xem ví dụ để hiểu rõ hơn)
Họ tên
Đơn vị
Vận tốc trung bình (đã làm tròn ra giá trị nguyên)

3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
"""
class Dua:
    def __init__(self, ten, diadiem,tg):
        self.ten = ten
        self.diadiem = diadiem
        self.tg = tg
    def ma(self):
        return ''.join(i[0] for i in self.diadiem.split()) + ''.join(i[0] for i in self.ten.split())

    def vantoc(self):
        thoigian_dua = self.tg
        return round(120 / (thoigian_dua / 60))

    def thongtin(self):
        return f'{self.ma()} {self.ten} {self.diadiem} {self.tg} {self.vantoc()} Km/h'
n = int(input())
ds = []

for i in range(n):
    ten = input()
    diadiem = input()
    td = [int(i) for i in input().split(':')]
    tg = td[0] * 60 + td[1] - 360
    ds.append(Dua(ten, diadiem, tg))
ds.sort(key = lambda x: x.tg)
for i in ds:
    print(i.thongtin())