"""
Dãy số Fibonacci được định nghĩa theo công thức như sau:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 với n>2
Cho hai số nguyên dương a và b (1 < a < b < 93). Viết chương trình liệt kê các số Fibonacci từ a đến b.

Input

Dòng đầu ghi số bộ test, không quá 10.
Mỗi bộ test viết trên một dòng hai số a và b.

Output
Ghi ra kết quả của mỗi test trên một dòng, mỗi số cách nhau một khoảng trống
"""

def test(n = 93):
    fib = [0] * (n + 1)
    fib[1] = 1
    fib[2] = 1
    for i in range(3,n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

t = int(input().strip())

fibo = test()

for _ in range(t):
    a,b = map(int,input().split())
    print(" ".join(map(str,fibo[a:b + 1])))