"""
Cho một dãy số a1 ... an. Một nghịch thế là một cặp số u, v sao cho u < v và au > av. Nhiệm vụ của bạn là đếm số nghịch thế.

Input:
Dòng đầu tiên chứa 2 số nguyên n (2 ≤ n ≤ 105)
Dòng tiếp theo chứa n số nguyên của mảng a (-109 ≤ ai ≤ 109)

Output:
In ra một số nguyên duy nhất là số cặp nghịch thế tìm được.
"""

def merge_and_count(arr, temp, left, mid, right):
    """Hàm merge và đếm số cặp nghịch thế"""
    i, j, k = left, mid + 1, left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:  # Nếu không có nghịch thế
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)  # Đếm số lượng nghịch thế
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count


def merge_sort_and_count(arr, temp, left, right):
    """Hàm chia để trị để đếm số cặp nghịch thế"""
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = 0
    inv_count += merge_sort_and_count(arr, temp, left, mid)
    inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
    inv_count += merge_and_count(arr, temp, left, mid, right)

    return inv_count


def count_inversions(arr):
    """Hàm chính để đếm số cặp nghịch thế"""
    n = len(arr)
    temp = [0] * n
    return merge_sort_and_count(arr, temp, 0, n - 1)

n = int(input())
A =list(map(int,input().split()))
print(count_inversions(A))