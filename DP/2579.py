import sys
input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]

memos = [[0, 0],[0, 0]]

for i in range(2, n+2):
    memos.append([memos[i-1][1]+stair[i-2], max(memos[i-2])+stair[i-2]])


print(max(memos[-1]))
