"""
Cho dãy số A có 10 phần tử là các số nguyên dương. Hãy đếm xem sẽ có bao nhiêu số khác nhau trong dãy nếu tất cả
các phần tử đều được chia dư cho 42.
Input
Gồm 10 số nguyên dương, viết trên một hoặc nhiều dòng.

Output
Ghi ra các số khác nhau tìm được sau khi đã chia dư cho 42.
39 40 41 42 43 44 82
83 84 85
"""

# 1 cách mới để đọc input từ nhiều dòng

x = 0
b = set()

while True:
    a = [int(x) for x in input().split()]
    x += len(a)

    for i in range(len(a)):
        b.add(a[i] % 42)
    if x == 10:
        break
print(len(b))