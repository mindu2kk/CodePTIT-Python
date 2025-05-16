"""
Cho một số nguyên dương không quá 200 chữ số. Mỗi bước tách số nguyên thành hai nửa: nửa đầu là n/2 chữ số đầu tiên, nửa sau là phần còn lại (trong đó n là số chữ số của số ban đầu, nếu n lẻ thì phép chia 2 sẽ tính phần nguyên). Sau đó thực hiện tính tổng của hai nửa này.
Lặp lại các bước trên cho đến khi kết quả chỉ còn là số có 1 chữ số.
Hãy thực hiện tính toán và in kết quả của từng bước.

Input
Chỉ có một số nguyên dương không quá 200 chữ số.

Output
Ghi ra kết quả từng bước, mỗi bước trên một dòng. Dừng lại khi kết quả chỉ còn 1 chữ số.
"""

n = input()
while len(n) > 1:
    n = str(int(n[:len(n)//2]) + int(n[len(n)//2:]))
    print(n)
