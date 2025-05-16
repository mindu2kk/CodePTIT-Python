"""

"""

class Rectangle:
    def __init__(self,d,r,m):
        self.d = d
        self.r = r
        self.m = m
    def chuvi(self):
        return 2 * (self.d + self.r)
    def dt(self):
        return self.d * self.r
    def col(self):
        return self.m[0].upper() + self.m[1:].lower()
arr = input().split()

if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.chuvi(),r.dt(),r.col()))
else:
    print('INVALID')