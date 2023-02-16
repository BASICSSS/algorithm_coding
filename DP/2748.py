import sys
input = sys.stdin.readline

def fibo(n):
    if memos[n] == -1:
        memos[n] = fibo(n-1) + fibo(n-2) 
    return memos[n]

n = int(input())
memos = [-1] * 91
memos[0] = 0
memos[1] = 1

print(fibo(n))