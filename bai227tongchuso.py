"""
Cho một số nguyên (có thể âm) không quá 100.000 chữ số.
Mỗi bước thực hiện thay thế số nguyên này bằng giá trị tổng chữ số của số đó.
 Hỏi sau mấy bước thì số đó chỉ còn duy nhất 1 chữ số.

Input
Chỉ có duy nhất số nguyên N (không quá 100.000 chữ số)

Output
Ghi ra số bước cần thực hiện.
"""

n = str(input())
cnt = 0
while len(n) > 1:
    n = str(sum(ord(d) - 48 for d in str(n)))
    cnt += 1
print(cnt)