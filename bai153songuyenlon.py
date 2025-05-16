"""
Cho hai số a và b trong đó a≤1012, b≤10250. Nhiệm vụ của bạn là tìm ước số chung lớn nhất của hai số a, b.

Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
T dòng tiếp đưa các bộ test. Mỗi bộ test gồm hai dòng: dòng đầu tiên đưa vào số a; dòng tiếp theo đưa vào số b.
Các số T, a, b thỏa mãn ràng buộc: 1≤T≤100; 1≤a≤1012; 1≤b≤10250;

Output:
Đưa ra kết quả mỗi test theo từng dòng.
1
1221
1234567891011121314151617181920212223242526272829
"""
from math import gcd

def test(a,b):
    curr = 0
    for digit in b:
        curr = (curr * 10 + int(digit)) % a
    return curr

def tinh(a,b):
    if a == 0:
        return int(b)
    remain = test(a,b)
    return gcd(a,remain)

t = int(input())

for _ in range(t):
    a = int(input().strip())
    b = input().strip()
    print(tinh(a,b))