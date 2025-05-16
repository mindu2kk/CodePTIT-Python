"""
Số nguyên dương N được gọi là phản nguyên tố nếu như số lượng ước số của N lớn hơn số lượng ước số của tất cả các số nguyên dương nhỏ hơn N.

Ví dụ các số phản nguyên tố đầu tiên: 1, 2, 4, 6, 12, 24, …

Cho số nguyên dương X, hãy tìm số phản nguyên tố bé nhất không nhỏ hơn X.

Input:
Dòng đầu ghi số bộ test T (không quá 106)
Mỗi test ghi số nguyên dương X (1 ≤ X ≤ 107)

Output:
Với mỗi test, ghi ra kết quả tính được trên một dòng.
"""
import bisect

# Tạo danh sách lưu số phản nguyên tố
hcn_list = []
max_div = 0

# Mảng để lưu số ước của từng số từ 1 đến 10^7
divisors = [0] * (10**7 + 1)

# Tính số ước của mỗi số từ 1 đến 10^7
for i in range(1, 10**7 + 1):
    for j in range(i, 10**7 + 1, i):
        divisors[j] += 1

# Xây dựng danh sách số phản nguyên tố
for n in range(1, 10**7 + 1):
    if divisors[n] > max_div:
        hcn_list.append(n)
        max_div = divisors[n]

# Xử lý test case
t = int(input())
for _ in range(t):
    x = int(input())
    print(hcn_list[bisect.bisect_left(hcn_list, x)])
