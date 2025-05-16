"""
Trong 10 chữ số thập phân thì có 4 chữ số nguyên tố là 2, 3, 5, 7.
Một số nguyên dương được coi là thỏa mãn nguyên tố đúng vị trí nếu thỏa mãn cả hai điều kiện:
Nếu i là nguyên tố thì vị trí thứ i cũng phải là chữ số nguyên tố.
Ngược lại nếu i không phải là số nguyên tố thì vị trí thứ i không phải là chữ số nguyên tố.
Ví dụ: số 14239567 thỏa mãn nguyên tố đúng vị trí vì các vị trí thứ 2, 3, 5, 7 là các chữ số nguyên tố, các vị trí khác không nguyên tố.
Viết chương trình kiểm tra một số nguyên dương không quá 500 chữ số có thỏa mãn tính chất trên hay không.

Input
Dòng đầu ghi số bộ test, không quá 10.
Mỗi bộ test viết trên một dòng số nguyên dương không quá 500 chữ số.

Output
Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

2
14239567
2314514535353
"""
def checnt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = input()
    ok = True
    for i in range(len(n)):
        if checnt(i) and not checnt(int(n[i])):
            print("NO")
            ok = False
            break
        elif not checnt(i) and checnt(int(n[i])):
            print("NO")
            ok = False
            break
    if ok:
        print("YES")

