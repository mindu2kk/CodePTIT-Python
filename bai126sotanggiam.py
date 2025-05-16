"""
Một số nguyên dương được gọi là số tăng giảm nếu thỏa mãn các điều kiện:
Có từ 3 chữ số trở lên
Tìm ra một vị trí trong dãy chữ số sao cho từ bên trái đến vị trí đó thỏa mãn thứ tự tăng dần (tăng chặt)
còn từ vị trí đó đến hết thì thỏa mãn thứ tự giảm dần (giảm chặt).
Viết chương trình kiểm tra một số có phải số tăng giảm hay không.

Input
Dòng đầu ghi số bộ test. Mỗi bộ test viết trên một dòng số nguyên dương N không quá 18 chữ số

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
3
12342
23342
5678961
"""
def check(s):
    n = len(s)
    if n < 3:
        return "NO"
    for i in range(0,n - 1):
        if all(s[j] < s[j + 1] for j in range(i)) and all(s[j] > s[j + 1] for j in range (i,n - 1)):
            return "YES"
    return "NO"
t = int(input())
for _ in range(t):
    s = input()
    print(check(s))