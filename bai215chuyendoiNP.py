from math import *


def toS(i):
    if i <= 9:
        return str(i)
    return chr(ord('A') + i - 10)


def convert(s):
    s = s[::-1]
    ans = 0
    for i in range(len(s)):
        x = ord(s[i]) - 48
        ans += x * (2 ** i)
    return int(ans)


def main():
    # with open('pykt086/DATA.in', 'r') as r:
    with open('DATA.in', 'r') as r:
        # T = int(r.readline().strip())
        for _ in range(int(r.readline().strip())):
            n = int(r.readline().strip())
            x = int(log2(n))
            s = r.readline().strip()

            # Pad the string with leading zeros to make its length a multiple of x
            while len(s) % x != 0:
                s = "0" + s

            ans = ''
            while s:
                ans = toS(convert(s[-x:])) + ans
                s = s[:-x]

            print(ans)


if __name__ == '__main__':
    main()