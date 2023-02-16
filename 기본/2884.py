# import sys
# input = sys.stdin.readline

# H, M = map(int, input().split())

# if M < 45:
#     if H==0:
#         H=23
#         M += 60
#     else:
#         H -= 1
#         M += 60
        

# print(H, M-45)


import sys
input = sys.stdin.readline

H, M = map(int, input().split())

if M < 45:
    if H==0:
        print(23, (60+M)-45)
    else:
        print(H-1,(60+M)-45)
else:
    print(H, M-45)