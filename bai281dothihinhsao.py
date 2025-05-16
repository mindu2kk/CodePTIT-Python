"""
Một đơn đồ thị vô hướng được gọi là Hình Sao nếu có một đỉnh có thể nối đến tất cả các đỉnh còn lại, còn các đỉnh khác thì không có cạnh nối với nhau.

Cho mô tả một đơn đồ thị vô hướng N đỉnh với đúng N-1 cạnh. Hãy kiểm tra xem đồ thị đó có phải dạng Hình Sao hay không.

Dữ liệu vào

Dòng đầu tiên ghi số N là số đỉnh của đồ thị (1 ≤ N ≤ 105).
N-1 dòng tiếp theo, mỗi dòng ghi ra một cặp (u,v) là cạnh của đồ thị. Dữ liệu đảm bảo u ≠ v.

Kết quả
Ghi ra trên một dòng chữ “Yes” nếu đồ thị là Hình Sao; chữ “No” trong trường hợp ngược lại.
5
1 2
1 3
1 4
1 5
"""

def test(n,canh):
    if n == 1:
        return "Yes"
    degree = [0] * (n + 1)

    for u,v in canh:
        degree[u] += 1
        degree[v] += 1
    center = max(range(1,n + 1), key = lambda x:degree[x])

    if degree[center] == n - 1 and degree.count(1) == n - 1:
        return "Yes"
    return "No"

n = int(input())
canh = [tuple(map(int,input().split())) for _ in range(n - 1)]
print(test(n,canh))