import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    # 0push pop 0push
    distance = [0] * (v+1)
    queue = deque()
    visited[start] = True
    queue.append(start)
    while queue:
        now_v = queue.popleft()
        for next_v in graph[now_v]:
            if visited[next_v]:
                continue
            visited[next_v]=True
            distance[next_v]=distance[now_v]+1
            queue.append(next_v)
    return sum(distance)
    
v, e = map(int, input().split())
start = 1
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
result = [-1]
for i in range(1,v+1):
    visited = [False] *(v+1)
    result.append(bfs(graph, i))
    
print(result.index(min(result[1:])))
