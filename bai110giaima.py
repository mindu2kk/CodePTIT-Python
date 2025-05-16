"""
Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa. Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh nhau giống nhau và viết số lượng phía sau các chữ cái đó.

Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1

Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.

Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng.

Input

Dòng đầu ghi số bộ test. Mỗi bộ test ghi xâu mã hóa.

Output

Với mỗi test ghi ra xâu ký tự ban đầu.
"""
def decode(s):
    res  = ""
    cnt = 0

    while cnt < len(s):
        char = s[cnt]
        cnt += 1
        digit = int(s[cnt])
        res += char * digit
        cnt += 1
    return res

T = int(input())

for _ in range(T):
    s = input()
    print(decode(s))