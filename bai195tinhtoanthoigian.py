"""
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
"""
class Khach:
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        self.vao = vao
        self.ra = ra
    def tinh(self):
        return (int(self.ra[:2]) - int(self.vao[:2])) * 60  + int(self.ra[3:5]) - int(self.vao[3:5])

    def toStr(self):
        return f'{self.ma} {self.ten} {self.tinh() // 60} gio {self.tinh() % 60} phut'

ds = []
n = int(input())

for i in range(n):
    ma = input()
    ten = input()
    vao = input()
    ra = input()
    ds.append(Khach(ma, ten, vao, ra))
ds.sort(key = lambda x : x.tinh(),reverse = True)
for i in ds:
    print(i.toStr())
