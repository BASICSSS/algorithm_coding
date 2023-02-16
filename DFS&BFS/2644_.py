import sys
from collections import deque

def find_chon(graph, visited, start, end):
    
    queue = deque([start])
    visited[start] = True
    count = [0] * (n + 1)

    while queue:
        now_v = queue.popleft()
        for next_v in graph[now_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
                count[next_v] = count[now_v] + 1
                if next_v == end:
                    return count[next_v]
    return -1


n = int(sys.stdin.readline())
num_a, num_b = map(int, input().split())
m = int(sys.stdin.readline())

graph = [ [] for _ in range(n+1)]
visited = [False] * (n +1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(find_chon(graph, visited, num_a, num_b))


# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(graph, start, end, visited):
#     distances = [0] * (v + 1)
#     # 0 push pop print 0 push
#     queue = deque()
#     visited[start] = True
#     queue.append(start)
    
#     while queue:
#         now_v = queue.popleft()
#         for next_v in graph[now_v]:
#             if visited[next_v]:
#                 continue
#             visited[next_v]=True
#             distances[next_v] = distances[now_v] +1
#             queue.append(next_v)
#             if next_v == end:
#                 return distances[next_v]
    
#     return -1


# v = int(input())
# start, end = map(int, input().split())
# e = int(input())

# graph = [[] for _ in range(v+1)]

# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# visited = [False] * (v+1)

# print(bfs(graph, start, end, visited))
