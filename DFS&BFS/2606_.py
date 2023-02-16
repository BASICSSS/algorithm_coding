import sys
from collections import deque

# BFS

# def birus(graph, visited, start):
#     queue = deque([start])
#     visited[start] = True
#     count = [0] * (n+1)

#     while queue:
#         current_v = queue.popleft()
#         for next_v in graph[current_v]:
#             if not visited[next_v]:
#                 visited[next_v] = True
#                 queue.append(next_v)
#                 count[next_v] = count[current_v] + 1
#     return count

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# cnt = 0 # print(sum(visited)-1) 로 방문여부만 체크해도 되겠네(결국 원하는건 이거였으니)
# for i in birus(graph, visited, 1):
#     if i !=0:
#         cnt += 1
# print(cnt)

# DFS

import sys
from collections import deque

def birus_dfs(graph, visited, start):
    
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            birus_dfs(graph, visited, i)
    print(visited)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

birus_dfs(graph, visited, 1)
print(sum(visited) - 1)