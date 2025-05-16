t = int(input())
dict = {}
for _ in range(t):
    bien,xe,so,huong,ngay = input().split()
    if huong == "OUT":
        continue
    
    if ngay not in dict:
        dict[ngay] = 0
    if so == "2":
        dict[ngay] += 20000
    elif so == "5":
        dict[ngay] += 10000
    elif so == "7":
        dict[ngay] += 15000
    elif so == "29":
        dict[ngay] += 50000
    else:
        dict[ngay] += 70000
        
for key in dict:
    print(f"{key}: {dict[key]}")
    
