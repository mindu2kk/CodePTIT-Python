"""
Khi  viết giá trị số nguyên trong Tiếng Anh, người ta thường thêm dấu phẩy để phân tách các nhóm 3 chữ số (tính từ cuối). Ví dụ số 153920529 được viết lại thành 153,920,529.

Cho số nguyên dương N trong phạm vi số int (không quá 2 tỷ). Hãy chèn dấu phẩy vào N theo quy tắc trên.

Input

Chỉ có 1 số N

Output

Kết quả sau khi đã chèn dầu phẩy
153920529

"""
def test(n):
    res = []
    n = str(n)

    for i,digit in enumerate(reversed(n)):
        if i > 0 and i % 3 == 0:
            res.append(',')
        res.append(digit)
    return ''.join(reversed(res))

n = int(input())
print(test(n))

