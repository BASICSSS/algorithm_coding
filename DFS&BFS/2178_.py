import sys
from collections import deque

dir_r = [-1,1,0,0]
dir_c = [0,0,-1,1]
def BFS(start_r, start_c, graph, visited):
    distance = [[1] * (M+1) for _ in range(N)]
    queue = deque([(start_r, start_c)]) #튜플로 넣어줘야하며 튜플로 넣었을때 접근은 인덱스가 아닌 각각의 값으로 받아야함
    visited[start_r][start_c] = True
    # while queue: #기존 그래프 형식의 큐에서 한의 값을 뺄때
    #     curr_nd = queue.popleft()
    #     for next_nd in graph:
    #         if not graph[next_nd]:
    #             graph[next_nd] = True
    #             queue.append(next_nd)
    while queue:
        curr_nd = queue.popleft()
        for i in range(4):
            next_r = curr_nd[0] + dir_r[i]
            next_c = curr_nd[1] + dir_c[i]
            if (0 <= next_r < N) and (0<= next_c < M) and graph[next_r][next_c] == 1:
                if not visited[next_r][next_c]:
                    queue.append([next_r, next_c])
                    visited[next_r][next_c] = True
                    distance[next_r][next_c] = distance[curr_nd[0]][curr_nd[1]] + 1
    return distance[N-1][M-1]

N, M = map(int, input().split())

graph =[]
for _ in range(N): #이건 어차피 미로형태로 들어가는 거라 그래프 빈공간 따로 안만들고 바로 넣으면 됨
    graph.append(list(map(int, input())))

print(graph)

visited = [[False] * (M+1) for _ in range(N)]
print(BFS(0,0, graph, visited))


# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(start_r, start_c, visited, distance):
#     derivatives = [
#         (-1,0),
#         (1,0),
#         (0,-1),
#         (0,1)
#     ]

#     queue = deque()
#     visited[start_r][start_c] = 0
#     distance[start_r][start_c] = 1
#     queue.append((start_r, start_c))
#     while queue:
#         now_r, now_c = queue.popleft()
#         for dr, dc in derivatives:
#             next_r, next_c = now_r + dr, now_c + dc
#             if not (-1 < next_r < N and -1 < next_c < M):
#                 continue
#             if visited[next_r][next_c] == 0:
#                 continue
#             visited[next_r][next_c] = 0
#             distance[next_r][next_c] = distance[now_r][now_c] + 1
#             queue.append((next_r, next_c))
#     return distance[N-1][M-1]

# N, M = map(int, input().split())

# visited = [list(map(int, input().rstrip())) for _ in range(N)]  # 1 은 갈수 있고 0은 갈 수 없다
# distance = [[0] * M for _ in range(N)]

# print(bfs(0,0,visited, distance))