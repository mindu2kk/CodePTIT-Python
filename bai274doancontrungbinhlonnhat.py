"""
Cho dãy số A[] có N phần tử, N không quá 105, các số trong dãy đều nguyên dương và không quá 9 chữ số. Hãy tính độ dài của dãy con liên tiếp có trung bình cộng lớn nhất trong dãy.
Trong trường hợp có nhiều dãy con liên tiếp đều có trung bình cộng lớn nhất thì dãy nào dài hơn sẽ được chọn.

Input
Dòng đầu ghi số N.
Dòng thứ 2 ghi N số của dãy A[]

Output
Ghi ra độ dài dãy con liên tiếp có trung bình cộng lớn nhất tìm được.
5
5 1 6 7 2
"""

n = int(input())
A = list(map(int,input().split()))

cnt,res = 0,0
m = max(A)
for i in A:
    if i == m:
        cnt += 1
    else:
        res = max(res,cnt)
        cnt = 0
print(max(res,cnt))
