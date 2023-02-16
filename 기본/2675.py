# import sys
# input = sys.stdin.readline

# n = int(input())

# for _ in range(n):
#     num, arr = input().split()
#     text = ''
#     for i in arr:
#         text += i*int(num)
#     print(text)
    
T = int(input())

for _ in range(T):
    cnt, S = input().split()
    answer = ""
    for i in S:
        answer += int(cnt)*i
    print(answer)