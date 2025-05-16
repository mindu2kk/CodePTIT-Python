def solve():
    n = int(input())
    a = list(map(int, input().split()))

    min_steps = float('inf')

    for i in range(n):
        steps = 0
        temp_a = a[:]  # Tạo bản sao của dãy số

        # Tính toán bên trái đỉnh
        for j in range(i - 1, -1, -1):
            target = temp_a[i] - (i - j)
            if temp_a[j] != target:
                steps += abs(temp_a[j] - target)
                temp_a[j] = target

        # Tính toán bên phải đỉnh
        for j in range(i + 1, n):
            target = temp_a[i] - (j - i)
            if temp_a[j] != target:
                steps += abs(temp_a[j] - target)
                temp_a[j] = target

        # Kiểm tra điều kiện tất cả các phần tử lớn hơn 0
        valid = True
        for val in temp_a:
            if val <= 0:
                valid = False
                break

        if valid:
            min_steps = min(min_steps, steps)

    print(min_steps)


solve()