"""

2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
"""
from datetime import datetime

class Phim:
    def __init__(self,ma_phim,ten_tl,ngay,ten,so_tap):
        self.ma_phim = f'P{ma_phim:03d}'
        self.ten_tl = ten_tl
        self.ngay = datetime.strptime(ngay, '%d/%m/%Y')
        self.ten = ten
        self.so_tap = so_tap
    def toStr(self):
        return f'{self.ma_phim} {self.ten_tl} {self.ngay.strftime('%d/%m/%Y')} {self.ten} {self.so_tap}'

n,m = map(int,input().split())
ds = []
the_loai = {}
for i in range(1,n + 1):
    ten_tl = input()
    ma_tl = f'TL{i:03d}'
    the_loai[ma_tl] = ten_tl
for i in range(1,m + 1):
    ma_tl = input().strip()
    ngay = input().strip()
    ten = input()
    so_tap = int(input())
    ten_tl = the_loai[ma_tl]
    ds.append(Phim(i,ten_tl,ngay,ten,so_tap))
ds.sort(key = lambda x: (x.ngay,x.ten,-x.so_tap))
for i in ds:
    print(i.toStr())
