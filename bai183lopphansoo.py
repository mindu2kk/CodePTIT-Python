import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        GCD = math.gcd(self.tu, self.mau)
        self.tu //= GCD
        self.mau //= GCD
        return '{}/{}'.format(self.tu, self.mau)

tu,mau = map(int,input().split())
A = PhanSo(tu,mau)
print(A.rutgon())
