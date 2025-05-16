"""
Cho một xâu ký tự có thể có các ký tự chữ cái và chữ số. Người ta thực hiện một phép mã hóa đơn giản,
trong đó đếm từ trái qua phải các ký tự giống nhau liên tiếp và viết số đếm trước ký tự đó.

Ví dụ: AACDDPQ được mã hóa thành 2A1C2D1P1Q

           11111147g được mã hóa thành 6114171g

Viết chương trình thực hiện thao tác mã hóa như trên.

Input

Dòng đầu ghi số bộ test. Mỗi dòng sau là một xâu ký tự, độ dài không quá 1000.

Output

Với mỗi bộ test, ghi ra xâu ký tự mã hóa tương ứng.

3
AACDDPQ
11111147g
1111111111
"""
def encode(s):
    res = ""
    i = 1
    cnt = 1
    for i in range(1,len(s)):
        if s[i] == s[i - 1]:
            i += 1
            cnt += 1
        else:
            res += str(cnt) + s[i - 1]
            cnt = 1
    res += str(cnt) + s[-1]
    return res

t = int(input())
for _ in range(t):
    s = input().strip()
    print(encode(s))