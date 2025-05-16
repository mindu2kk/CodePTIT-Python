"""
Cho danh sách các email trong file CONTACT.in, hãy loại bỏ các email trùng nhau và sắp xếp các email còn lại theo thứ tự từ điển.
Chú ý: địa chỉ email thì không phân biệt chữ hoa, chữ thường. Kết quả in ra cần đưa tất cả về dạng chữ thường.

Input - file văn bản CONTACT.in
Gồm không quá 300 dòng, mỗi dòng ghi một địa chỉ email.
Độ dài mỗi email không quá 100 ký tự.
Chú ý: Dữ liệu vào không có số dòng nên cần đọc đến hết file.

Output
Ghi ra danh sách các email đã loại bỏ trùng nhau và sắp xếp theo thứ tự từ điển.
"""
def process_email(file_path):
    with open(file_path, 'r') as file:
        emails = set()
        for line in file:
            email = line.strip().lower()
            emails.add(email)

    sorted_emails = sorted(emails)
    return sorted_emails

result = process_email('CONTACT.in')
for email in result:
    print(email)