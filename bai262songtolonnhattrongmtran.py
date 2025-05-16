"""
Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.
Hãy tìm số nguyên tố lớn nhất trong ma trận và các vị trí có giá trị bằng số nguyên tố lớn nhất đó.

Input
Dòng đầu ghi hai số N và M (1 < N, M < 50)
Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 1000.

Output
Ghi ra giá trị của số nguyên tố lớn nhất. Sau đó lần lượt là các vị trí của số nguyên tố lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.
Nếu không tìm thấy số nguyên tố nào thì ghi ra NOT FOUND

6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29
"""

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for i in range(n)]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

max_prime = 0
for i in range(n):
    for j in range(m):
        if is_prime(matrix[i][j]) and matrix[i][j] > max_prime:
            max_prime = matrix[i][j]
            max_prime_positions = [(i, j)]
        elif is_prime(matrix[i][j]) and matrix[i][j] == max_prime:
            max_prime_positions.append((i, j))

if max_prime == 0:
    print("NOT FOUND")
else:
    print(max_prime)
    for i in max_prime_positions:
        print(f"Vi tri [{i[0]}][{i[1]}]")
