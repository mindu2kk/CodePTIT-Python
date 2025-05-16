"""

"""
import math


class PhanSo:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        gcd = math.gcd(self.tu,self.mau)
        self.tu //= gcd
        self.mau //= gcd
        return self
    def tinh(self,other):
        mau = self.mau * other.mau
        ans = PhanSo(self.tu * mau // self.mau + other.tu * mau // other.mau,mau)
        return ans.rutgon()

a,b,c,d = map(int,input().split())
A = PhanSo(a,b)
B = PhanSo(c,d)
C = A.tinh(B)
print(str(C.tu) +'/'+ str(C.mau))