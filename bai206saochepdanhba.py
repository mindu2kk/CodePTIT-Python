# pykt075.py
class Data:
    def __init__(self, day, name, phoneNumber) -> None:
        self.day = day
        self.name = name
        self.phoneNumber = phoneNumber
        a = name.strip().split(" ")
        self.lastName = a[-1]
        self.firstMiddleName = a[:-1]
        # middleName = ""
        # for i in range(1, len(a) - 1):
        #     middleName += a[i] + " "
        # self.middleName = middleName.strip()

    def __str__(self) -> str:
        return self.name + ": " + self.phoneNumber + " " + self.day;


def cmp(a):
    return (a.lastName, a.firstMiddleName)


def main():
    # Write your code here
    dt = []

    # with open("pykt075/SOTAY.txt", 'r') as f:
    with open("SOTAY.txt", 'r') as f:
        s = f.readline().strip()
        day = s.split()[1]
        while True:
            try:

                s = f.readline().strip()
                if (len(s) == 0):
                    break
                if (s.count("/") > 0):
                    date = s.split(" ")
                    day = date[1]
                else:
                    phoneNumber = f.readline().strip()
                    dt.append(Data(day, s, phoneNumber))
            except:
                break
    dt.sort(key=cmp)
    # with open("pykt075/DIENTHOAI.txt", "w") as f:
    with open("DIENTHOAI.txt", "w") as f:
        for x in dt:
            f.writelines(str(x) + "\n")


if __name__ == '__main__':
    main()