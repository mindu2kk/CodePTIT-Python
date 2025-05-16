"""
Với mỗi số nguyên dương N, số M được coi là số đặc biệt của N nếu M được tạo ra bằng tổng các lũy thừa không âm khác nhau của N. Ví dụ N = 4 thì M = 17 là số đặc biệt vì 17 = 40 + 42.
Viết chương trình nhập số N và số K. Sau đó in ra số đặc biệt thứ K của N nếu sắp xếp các số đặc biệt của N theo thứ tự tăng dần.
Kết quả có thể rất lớn, hãy in ra theo modulo 109 + 7.

Input
Dòng đầu tiên chứa một số nguyên duy nhất t (1 ≤ t ≤ 104) - số lượng bộ test.
Dòng tiếp theo chứa hai số nguyên N và K (2 ≤ N ≤ 109; 1 ≤ k ≤ 109).

Output
Với mỗi bộ test, ghi ra số đặc biệt thứ K của N theo modulo 109 + 7

3
3 4
2 12
105 564
"""

MOD = 10**9 + 7

def test(n,k):
    res = 0
    power = 1

    while k > 0:
        if k % 2 == 1:
            res = (res + power) % MOD
        power = (power * n) % MOD
        k //= 2
    return res

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    print(test(n,k))