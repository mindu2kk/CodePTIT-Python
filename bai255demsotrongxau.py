"""
Cho một ký tự S[] chỉ có các chữ số, độ dài không quá 1000, và số nguyên dương N (không quá 9 chữ số). Hãy đếm xem số N xuất hiện bao nhiêu lần trong S[].
Chú ý: các ký tự số không được đếm lặp. Tức là mỗi ký tự chỉ được xét một lần.
Ví dụ: S[] = “1212121112211221121”, N = 121 thì đáp án là 3.

Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi test gồm hai dòng, dòng đầu là xâu ký tự S[], dòng sau là số N.

Output
Với mỗi bộ test, ghi ra kết quả tính được trên một dòng.

2
1212121112211221121
121
2222222222322292
2222
"""

t = int(input())
for _ in range(t):
    s = input()
    n = input()
    l = len(n)
    cnt = 0
    i = 0
    while i <= len(s) - len(n):
        if s[i:i + l] == n:
            cnt += 1
            i += l
        else:
            i += 1
    print(cnt)
