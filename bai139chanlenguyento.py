"""
Cho một số nguyên dương không quá 500 chữ số.
Hãy kiểm tra xem số đó có thỏa mãn đồng thời ba tính chất sau hay không?
Vị trí chẵn là chữ số chẵn
Vị trí lẻ là chữ số lẻ
Tổng chữ số là một số nguyên tố.

Input
Dòng đầu ghi số bộ test (không quá 10)
Mỗi bộ test ghi trên một dòng giá trị số nguyên (không quá 500 chữ số)

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

2
2345678521
1212121212121212121212121
"""
def check(n):
    for i in range(len(n)):
        if int(n[i]) % 2 != 0 and i % 2 == 0:
            return False
        elif int(n[i]) % 2 == 0 and i % 2 != 0:
            return False
    return True
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = input()
    if check(n) and checknto(sum(int(i) for i in n)):
        print("YES")
    else:
        print("NO")

