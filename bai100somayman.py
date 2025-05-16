n = int(input())
a = b = 0

while n > 0:
    x = n % 10
    n //= 10
    if x == 4:
        a += 1
    elif x == 7:
        b += 1
if a + b == 4 or a + b == 7:
    print("YES")
else:
    print("NO")
