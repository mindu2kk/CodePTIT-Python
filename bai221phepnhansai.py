"""
Một người không hiểu thuật toán nhân nên đã thực hiện phép nhân xy như sau.
Người đó lấy  từng chữ số của số nhân y, nhân với số bị nhân x rồi ghi
thành từng dòng thẳng cột với nhau.
Tổng các dòng khi đó sẽ là z. Biết y và z, liệu bạn có thể khôi phục phép nhân đúng?

Input: mỗi dòng 2 số y và z, kết thúc -1.
Output: x
Giới hạn: 0 £ y, z £ 5000000
"""
def sum_digit(x):
    return sum(int(c) for c in str(x))

while True:
    s = input()
    if s == "-1":
        break
    y,z = map(int,s.split())
    print(int(z / sum_digit(y)))

