"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:
Tích các chữ số ở vị trí chẵn – giá trị tích chữ số có thể đến 18 chữ số. Chú ý khi tính tích bỏ qua các chữ số 0.
Tổng các chữ số ở vị trí lẻ

Input
Dòng đầu ghi số bộ test (không quá 20)
Mỗi bộ test ghi trên một dòng số nguyên dương N (ít nhất 2 chữ số và không quá 500 chữ số)

Output
Với mỗi bộ test, viết trên một dòng hai giá trị: tích chữ số và tổng chữ số tính được.
"""
def tich(lst,n):
    tich=1
    check=False
    for i in range(0,n,2):
        if int(lst[i]) !=0:
            tich*=int(lst[i])
            check=True
    if check == False:
        tich=0
    return tich

def tong(lst,n):
    tong=0
    check=False
    for i in range(1,n,2):
        tong += int(lst[i])
    return tong

t = int(input())

for _ in range(t):
    lst = input()
    print(f"{tich(lst,len(lst))} {tong(lst,len(lst))}")

