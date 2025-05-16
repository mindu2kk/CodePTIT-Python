n = int(input())
mon = []
for _ in range(n):
    tenmon = input().strip()
    c = input().strip()
    t = input().strip()
    mon.append((tenmon,c,t))
mon.sort(key = lambda x:(x[0]))

for st in mon:
    print(*st)

"""
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
"""