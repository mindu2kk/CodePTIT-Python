"""
Số cuộn của số tự nhiên x là số S(x) = H(x) mod 9, trong đó H(x) là tổng các chữ số của x, mod  là phép chia dư.
Cho số tự nhiên x có tối đa 200 chữ số. Hãy cộng thêm cho x một giá trị nhỏ nhất k để x+k là bội số của 9.
Giá trị x+k là bao nhiêu?

Input gồm nhiều dòng, mỗi dòng một số x, kết thúc là -1.

Kết quả hiển thị trên màn hình.
"""

while True:
    s = input()
    if s == "-1":
        break
    s = int(s)
    if s % 9 != 0:
        print((int(s // 9) + 1) * 9)
    else:
        print(s)