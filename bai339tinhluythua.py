def power_modulo(a, b, m):
  """Tính a^b modulo m sử dụng thuật toán mũ nhị phân."""
  res = 1
  a %= m
  while b > 0:
    if b % 2 == 1:
      res = (res * a) % m
    a = (a * a) % m
    b //= 2
  return res

def solve():
  t = int(input())
  for _ in range(t):
    a, b, c, d, m = map(int, input().split())
    result = power_modulo(a, b, m)
    result = power_modulo(result, power_modulo(c, d, m - 1), m)  # Sử dụng định lý Euler
    print(result)

solve()