t = int(input())
while t > 0:
    n = int(input())
    ok = True
    while n != 0:
        x = n % 10
        n //= 10
        if x != 4 and x != 7:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1