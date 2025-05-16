"""
Cho số nguyên dương N có ít nhất 4 chữ số và không quá 500 chữ số.
Một số được gọi là số đầu cuối nguyên tố nếu thỏa mãn cả hai điều kiện:
Ba chữ số đầu ghép lại được một số nguyên tố
Ba chữ số cuối ghép lại được một số nguyên tố
Viết chương trình kiểm tra xem N có phải là đầu cuối nguyên tố hay không?

Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi bộ test viết trên một dòng số N, ít nhất 4 chữ số và không quá 500 chữ số.

Output
Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

3
12743
7337
12345678901234
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
    n = input()
    if nto(int(n[-3:])) and nto(int(n[:3])):
        print("YES")
    else:
        print("NO")