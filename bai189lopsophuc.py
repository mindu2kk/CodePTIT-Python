"""
Khai báo lớp Số phức với hai thuộc tính là phần thực và phần ảo.
Viết chương trình thực hiện nhập hai số phức A, B và thực hiện các thao tác tính toán trên số phức
C = (A + B) x A
D = (A + B)2

Input:
Dòng đầu tiên là số bộ test T (T <= 100)
T dòng tiếp theo mỗi dòng gồm 4 số lần lượt là a, b, c, d, với -102 < a, b, c, d < 102.

Output:
Kết quả của hai phép tính theo định dạng trong ví dụ

3
1 2 3 4
2 3 4 5
1 -2 5 -6
"""
class SoPhuc:
    def __init__(self,thuc,ao):
        self.thuc = thuc
        self.ao = ao

    def __add__(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)

    def __mul__(self, other):
        return SoPhuc(self.thuc * other.thuc - self.ao * other.ao,self.thuc * other.ao + self.ao * other.thuc)

    def __str__(self):
        if self.ao < 0:
            return '{} - {}i'.format(self.thuc,abs(self.ao))
        return '{} + {}i'.format(self.thuc,self.ao)
t = int(input())

for _ in range(t):
    a,b,c,d = map(int,input().split())
    A = SoPhuc(a,b)
    B = SoPhuc(c,d)
    C = (A + B) * A
    D = (A + B) * (A + B)
    print(f"{C}, {D}")
