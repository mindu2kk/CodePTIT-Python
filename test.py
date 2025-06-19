from itertools import combinations, product
from math import isqrt, gcd


def nto(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def tong(n):
    sum = 0
    while n > 0:
        digit = n % 10
        if nto(digit):
            sum += digit
            n //= 10
        else:
            return False
    return sum

def gt(n):
    return 1 if (n == 0 or n == 1) else n * gt(n - 1)

def lamtron(n):
    factor = 10
    while n > factor:
        remain = n % factor
        n -= remain
        if remain >= factor // 2:
            n += factor
        factor *= 10
    return n

def ntocungnhau(n):
    cnt = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            cnt += 1
    return cnt

def tinhlai(n,m,x):
    cnt = 0
    while n < x:
        n = n * (m / 100 + 1)
        cnt += 1
    return cnt

def demkitu(s):
    t = sum(1 for c in s if c.islower())
    h = len(s) - t
    if t >= h:
        print(s.lower())
    else:
        print(s.upper())

def daucuoi(n):
    if n[:2] == n[-2:]:
        print("YES")
    else:
        print("NO")

def chuachan(n):
    return all(c in '02468' for c in n)

def sodep(n):
    res = []
    for i in range(22,int(n)):
        i = str(i)
        if len(i) % 2 == 0 and i == i[::-1] and chuachan(i):
            res.append(i)
    return(" ".join(res))

def decode(s):
    cnt = 0
    res = ""
    while cnt < len(s):
        char = s[cnt]
        cnt += 1
        digit = s[cnt]
        res += char * int(digit)
        cnt += 1
    return res

def encode(s):
    cnt = 1
    res = ""
    i = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cnt += 1
            i += 1
        else:
            res += (str(cnt) + s[i-1])
            cnt = 1
    res += (str(cnt) + s[-1])
    return res

P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def decode2(k,s):
    res = ""
    if k == 0:
        return
    for i in s:
        idx = P.index(i)
        res += P[(idx + k) % 28]
    return(res[::-1])

def kcach(s):
    n = len(s)
    rev = s[::-1]
    for i in range(1,n):
        if abs(ord(rev[i]) - ord(rev[i-1])) != abs(ord(s[i]) - ord(s[i-1])):
            return "NO"
    return "YES"

def chanle(s):
    if sum(int(c) for c in s) % 10 != 0:
        return "NO"
    for i in range(1,len(s)):
        if abs(int(s[i]) - int(s[i-1])) != 2:
            return "NO"
    return "YES"

def bobanto(l,r):
    num = list(range(l,r+1))
    for a,b,c in combinations(num,3):
        if gcd(a,b) == 1 and gcd(b,c) == 1 and gcd(a,c) == 1:
            print(f"({a}, {b}, {c})")

def chiahet7(n):
    ok = False
    if int(n) % 7 == 0:
        ok = True
        return n
    else:
        for i in range(1,1000):
            rev = str(n)[::-1]
            res = int(rev) + int(n)
            if res % 7 == 0:
                ok = True
                return res
            else:
                n = res
        if ok == False:
            return -1

def sodep(n):
    if n[0] == n[1]:
        return "NO"
    for i in range(0,len(n)-2):
        if i % 2 == 0 and n[i] != n[i+2]:
            return "NO"
        if i % 2 == 1 and n[i] != n[i+2]:
            return "NO"
    return "YES"


def sotaanggiam(n):
    ok = 1
    if len(n) < 3:
        return "NO"
    for i in range(0,len(n)-1):
        if n[i] < n[i+1]:
            if ok == 0:
                return "NO"
            ok = 1
        else:
            ok = 0
    return "YES"

def ktrahecs3(n):
    if all(c in "012" for c in n):
        return "YES"
    return "NO"

def revchan(n):
    res = []
    for i in range(2,7,2):
        half_s = 10 ** (i // 2 -1)
        half_e = 10 ** (i // 2)

        for half in range(half_s,half_e):
            s = str(half)
            palid = int(s + s[::-1])

            if palid >= int(n):
                break

            if len(str(palid)) % 2 == 0 and all(c in "02468" for c in str(palid)):
                res.append(str(palid))
    return " ".join(res)

def hanoi(n,dau,tg,cuoi):
    if n == 1:
        print(f"{dau} -> {cuoi}")
        return
    hanoi(n -1,dau,cuoi,tg)
    print(f"{dau} -> {cuoi}")
    hanoi(n - 1,tg,dau,cuoi)

def kitu(s):
    if set(s) != {"A","B","C"}:
        return False
    return s.count("A") <= s.count("B") <= s.count("C")

def solve(n):
    for len in range(3,n+1):

        for s in product("ABC",repeat=len):
            s = "".join(s)
            if kitu(s):
                print(s)
def uocsolon(a,b):
    curr = 0
    for i in range(len(b)):
        curr = (curr * 10 + int(b[i])) % a
    if a == 0:
        return int(b)
    return gcd(a,curr)

def fibo(n = 93):
    fib = [0] * (n + 1)
    fib[1] = 1
    fib[2] = 1
    for i in range(3,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def hamming(n):
    m = {1:1}
    while True:
        a = []
        check = 1
        for i in m:
            if i < 10 ** 10:
                if not (i * 2 in m):
                    a.append(i * 2)
                if not i * 3 in m:
                    a.append(i * 3)
                if not i * 5 in m:
                    a.append(i * 5)
        for i in a:
            check = 0
            m[i] = 1
        if check == 1:
            break
    a = sorted(list(m))
    dem = 1
    for i in a:
        m[i] = dem
        dem += 1
    if n in m:
        print(m[n])
    else:
        print("Not in sequence")
t = int(input())
n = hamming()
for _ in range(t):
    n = int(input())
    print()





"""
1
1221
1234567891011121314151617181920212223242526272829
"""