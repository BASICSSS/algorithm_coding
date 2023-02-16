import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, end, visited):
    distances = [-1] * (v + 1)
    # 0 push pop print 0 push
    queue = deque()
    visited[start] = True
    distances[start] = 0  # 거리도 넣어줘야함
    queue.append(start)
    
    while queue:
        now_v = queue.popleft()
        for next_v in graph[now_v]:
            if visited[next_v]:
                continue
            visited[next_v]=True
            distances[next_v] = distances[now_v] +1
            queue.append(next_v)
            if next_v == end:
                return distances[next_v]
    
    return -1


v = int(input())
start, end = map(int, input().split())
e = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (v+1)

print(bfs(graph, start, end, visited))
