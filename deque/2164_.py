import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
	queue.append(i+1)

for num in range(1, n + 1):
	if len(queue) == 1:
		print(queue[0])
		break
	queue.popleft()
	next_v = queue.popleft()
	queue.append(next_v)

