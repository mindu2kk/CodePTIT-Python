"""
Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.
Một số được coi là thuận nghịch nếu có từ 2 chữ số trở lên và nếu viết theo thứ tự ngược lại giá trị vẫn không thay đổi so với giá trị ban đầu. Ví dụ: 99, 121, 1331
Hãy tìm số thuận nghịch lớn nhất trong ma trận và các vị trí có giá trị bằng số thuận nghịch lớn nhất đó.

Input
Dòng đầu ghi hai số N và M (1 < N, M < 50)
Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 10000.

Output
Ghi ra giá trị của số thuận nghịch lớn nhất. Sau đó lần lượt là các vị trí của số thuận nghịch lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.
Nếu không tìm thấy số thuận nghịch nào thì ghi ra NOT FOUND

6 4
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 12221
"""

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
def dx(n):
    return str(n) == str(n)[::-1]

maxx = -1
maxx_posi = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] > maxx and dx(matrix[i][j]):
            maxx = matrix[i][j]
            maxx_posi = [(i,j)]
        elif matrix[i][j] == maxx and dx(matrix[i][j]):
            maxx_posi.append((i,j))

if maxx == 0:
    print("NOT FOUND")
else:
    print(maxx)
    for x,y in maxx_posi:
        print(f"Vi tri [{x}][{y}]")


