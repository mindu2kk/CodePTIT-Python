"""
Cho N xâu S[1], S[2], …, S[N] có độ dài bằng nhau. Mỗi bước, với xâu T, bạn được phép xoay vòng 1 kí tự, tức lấy kí tự đầu tiên của T rồi chuyển xuống cuối. Ví dụ xâu “cool” sẽ chuyển thành “oolc”.
Bạn cần phải xoay N xâu sao cho tất cả chúng đều giống nhau. Hãy xác định số bước ít nhất để hoàn thành được công việc này?

Input:
Mỗi test bắt đầu bởi số nguyên N (1 ≤ N ≤ 50).
N dòng tiếp theo, mỗi dòng gồm xâu S[i] có độ dài không quá 50.

Output:
Với mỗi test, in ra số bước ít nhất tìm được, nếu không thể biến đổi, hãy in ra “NO”.

4
xzzwo
zwoxz
zzwox
xzzwo

3
aa
aa
ab
"""

def rotate_str(s,k):
    return s[k:] + s[:k]

def min_rotation_steps(strings):
    n = len(strings)
    length = len(strings[0])
    min_step = float('inf')

    for shift in range(length):
        target = rotate_str(strings[0],shift)
        total_steps = shift

        for s in strings[1:]:
            min_shift = float('inf')

            for k in range(length):
                if rotate_str(s,k) == target:
                    min_shift = min(min_shift,k)
            if min_shift == float('inf'):
                return -1
            total_steps += min_shift
        min_step = min(min_step,total_steps)
    return min_step


n = int(input())
strings = [input().strip() for _ in range(n)]
print(min_rotation_steps(strings))
