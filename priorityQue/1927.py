import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
pq = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(pq, x)
    elif x == 0:
        if not pq:
            print(0)
        else:
            print(heappop(pq))