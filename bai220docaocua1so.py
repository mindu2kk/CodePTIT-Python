"""
Độ cao của một số tự nhiên là tổng các chữ số của số đó, ký hiệu là H(x).
Viết hàm Count(n, h) cho ra số lượng các số < n, độ cao h.
Ví dụ: Count(20, 7) = 2: Có 2 số nhỏ thua 20, độ cao 7 là 7 và 16 .

Input: mỗi dòng 2 số n và h, kết thúc -1.

Output: Count(n, h)
Giới hạn: 0 £ n £ 1000000, 0 £ h £ 200
"""
def sum_digits(x):
    return sum(int(d) for d in str(x))

while True:
    s = input()
    if s == "-1":
        break
    n, h = map(int, s.split())

    count = sum(1 for x in range(n) if sum_digits(x) == h)

    print(count)
