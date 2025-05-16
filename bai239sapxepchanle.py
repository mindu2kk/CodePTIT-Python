"""
Cho dãy số A[] có n phần tử. Hãy sắp xếp các số chẵn trong dãy theo thứ tự tăng dần và các số lẻ theo thứ tự giảm dần.
In ra dãy kết quả đã sắp xếp trong đó vị trí số chẵn và vị trí số lẻ không thay đổi so với dãy ban đầu.

Input
Dòng đầu ghi số n (1 < n ≤ 1000)
Các dòng tiếp theo ghi đủ n số của dãy A[], các số đều nguyên dương và không quá 1000.

Output
Ghi ra dãy kết quả đã sắp xếp trong đó các vị trí của số chẵn và số lẻ không thay đổi.

10
1 2 3 4 5 6 7 7 9 6
"""
def custom_sort(n, A):
    even_numbers = sorted([x for x in A if x % 2 == 0])  # Chẵn tăng dần
    odd_numbers = sorted([x for x in A if x % 2 == 1], reverse=True)  # Lẻ giảm dần

    even_index = 0
    odd_index = 0

    result = []
    for num in A:
        if num % 2 == 0:
            result.append(even_numbers[even_index])
            even_index += 1
        else:
            result.append(odd_numbers[odd_index])
            odd_index += 1

    print(*result)

# Nhập số phần tử n
n = int(input())

A = []
while len(A) < n:
    i = [int(x) for x in input().split()]
    A += i

custom_sort(n, A)
