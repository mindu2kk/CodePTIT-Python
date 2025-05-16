"""
Nhóm HS cùng nhau đăng ký 3 môn học trong Học kỳ hè năm 2021 theo đúng thứ tự:

Môn 1: Lập trình hướng đối tượng: 3 tín chỉ
Môn 2: Ngôn ngữ lập trình C++: 3 tín chỉ
Môn 3: Tin học cơ sở 2: 2 tín chỉ
Người ta muốn xếp hạng thứ tự các sinh viên trong danh sách theo điểm trung bình giảm dần. Biết rằng điểm trung bình tính đến 2 số phần thập phân và nếu điểm bằng nhau thì thứ hạng cũng bằng nhau.

Input
Dòng đầu ghi số sinh viên (không quá 20).
Mỗi sinh viên ghi trên 4 dòng gồm:
Họ tên: có thể chưa được chuẩn hóa
Điểm môn 1
Điểm môn 2
Điểm môn 3
Các giá trị điểm là số nguyên và đảm bảo trong phạm vi từ 0 đến 10.

Output
Ghi ra danh sách sinh viên đã tính điểm và sắp xếp theo xếp hạng từ cao nhất đến thấp nhất, gồm các thông tin:
Mã sinh viên (tự động tăng theo thứ tự nhập, tính từ SV01)
Họ tên đã chuẩn hóa
Điểm trung bình với đúng 2 số phần thập phân
Xếp hạng
Chú ý: 2 sinh viên có điểm trung bình bằng nhau thì xếp hạng bằng nhau, và nếu có 2 sinh viên hạng là X thì sinh viên tiếp theo trong danh sách có hạng X+2.
Trong trường hợp xếp hạng bằng nhau thì cần sắp xếp theo mã sinh viên tăng dần.

2
 ha Thi kieu     anh
7
6
7
Pham    THI  HAO
6
7
6
"""

class SinhVien:
    def __init__(self,stt,name,diem_tb):
        self.stt = f'SV{stt:02d}'
        self.name = name
        self.diem_tb = diem_tb
        self.xep_hang = 0
    def chuanhoa(self):
        return ' '.join(x.capitalize() for x in self.name.split())
    def toStr(self):
        return f'{self.stt} {self.chuanhoa()} {self.diem_tb:.2f} {self.xep_hang}'

n = int(input())
ds = []

for i in range(1,n + 1):
    name = input().strip()
    diem1 = float(input())
    diem2 = float(input())
    diem3 = float(input())
    diem_tb = (diem1 * 3 + diem2 * 3 + diem3 * 2) / 8
    diem_tb = round(diem_tb + 1e-9, 2)
    ds.append(SinhVien(i,name,diem_tb))

ds.sort(key = lambda x : (-x.diem_tb,x.stt))
hang,diemtrc,dem = 1,-1,0

for i,sv in enumerate(ds):
    if sv.diem_tb == diemtrc:
        dem += 1
        sv.xep_hang = hang
    else:
        hang += dem
        diemtrc = sv.diem_tb
        sv.xep_hang = hang
        dem = 1
for i in ds:
    print(i.toStr())