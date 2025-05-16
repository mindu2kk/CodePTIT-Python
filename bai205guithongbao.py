"""
Theo quy định của một số thiết bị. Nội dung thông báo chỉ được phép chứa tối đa 100 ký tự.
Điều này đòi hỏi lập trình viên phải xử lý nội dung các thông báo có độ dài lớn hơn 100 ký tự bằng cách rút gọn thông tin.
Tuy nhiên, việc rút gọn phải đảm bảo nguyên tắc không bị cắt giữa từ.
Trong trường hợp nếu từ hiện tại làm độ dài thông báo vượt quá 100 ký tự sẽ loại bỏ từ đó khỏi thông báo.
Nhiệm vụ của bạn là hãy viết chương trình xử lý yêu cầu trên.

Input:

Dòng đầu tiên là số bộ test T < 100.
T dòng tiếp theo mỗi dòng là một xâu ký tự có độ dài tối đa 1000 ký tự.
"""

def shorten_message(text):
    words = text.split()
    result = []
    length = 0

    for word in words:
        if length + len(word)> 100:
            break
        result.append(word)
        length += len(word) + (1 if result else 0)

    print(" ".join(result))

T = int(input().strip())

for _ in range(T):
    text = input().strip()
    shorten_message(text)