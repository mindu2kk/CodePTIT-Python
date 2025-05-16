"""
Mỗi team thi lập trình ICPC có 3 sinh viên đến từ cùng một trường đại học.
Thông tin về một team gồm:
Mã team (tự động tăng, tính từ Team01)
Tên team: không quá 50 ký tự
Tên trường: không quá 150 ký tự
Thông tin mỗi thí sinh gồm:
Mã thí sinh (tự động tăng, tính từ C001)
Họ và tên: không quá 50 ký tự.
Mã team
Hãy nhập và in ra danh sách thí sinh thi lập trình được sắp xếp theo họ tên (thứ tự từ điển).

Input
Dòng đầu ghi số team. Mỗi team ghi trên 2 dòng gồm tên team và tên trường.
Tiếp theo là một dòng ghi số thí sinh. Mỗi thí sinh ghi trên 2 dòng gồm họ tên và mã team.

Output
Ghi ra danh sách đã sắp xếp theo họ tên thí sinh (thứ tự từ điển) gồm các thông tin:
Mã thí sinh
Họ và tên thí sinh
Tên team
Tên trường

2
BAV_MIS
Banking Academy of Vietnam
FTU Knights1
Foreign Trade University
6
Le Trung Toan
Team01
Nguyen Trinh Quoc Long
Team01
Giang Minh Tung
Team01
Nguyen Hang Giang
Team02
Nguyen Thanh Nhan
Team02
Nguyen Viet Duc
Team02
"""
class TS:
    def __init__(self,stt,ten,nhom_ten,trg):
        self.stt = f'C{stt:03d}'
        self.ten = ten
        self.nhom_ten = nhom_ten
        self.trg = trg

    def toStr(self):
        return f"{self.stt} {self.ten} {self.nhom_ten} {self.trg}"

n = int(input())
ds = []
team = {}
for i in range(1,n + 1):
    nhom_ten = input()
    trg = input()
    so_nhom = f'Team{i:02d}'
    team[so_nhom] = (nhom_ten,trg)

m = int(input())
for i in range(1,m + 1):
    ten = input()
    so_nhom = input()
    nhom_ten,trg = team[so_nhom]

    ds.append(TS(i,ten,nhom_ten,trg))
ds.sort(key=lambda x:x.ten)

for i in ds:
    print(i.toStr())