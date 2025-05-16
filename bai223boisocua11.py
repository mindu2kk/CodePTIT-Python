"""
Cho số tự nhiên x có tối đa 200 chữ số. Nếu x là bội của 11 thì hiển thị YES; ngược lại, hiển thị NO.
Input gồm nhiều dòng, mỗi dòng một số x, kết thúc là -1.
Kết quả hiển thị trên màn hình.
"""

def chiahet(x):
    chan = 0
    le = 0
    for i,val in enumerate(x):
        if i % 2 == 0:
            chan += int(val)
        else:
            le += int(val)
    if abs(chan - le) % 11 == 0:
        return "YES"
    return "NO"

while True:
    x = input().strip()
    if x == "-1":
        break
    print(chiahet(x))