def min_triplet_sum(arr, n):
    # Khởi tạo ba số nhỏ nhất
    min1 = min2 = min3 = float('inf')

    for num in arr:
        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
        elif num < min2:
            min3 = min2
            min2 = num
        elif num < min3:
            min3 = num

    return min1 + min2 + min3


# Đọc số lượng test case
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    print(min_triplet_sum(A, N))


"""
2
7
1 2 3 0 -1 8 10 
7
9 8 20 3 4 -1 0
"""