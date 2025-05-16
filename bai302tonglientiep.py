"""
Một số số nguyên dương có thể được biểu diễn thành tổng của các số nguyên dương liên tiếp.
Ví dụ: 6 = 1 +2 + 3 hoặc 9 = 4 + 5 hoặc 9 = 2 + 3 + 4
Cho số nguyên dương N không quá 9 chữ số. Hãy đếm xem có bao nhiêu cách biểu diễn N thành tổng các số nguyên dương liên tiếp.

Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi một số nguyên dương N, không quá 9 chữ số.

Output
Ghi ra số cách tìm được.

3
6
8
9
"""
def count_consecutive_sums(N):
    count = 0
    k = 2
    while k * (k - 1) // 2 < N:
        if (N - k * (k - 1) // 2) % k == 0:
            count += 1
        k += 1
    return count

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(count_consecutive_sums(N))


