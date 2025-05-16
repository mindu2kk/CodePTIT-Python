"""
Trường THPT ACB tuyển giáo viên mới cho ba môn Toán, Lý, Hóa. Theo yêu cầu mới, bài thi tuyển gồm 2 nội dung: Tin học và Chuyên môn. Điểm thi Tin học sẽ được nhân đôi khi tính tổng điểm.
Mỗi GV có thể có điểm ưu tiên được xét theo mã như trong bảng sau:
Mã xét tuyển gồm 2 thành phần. Chữ cái đầu tiên ứng với môn học: A là Toán, B là Lý và C là Hóa; tiếp theo là 1 chữ số thể hiện mã ưu tiên.
Tổng điểm sau khi cộng điểm ưu tiên nếu từ 18 trở lên sẽ được xét TRÚNG TUYỂN, nhỏ hơn sẽ bị LOẠI.
Viết chương trình nhập danh sách điểm thi và sắp xếp GV theo thứ tự tổng điểm giảm dần. Mã GV dự thi được tự động gán theo thứ tự bắt đầu từ 01.

Input
Dòng đầu thi số giáo viên đăng ký thi tuyển (không quá 20).
Mỗi GV được viết trên 4 dòng gồm:
Tên GV (xâu ký tự độ dài không quá 50)
Mã xét tuyển
Điểm tin học (số thực trong phạm vi 0 đến 10)
Điểm chuyên môn (số thực trong phạm vi 0 đến 10)

Output
Ghi ra danh sách đã sắp xếp. Thông tin mỗi GV gồm: Mã GV, Tên, Môn học, Tổng điểm (1 chữ số phần thập phân), Kết quả. Mỗi thông tin cách nhau một khoảng trống.

3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
"""
class GV:
    def __init__(self,stt,ten,ma,diem):
        self.stt = f'GV{stt:02d}'
        self.ten = ten
        self.ma = ma
        self.diem = diem
    def mon(self):
        if self.ma[0] == 'A':
            return 'TOAN'
        elif self.ma[0] == 'B':
            return 'LY'
        else:
            return 'HOA'
    def tong(self):
        if self.ma[1] == '1':
            return self.diem + 2
        elif self.ma[1] == '2':
            return self.diem + 1.5
        elif self.ma[1] == '3':
            return self.diem + 1
        else:
            return self.diem
    def xep(self):
        if self.tong() >= 18:
            return 'TRUNG TUYEN'
        else:
            return 'LOAI'

    def toStr(self):
        return f'{self.stt} {self.ten} {self.mon()} {self.tong()} {self.xep()}'

n = int(input())
ds = []

for i in range(1,n + 1):
    ten = input().strip()
    ma = input().strip()
    tin = float(input())
    chuyen = float(input())
    diem = tin * 2 + chuyen
    ds.append(GV(i,ten,ma,diem))
ds.sort(key=lambda x: -x.tong())
for i in ds:
    print(i.toStr())
