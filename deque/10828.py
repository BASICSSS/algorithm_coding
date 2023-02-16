import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

stack = deque()

for _ in range(n):
    data = input().split()
    if data[0] == "push":
        stack.append(data[1])
    elif data[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif data[0] == "size":
        print(len(stack))
    elif data[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif data[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])

