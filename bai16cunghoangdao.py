"""

"""
def test(day, month):
    zodiac_ranges = [
        ((20, 1), (18, 2), "Bao Binh"),
        ((19, 2), (20, 3), "Song Ngu"),
        ((21, 3), (19, 4), "Bach Duong"),
        ((20, 4), (20, 5), "Kim Nguu"),
        ((21, 5), (20, 6), "Song Tu"),
        ((21, 6), (22, 7), "Cu Giai"),
        ((23, 7), (22, 8), "Su Tu"),
        ((23, 8), (22, 9), "Xu Nu"),
        ((23, 9), (22, 10), "Thien Binh"),
        ((23, 10), (22, 11), "Thien Yet"),
        ((23, 11), (21, 12), "Nhan Ma"),
        ((22, 12), (19, 1), "Ma Ket")
    ]

    for (start_day, start_month), (end_day, end_month), sign in zodiac_ranges:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign

t = int(input())

for _ in range(t):
    day, month = map(int, input().split())
    print(test(day, month))
