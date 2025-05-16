"""
Tình hình chiến sự ở vùng biển Z đang trở nên cực kì cam go. Nhà vua quyết định gửi thêm quân chi viên tới chiến trường.  Trong tay nhà vua đang có quyền triệu tập k đội quân từ khắp mọi miền đất nước. Để tập trung binh lực tốt nhất, nhà vua đã triệu tập cả k đội quân đến kinh thành rồi sau đó mới di chuyển đến chiến trường. Do số lượng đoàn quân khá lớn, nhà vua quyết định để 1 đại tướng đi thuê xe để chở quân lính. Vì tình đoàn kết, tất cả các chiến sĩ từ k quân đoàn tuyên bố: Nếu di chuyển, họ muốn được di chuyển cùng tất cả các đồng đội của mình trên một xe và trên xe đó không được có tới 3 quân đoàn khác nhau vì như vậy rất dễ xảy ra xô xát. Đến đây , tướng quân rất đau đầu trong việc chọn lựa loại xe đưa các đội quân đi vì nhà vua muốn chi phí di chuyển là ít nhất. Chi phí di chuyển sẽ bằng số lượng xe thuê nhân với sức chứa của loại xe.  Hãy giúp tướng quân tính toán ra chi phí nhỏ nhất để thuê xe mà thỏa mãn yêu cầu của tất cả quân lính nhé

Input:

Dòng đầu tiên gồm số n và k (1 ≤ n ≤ 5.105, 1 ≤ k ≤ 10000). Với n là số lượng quân lính, k là số lượng các quân đoàn. Giả sử các quân đoàn đánh số từ 1 đến k.

Dòng thứ 2 gồm n số nguyên a[i] (1 ≤ a[i] ≤ k) trong đó a[i] là số hiệu quân đoàn của người lính thứ i.

Output:

Ghi ra chi phí nhỏ nhất.
"""


def calculate_min_cost(n, k, a):
    from collections import Counter

    # Đếm số lượng lính mỗi quân đoàn
    counter = Counter(a)
    groups = list(counter.values())

    # Khởi tạo kết quả
    min_cost = float('inf')

    # Thử với các sức chứa xe khác nhau
    for capacity in range(1, n + 1):
        cost = 0
        for group in groups:
            # Tính số xe cần thiết cho mỗi nhóm
            cost += (group + capacity - 1) // capacity

        # Cập nhật chi phí nhỏ nhất
        min_cost = min(min_cost, cost * capacity)

    return min_cost


# Nhập dữ liệu ví dụ
n,k = map(int,input().split())
a = list(map(int,input().split()))
print(calculate_min_cost(n, k, a))
