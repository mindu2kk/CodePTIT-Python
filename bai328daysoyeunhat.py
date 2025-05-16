def min_weakness(N, A):
    from statistics import median

    X = median(A)

    adjusted_A = [a - X for a in A]

    # Hàm tính tổng con lớn nhất và nhỏ nhất (Kadane's Algorithm)
    def max_absolute_subarray(arr):
        max_sum = cur_max_sum = arr[0]
        min_sum = cur_min_sum = arr[0]

        for num in arr[1:]:
            cur_max_sum = max(num, cur_max_sum + num)
            cur_min_sum = min(num, cur_min_sum + num)
            max_sum = max(max_sum, cur_max_sum)
            min_sum = min(min_sum, cur_min_sum)

        return max(abs(max_sum), abs(min_sum))

    return f"{max_absolute_subarray(adjusted_A):.6f}"

from sys import stdin
N = int(stdin.readline())
A = [i for i in map(float, stdin.readline().split())]

# Xuất kết quả
print(min_weakness(N, A))
