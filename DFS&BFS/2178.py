import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque()
    distance = [-1] *(n+1) 
    # 0 push pop print 0 push
    visited[start] = True
    distance[start] = 0
    queue.append(start)
    while queue:
        now_v = queue.popleft()
        for next_v in graph[now_v]:
            continue
        visited[next_v] = True
        distance[next_v] = distance[now_v] + 1
        queue.append(next_v)
    return min(distance)
            
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
      
    
start = 1
visited = [False] * (n+1)
print(bfs(graph, start, visited))



##
from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 벽이므로 진행 불가
      if graph[nx][ny] == 0:
        continue
      
      # 벽이 아니므로 이동
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return graph[N-1][M-1]

print(bfs(0, 0)) 


######
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_r, start_c, visited, distance):
    derivatives = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    queue = deque()
    visited[start_r][start_c] = 0
    distance[start_r][start_c] = 1
    queue.append((start_r, start_c))
    while queue:
        now_r, now_c = queue.popleft()
        for dr, dc in derivatives:
            next_r, next_c = now_r + dr, now_c + dc
            if not (-1 < next_r < N and -1 < next_c < M):
                continue
            if visited[next_r][next_c] == 0:
                continue
            visited[next_r][next_c] = 0
            distance[next_r][next_c] = distance[now_r][now_c] + 1
            queue.append((next_r, next_c))
    return distance[N-1][M-1]

N, M = map(int, input().split())

visited = [list(map(int, input().rstrip())) for _ in range(N)]  # 1 은 갈수 있고 0은 갈 수 없다
distance = [[0] * M for _ in range(N)]

print(bfs(0,0,visited, distance))