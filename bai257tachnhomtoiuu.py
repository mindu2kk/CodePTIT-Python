"""
Cho dãy số A[] có N phần tử là các số nguyên dương. Với mỗi số nguyên K, hãy tính xem có thể tách dãy số A thành ít nhất bao nhiêu nhóm sao cho mỗi số trong nhóm đều có thể tìm được ít nhất một số khác cùng nhóm có chênh lệch không vượt quá K.
Ví dụ: A[] = {2, 6, 1, 7, 3, 4, 9}; K = 1 thì kết quả là 3 ứng với 3 nhóm {2,1,3,4}; {6,7};  {9}

Input
Dòng đầu ghi hai số N và K (0 <= K <= 105; 0 <= N <= 106).
Dòng thứ 2 ghi ra N số của dãy A[], các số nguyên dương và không quá 106.

Output
Ghi ra số nhóm ít nhất có thể.

7 1
2 6 1 7 3 4 9
"""

n,k = map(int,input().split())

A = list(map(int,input().split()))
A = sorted(A)
B = []
cnt = 1
for i in range(0,len(A) - 1):
    if A[i + 1] - A[i] > k:
        cnt += 1
print(cnt)