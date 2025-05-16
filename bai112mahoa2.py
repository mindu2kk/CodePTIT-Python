"""
Cho dãy ký tự chuẩn P[] gồm 28 chữ cái, trong đó có 26 chữ cái in hoa từ A đến Z, hai ký tự cuối là gạch dưới ‘_’ và dấu chấm ‘.’
P[] = “ABCDEFGHIJKLMNOPQRSTUVWXYZ_.”
Phép mã hóa với khoảng cách K (0<K<28) được định nghĩa là phép chuyển các ký tự s[i] thành ký tự P[(i+K)%28] trong dãy ký tự chuẩn P nói trên.
Ví dụ với K = 3 thì ‘A’ chuyển thành ‘D’; ‘B’ chuyển thành ‘E’ và ‘.’ chuyển thành ‘C’.
Cho số K và một xâu S (chỉ bao gồm các chữ cái thuộc P[], không có khoảng trống). Hãy mã hóa xâu S theo quy tắc trên, sau đó đảo ngược thứ tự các chữ cái.

Input
Mỗi dòng ghi số K và xâu S.
Input kết thúc khi K = 0.

Output
Ghi ra kết quả cho từng test.

1 ABCD
14 ROAD
0
"""
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    try:
        k, s = input().split()
    except ValueError:
        break
    k = int(k)
    if k == 0:
        break
    res = ""
    for i in s:
        i = P.index(i)
        res += P[(i + k) % 28]
    print(res[::-1])




