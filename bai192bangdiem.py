"""
Trường THCS XYZ lập bảng điểm tổng kết cho học sinh. Có 10 môn học lần lượt gồm: Toán, Tiếng Việt, Ngoại ngữ, Vật lý, Hóa học, Sinh học, Lịch Sử, Địa, Giáo dục công dân và môn Công nghệ. Trong đó môn Toán và Tiếng Việt tính hệ số 2, các môn còn lại hệ số 1.
Học sinh được xếp hạng theo điểm trung bình:
Từ 9 trở lên: loại XUAT SAC
Từ 8 đến 8.9: loại GIOI
Từ 7 đến 7.9: loại KHA
Từ 5 đến 6.9: loại TB
Dưới 5: loai YEU
Hãy lập bảng điểm tổng kết và sắp xếp theo điểm trung bình giảm dần.

Input
Dòng đầu ghi số học sinh (không quá 50).
Thông tin về mỗi học sinh có hai dòng: dòng đầu là họ tên (độ dài không quá 50), dòng thứ 2 gồm 10 số thực trong đoạn [0..10] lần lượt là điểm 10 môn theo đúng thứ tự đã mô tả.

Output
Danh sách đã sắp xếp được ghi ra bao gồm các thông tin:
Mã học sinh (tự động gán tăng dần theo thứ tự nhập, bắt đầu là HS01)
Họ và tên
Điểm trung bình (với 1 chữ số phần thập phân)
Xếp loại
Trong trường hợp điểm trung bình bằng nhau thì học sinh nào có mã học sinh nhỏ hơn sẽ xếp trên.

3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
"""
class HocSinh:
    def __init__(self, stt, ten, diem):
        self.stt = f'HS{stt:02d}'
        self.ten = ten
        self.diem = diem
    def xeploai(self):
        if self.diem >= 9:
            return "XUAT SAC"
        elif self.diem >= 8:
            return "GIOI"
        elif self.diem >= 7:
            return "KHA"
        elif self.diem >= 5:
            return "TB"
        else:
            return "YEU"
    def xep(self, other):
        return self.diem < other.diem

    def toStr(self):
        return f"{self.stt} {self.ten} {self.diem:.1f} {self.xeploai()}"


n = int(input())
ds = []
for i in range(1,n + 1):
    ten = input()
    A = list(map(float,input().split()))
    diem = (A[0] * 2 + A[1] * 2 + sum(A[2:])) / 10 / 1.2
    ds.append(HocSinh(i,ten,diem))

ds.sort(key = lambda x : (-x.diem,x.stt))

for hs in ds:
    print(hs.toStr())

