"""
Cho số nguyên dương N có không quá 500 chữ số.
Hãy kiểm tra xem 4 chữ số cuối cùng ghép lại có tạo thành một số nguyên tố hay không.
Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test viết trên một dòng số nguyên dương N, không quá 500 chữ số.

Output
Với mỗi bộ test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

3
12234323130097
3443354654654654461123
43543543434554659999
"""

def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    if nto(int(str(n)[-4:])):
        print("YES")
    else:
        print("NO")
