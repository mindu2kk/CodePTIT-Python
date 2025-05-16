"""
Doanh nghiệp X cần tuyển một số nhân viên mới. Bài thi tuyển có hai phần: lý thuyết và thực hành. Sau khi tính điểm trung bình, các thí sinh sẽ được xếp thành 4 loại:
Nếu điểm dưới 5 -> TRUOT
Nếu điểm lớn hơn hoặc bằng 5 nhưng nhỏ hơn 8 -> CAN NHAC
Nếu điểm từ 8 đến 9.5 -> DAT
Nếu điểm lớn hơn 9.5 -> XUAT SAC
Điểm các bài thi lý thuyết và thực hành đều là số thực trong phạm vi từ 0 đến 10. Tuy nhiên, khi nhập điểm các bài thi, cán bộ tuyển dụng có thể quên mất dấu . phân cách phần nguyên và phần thập phân. Do đó nếu điểm ghi là 78 thì cần được hiểu là 7.8
Hãy sắp xếp danh sách thí sinh đã được xếp loại theo điểm trung bình giảm dần.

Input
Dòng đầu ghi số thí sinh. Mỗi thí sinh ghi trên 3 dòng lần lượt là:
Họ và tên (xâu ký tự độ dài không quá 100)
Điểm lý thuyết
Điểm thực hành
Mã thí sinh cần được tự động gán theo mẫu TS + số thứ tự (tính từ 01).

Output
Ghi ra danh sách thí sinh đã sắp xếp, mỗi thí sinh gồm 4 thông tin: mã thí sinh, họ tên, điểm trung bình (với 2 số phần thập phân) và xếp loại. Mỗi thông tin cách nhau một khoảng trống.

3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
"""
class NhanVien():
    def __init__(self, id, ten, diemTB):
        self.id = f'TS0{id:01d}'
        self.ten = ten
        self.diemTB = diemTB
    def xep(self):
        if self.diemTB >= 9.5:
            return 'XUAT SAC'
        elif self.diemTB >= 8:
            return 'DAT'
        elif self.diemTB >= 5:
            return 'CAN NHAC'
        else:
            return 'TRUOT'

    def toStr(self):
        return f"{self.id} {self.ten} {self.diemTB:.2f} {self.xep()}"

n = int(input())
ds = []
for i in range(1,n + 1):
    ten = input().strip()
    diem1 = input()
    diem2 = input()
    diem1 = float(diem1) / 10 if len(diem1) >= 2 and '.' not in diem1 else float(diem1)
    diem2 = float(diem2) / 10 if len(diem2) >= 2 and '.' not in diem2 else float(diem2)
    tb = (diem1 + diem2) / 2
    ds.append(NhanVien(i,ten,tb))
ds.sort(key=lambda x: -x.diemTB)
for i in ds:
    print(i.toStr())