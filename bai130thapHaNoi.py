"""
Bài toán Tháp Hà Nội đã rất nổi tiểng. Bắt đầu có các đĩa xếp chồng lên cột A theo thứ tự kích thước giảm dần, nhỏ nhất ở trên cùng. Cột B và cột C ban đầu không có đĩa nào cả.

Mục tiêu của bạn là di chuyển toàn bộ các đĩa theo đúng thứ tự về cột C, tuân theo các quy tắc sau:
Mỗi lần chỉ có thể di chuyển một đĩa.
Mỗi lần di chuyển sẽ lấy đĩa trên từ một trong các cột và đặt nó lên trên một cột khác.
Không được đặt đĩa lên trên đĩa nhỏ hơn..

Input:
Số tự nhiên  0 < N < 10

Output:
In ra lần lượt từng bước theo mẫu trong ví dụ. Chú ý giữa các chữ cái và dấu -> có khoảng trống.
"""

def hanoi(n,dau,cuoi,tg):
    if n == 1:
        print(f"{dau} -> {cuoi}")
        return
    hanoi(n -1,dau,tg,cuoi)
    print(f"{dau} -> {cuoi}")
    hanoi(n - 1,tg,cuoi,dau)

n = int(input())

hanoi(n,'A','C','B')