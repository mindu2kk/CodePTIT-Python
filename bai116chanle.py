"""
Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?

Tổng chữ số của N chia hết cho 10
Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị
Input

Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.

Output

Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
"""
# Check sum % 10 == 0
def tong(s):
    return sum(int(digit) for digit in str(s))

# Check s[i] - s[i -1] == 2
def check(s):
    n = len(s)
    for i in range(1,n - 1):
        if abs(ord(s[i]) - ord(s[i-1])) != 2:
            return False
    return True

def test(s):
    if tong(s) % 10 == 0 and check(s):
        print("YES")
    else:
        print("NO")
t = int(input())

for _ in range(t):
    s = input()
    test(s)

