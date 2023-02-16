# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque
input = sys.stdin.readline
que = deque()

n = int(input())
for _ in range(n):
    data = list(input().split())
    if data[0] == "push":
        que.append(data[1])
    elif data[0] == "pop":
        if not que:
            print(-1)
        else:
            print(que.popleft())
    elif data[0] == "size":
        print(len(que))
    elif data[0] == "empty":
        if not que:
            print(1)
        else:
            print(0)
    elif data[0] == "front":
        if not que:
            print(-1)
        else:
            print(que[0])
    elif data[0] == "back":
        if not que:
            print(-1)
        else:
            print(que[-1])