"""
2
0 0 0 5
0 199 5 6
"""
import math
from decimal import Decimal
class Point:
    def __init__(self, x, y):
        self.x = Decimal(x)
        self.y = Decimal(y)

    def distance(self,other=None):
        return "{:.4f}".format(math.sqrt((self.x-other.x) ** 2 + (self.y-other.y) ** 2))

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1