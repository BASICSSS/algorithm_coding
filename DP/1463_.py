import sys

def calc_count(num):
    count_list = [0,0,1]
    for i in range(3, num+1):
        ch = []
        ch.append(count_list[i - 1] + 1)
        if i % 3 == 0:
            ch.append(count_list[i // 3] + 1)
        if i % 2 == 0:
            ch.append(count_list[i // 2] + 1)
        count_list.append(min(ch))
    return count_list[num]

N = int(sys.stdin.readline())
print(calc_count(N))