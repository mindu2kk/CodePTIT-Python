"""
Một số nguyên dương được gọi là đẹp nếu số đó chỉ có hai chữ số khác nhau và các chữ số ở cách nhau 2 vị trí đều bằng nhau. Ví dụ: 121, 1313131, 5656 …
Viết chương trình kiểm tra một số có phải số đẹp hay không?

Input
Dòng đầu ghi số bộ test.
Mỗi bộ test ghi một số nguyên dương N (lớn hơn 10 và có không quá 18 chữ số) trên một dòng.
Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

3
12121212
343433
78789989
"""
def test(n):
    for i in range(2,len(n)):
        if n[i] != n[i - 2] or n[i - 2] == n[i - 1]:
            return "NO"
    return "YES"
t = int(input())

for _ in range(t):
    n = input()
    print(test(n))