import sys
from collections import deque

def dfs(start, graph, visited): # DFS(queue) push ( pop * print push )  #print전에 visited

    visited[start] = True
    print(start, end=" ")
    for i in graph[start]: #각 노드의 인접노드 방문여부를 체크
        if not visited[i]:
            dfs(i, graph, visited)

def bfs(start, graph, bfs_visited): # BFS(stack) * push ( pop print * push ) #push전에 visited

    queue = deque([start])
    
    bfs_visited[start] = True
    
    while queue:
        visit_pop = queue.popleft()
        print(visit_pop, end = " ")
        for next_visit in graph[visit_pop]:
            if not bfs_visited[next_visit]:
                bfs_visited[next_visit] = True
                queue.append(next_visit)
    

input = sys.stdin.readline

v, e, start = map(int, input().split())

graph = []
for _ in range(v+1):
    graph.append([])

# graph = [[] for _ in range(v+1)] # 깊은 복사/ 얕은 복사

    
for _ in range(e):
    a, b = map(int, input().split()) #간선에 의해 양쪽다 같은 원소일것!
    graph[a].append(b)
    graph[b].append(a) 
    
for link in graph:
    link.sort()

visited = [False] * (v+1)
bfs_visited = [False] * (v+1)


dfs(start, graph, visited)
print()  # 줄 띄워주기용
bfs(start, graph, bfs_visited)
