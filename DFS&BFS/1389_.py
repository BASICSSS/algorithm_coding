import sys
from collections import deque

##BFS =>최단거리 문제

def search_backen(graph, visited, start, nums):
    backen_num = [0] * (nums + 1)
    queue = deque([start])
    visited[start] = True
    backen_num[start] = 0

    while queue:
        current_v = queue.popleft()
        for next_v in graph[current_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
                backen_num[next_v] = backen_num[current_v] +1 ## 여게 해심
    return sum(backen_num)

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)] # N+1로 0인덱스를 만들어서 호출 편하게 맞춰줌
for i in range(M):
    user_a, user_b = map(int, input().split())
    graph[user_a].append(user_b)
    graph[user_b].append(user_a)


backen_list =[]
for i in range(1, N+ 1):
    visited = [False] * (N + 1)
    backen_list.append(search_backen(graph, visited, i, N))


print(backen_list.index(min(backen_list)) + 1)
