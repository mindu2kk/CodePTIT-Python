"""
Viết chương trình khai báo lớp Thí Sinh gồm các thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3 và Tổng điểm.

Đọc thông tin 1 thí sinh từ bàn phím và in ra màn hình 3 thông tin: Họ tên, Ngày sinh, Tổng điểm.

Input

Gồm 5 dòng lần lượt, mỗi dòng ghi 1 thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3. Họ tên không quá 50 chữ cái, Ngày sinh viết đúng chuẩn dd/mm/yyyy. Các giá trị điểm là số thực (float).

Output

Ghi ra Họ tên, Ngày sinh và Tổng điểm. Mỗi thông tin cách nhau một khoảng trống. Điểm được ghi ra với 1 số sau dấu phẩy.

Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
"""
class ThiSinh:
    def __init__(self,ten,ns,diem1,diem2,diem3,tong):
        self.ten = ten
        self.ns = ns
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tong = diem3 + diem2 + diem1

    def inra(self):
        print(f"{self.ten} {self.ns} {self.tong:.1f}")

ten = input().strip()
ns = input().strip()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())
thi_sinh = ThiSinh(ten,ns,diem1,diem2,diem3,0)
thi_sinh.inra()