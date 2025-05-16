"""
Cho xâu nhị phân X[] có độ dài n. Nhiệm vụ của bạn là hãy đổi xâu nhị phân thành một số ở hệ cơ số b, trong đó b chỉ là một trong các số 2, 4, 8, 16. Ví dụ xâu X =”10010100010010101” và b = 8 ta có kết quả là 224225 là số ở hệ cơ số 8.

Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là gồm hai dòng: dòng đầu tiên đưa vào b là cơ số của hệ đếm; dòng tiếp theo đưa vào xâu nhị phân có độ dài n.
T, n, X[] thỏa mãn ràng buộc : 1≤T≤10; 1≤ n≤105; X[i] =0, 1;

Output:
Đưa ra kết quả mỗi test theo từng dòng.

2
8
10010100010010101
2
10010100010010101
"""

def binary_to_base(b, X):
    return format(int(X, 2), f'{b}')

T = int(input())
for _ in range(T):
    b = int(input())
    X = input().strip()
    print(binary_to_base(b, X))
