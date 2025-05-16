"""
Cho số nguyên dương N. Nhiệm vụ của bạn là hãy liệt kê tất cả các cách biểu diễn N thành tổng các số tự nhiên nhỏ hơn hoặc bằng N. Phép hoán vị của một cách được xem là giống nhau.
Ví dụ với N = 5 ta có kết quả là: (5), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1) .

Input:
Dòng đầu tiên đưa vào số lượng test T.
Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một số tự nhiên N được viết trên một dòng.
T, n thỏa mãn ràng buộc: 1≤T, N≤10.

Output:
Dòng đầu tiên là số lượng cách phân tích thỏa mãn.
Dòng tiếp theo liệt kê đáp án theo mẫu ví dụ đã cho.
"""
def tryy(n,max_val,path):
    if n == 0:
        res.append(f"({' '.join(map(str,path))})")
        return
    for i in range(min(n,max_val),0,-1):
        tryy(n - i,i,path + [i])

t = int(input())

for _ in range(t):
    n = int(input())
    res = []
    tryy(n,n,[])
    print(len(res))
    print(" ".join(res))

