"""
Khai báo lớp Matrix mô tả ma trận các số nguyên với các thuộc tính là kích thước ma trận và mảng hai chiều lưu các phần tử.
Nhập ma trận a cấp n*m. Hãy viết chương trình tính tích của a với ma trận chuyển vị của a.

Input: Dòng đầu tiên ghi số bộ test.
Với mỗi bộ test:
Dòng đầu tiên ghi hai số n và m là bậc của ma trân a;
n dòng tiếp theo, mỗi dòng ghi m  số của một dòng trong ma trận. n và m đều nguyên dương và nhỏ hơn 50. Các giá trị trong ma trận không vượt quá 100.

Output: Với mỗi bộ test ghi ra ma trận tích tương ứng, mỗi số cách nhau đúng một khoảng trống.

1
2 2
1 2
3 4
"""
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    elements = []
    while len(elements) < n * m:
        elements.extend(map(int, input().split()))

    matrix = [elements[i * m:(i + 1) * m] for i in range(n)]
    cv = [[matrix[i][j] for i in range(n)] for j in range(m)]
    res = [[sum(matrix[i][k] * cv[k][j] for k in range(m)) for j in range(n)] for i in range(n)]

    for row in res:
        print(*row)
