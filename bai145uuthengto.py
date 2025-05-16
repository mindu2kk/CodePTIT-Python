"""
Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:
Số chữ số của nó là một số nguyên tố
Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

3
1234567
22334455667
23400300489898989
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
    cnt = 0
    for i in range(len(n)):
        if nto(int(n[i])):
            cnt += 1
    if nto(len(n)) and cnt > len(n) - cnt:
        print("YES")
    else:
        print("NO")