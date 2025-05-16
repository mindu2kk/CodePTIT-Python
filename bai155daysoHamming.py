"""
Dãy số nguyên dương tăng dần trong đó ước số nguyên tố lớn nhất của các số trong dãy đều không vượt quá 5 được gọi là dãy số Hamming.
Ví dụ 10 = 2x5 thuộc dãy Hamming còn 26 = 2x13 không thuộc dãy Hamming.
Số 1 được coi là số đầu tiên của dãy Hamming.
Cho số nguyên dương N.  Hãy xác định xem N có thuộc dãy Hamming hay không và nếu có thì thứ tự của N trong dãy Hamming là bao nhiêu.

Input:
Dòng đầu tiên ghi số bộ test (không quá 105).
Mỗi test ghi một số N (1 ≤ N ≤ 1018).

Output:
Nếu giá trị N thuộc dãy Hamming thì ghi ra thứ tự của N (tính từ 1).
Nếu không thì ghi ra “Not in sequence”

11
1
2
6
7
8
9
10
11
12
13
14
"""
m = {1:1}

while True:
    a = []
    check = 1
    for i in m:
        if i < 10 ** 18:
            if not((i * 2) in m):
                a.append(i * 2)
            if not((i * 3) in m):
                a.append(i * 3)
            if not((i * 5) in m):
                a.append(i * 5)
    for i in a:
        check = 0
        m[i] = 1
    if check == 1:
        break
a = sorted(list(m))
dem = 1
for i in a:
    m[i] = dem
    dem += 1
t = int(input())

for _ in range(t):
    n = int(input())
    if n in m:
        print(m[n])
    else:
        print("Not in sequence")