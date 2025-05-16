"""
Có N quốc gia, mỗi quốc gia có dân số xác định. Hãy xác định có thể xếp được tối đa bao nhiêu nhóm có đúng k thành viên mà các thành viên từ các nước khác nhau.

Input:
Gồm nhiều test (không quá 20), mỗi test có định dạng như sau:
Dòng đầu tiên chứa số nguyên N và k(1 ≤ k ≤ N ≤ 105):
Dòng tiếp theo chứa N số nguyên không âm là dân số từng nước, các giá trị này không vượt quá 1012

Ouput
Với mỗi test, in ra 1 số nguyên là đáp án của bài toán.

5
5 4
4 4 4 4 4
6 5
1 2 3 4 5 6
2 2
1000000000000 1000000000000
17 7
96 17 32 138 112 50 7 19 412 23 14 50 47 343 427 22 39
50 10
638074479 717901019 910893151 924124222 991874870 919392444 729973192 607898881 838529741 907090878 632877562 678638852 749258866 949661738 784641190 815740520 689809286 711327114 658017649 636727234 871088534 964608547 867960437 964911023 642411618 868318236 793328473 849540177 960039699 998262224 775720601 634685437 743766982 826321850 846671921 712570181 676890302 814283264 958273130 899003369 909973864 921987721 978601888 633027021 896400011 725078407 662183572 629843174 617774786 695823011
"""
def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        population = list(map(int, input().split()))

        population.sort()

        if k == 1:
            print(sum(population))
        else:
            result = 0
            while True:
                count = 0
                for i in range(n):
                    if population[i] > 0:
                        count += 1
                if count < k:
                    break
                for i in range(n):
                    if population[i] > 0:
                        population[i] -= 1
                        if population[i] < 0:
                            population[i] = 0
                result += 1

            print(result)

solve()