"""
Cho một dãy số A[] có 4 số nguyên dương, đánh số vị trí từ 1 đến 4. Tại mỗi bước, giá trị A[i] được thay thế bằng abs(A[i] – A[i+1]), riêng A[4] = abs(A[4]-A[1]).
Hàm abs (trị tuyệt đối) được sử dụng để đảm bảo các giá trị của dãy số luôn dương.
Hãy đếm xem sau bao nhiêu bước thì dãy số A[] có cả 4 vị trí đều bằng nhau.

Input
Có 4 số của dãy A[], các giá trị không quá 9 chữ số. Input kết thúc với 4 số 0.

Output
Với mỗi test, ghi ra số bước cần thực hiện.

1 3 5 9
4 3 2 1
0 0 0 0
"""

while True:
    A = list(map(int, input().split()))

    if sum(A) == 0:
        break

    steps = 0

    while len(set(A)) > 1:
        A = [abs(A[i] - A[(i + 1) % 4]) for i in range(4)]
        steps += 1

    print(steps)
