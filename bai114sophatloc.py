for t in range(int(input())):
    a = input()
    b = [int(i) for i in a]
    if a[len(a) - 2] != "8" or a[len(a)- 1] != "6":
        print("NO")
    else:
        print("YES")