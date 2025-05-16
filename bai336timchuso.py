def find_last_three_digits(n):
    a, b = 2, 6
    for _ in range(n):
        a, b = b, (6 * b - 4 * a) % 1000
    return f"{a - 1:03d}"  # Đảm bảo có đúng 3 chữ số

t = int(input())
for _ in range(t):
    n = int(input())
    print(f"Case #{t}: {find_last_three_digits(n)}")
