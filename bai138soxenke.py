"""
Một số được gọi là xen kẽ nếu thỏa mãn cả ba tính chất sau:
Số chữ số là số lẻ
Chữ số đầu tiên khác chữ số thứ hai.
Các số ở vị trí đầu tiên, vị trí thứ 3, vị trí thứ 5…  và vị trí cuối cùng có giá trị bằng nhau
Viết chương trình kiểm tra một số có phải xen kẽ hay không.

Input
Dòng đầu ghi số bộ test (không quá 10).
Mỗi bộ test viết trên một dòng số cần kiểm tra, không quá 500 chữ số.

Output
Với mỗi bộ test viết ra YES hoặc NO tùy thuộc kết quả kiểm tra

2324272921262
"""
def test(n):
    l = len(n)
    if l % 2 == 0:
        return "NO"
    first_digit = n[0]
    for d in range(2,l,2):
        if n[d] != first_digit:
            return "NO"
    if first_digit != n[-1]:
        return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = input()
    print(test(n))