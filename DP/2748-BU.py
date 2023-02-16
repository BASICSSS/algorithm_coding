import sys
input = sys.stdin.readline

n = int(input())

memos = [0,1]

for i in range(2, n+1):
    memos.append(memos[i-1] + memos[i-2])
    
print(memos[n])