"""
Cho ma trận A kích thước N*M.
Hãy tìm số bước đi ít nhất để di chuyển từ vị trí A[1][1] đến vị trí A[N][M].
Biết rằng mỗi bước từ vị trí (i, j) ta có thể di chuyển theo một trong ba hướng:
Hướng xuống dưới với số ô di chuyển là hiệu hai giá trị A[i][j] và A[i+1][j]
Hướng sang phải với số ô di chuyển là hiệu hai giá trị A[i][j] và A[i][j+1]
Hướng chéo xuống với số ô di chuyển là hiệu của hai giá trị A[i][j] và A[i+1][j+1]

Input:
Dòng đầu tiên đưa vào số lượng test T.
Dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm hai phần: phần thứ nhất là hai số N, M; phần thứ hai là các phần tử của ma trận A[][]; các số được viết cách nhau một vài khoảng trống.
T, N, M, A[i][j] thỏa mãn ràng buộc: 1≤T≤100; 1≤ N, M, A[i][j]≤103.

Output:
Đưa ra kết quả mỗi test theo từng dòng.
Nếu không tìm được đường đi ghi ra -1
"""

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(i) for i in input().split()])

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = a[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + a[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + a[0][j]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(abs(dp[i - 1][j] - a[i][j]), abs(dp[i - 1][j - 1] - a[i][j]), abs(dp[i][j - 1] - a[i][j]))

    print(dp[n - 1][m - 1])