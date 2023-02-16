import sys

def hansoo(num):
    count = 0
    for i in range(1, num+1):
        if i<100:
            count += 1
        else:
            num_string = str(i)
            if (int(num_string[0]) - int(num_string[1])) == (int(num_string[1]) - int(num_string[2])):
                count +=1
    return count

N = int(sys.stdin.readline())
print(hansoo(N))