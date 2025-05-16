"""
Lớp học phần môn XYZ của trường ABC có không quá 100 sinh viên. Danh sách sinh viên gồm các thông tin: mã sinh viên, họ tên, lớp. Môn học có 10 buổi. Dữ liệu điểm danh với mỗi sinh viên được cho bởi một xâu ký tự gồm 10 ký tự trong đó: x là có mặt, m là đến muộn, v là vắng.
Với điểm chuyên cần tối đa là 10. Giả sử mỗi buổi vắng bị trừ 2 điểm, mỗi buổi đến muộn bị trừ 1 điểm. Hãy tính điểm chuyên cần cho mỗi sinh viên (tất nhiên nếu tính ra điểm âm thì ghi vào bảng điểm vẫn là 0).
Nếu điểm bằng 0 thì in thêm ghi chú KDDK (tức là không đủ điều kiện dự thi hết môn).

Input
Dòng đầu ghi số n là số sinh viên. Mỗi sinh viên ghi trên 3 dòng lần lượt là mã sinh viên, họ tên, lớp.
Tiếp theo là n dòng ghi dữ liệu điểm danh. Mỗi dòng gồm mã sinh viên, sau đó là một khoảng trống rồi đến xâu ký tự điểm danh có đúng 10 chữ cái.

Output
Ghi ra danh sách điểm chuyên cần (theo đúng thứ tự ban đầu) gồm các thông tin:
Mã sinh viên
Họ và tên
Lớp
Điểm chuyên cần
Ghi chú (nếu có)
Mỗi thông tin cách nhau một khoảng trống.

3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
"""
class HS:
    def __init__(self,ID,ten,lop):
        self.ID = ID
        self.ten = ten
        self.lop = lop
        self.diem = 10
    def tinh(self,s):
        for i in s:
            if i == 'm':
                self.diem -= 1
            elif i == 'v':
                self.diem -= 2
        if self.diem < 0:
            self.diem = 0

    def toStr(self):
        print(self.ID + " " + self.ten + " " + self.lop + " " + str(self.diem),end = '')
        if self.diem == 0:
            print(" KDDK",end = '')
        print()


n = int(input())
ds = []
m = {}

for i in range(1,n + 1):
    ma = input()
    ten = input()
    lop = input()
    tmp = HS(ma,ten,lop)
    m[tmp.ID] = tmp
    ds.append(tmp)
for i in range(1,n + 1):
    ma1,xau = map(str,input().split())
    m[ma1].tinh(xau)
for i in ds:
    i.toStr()