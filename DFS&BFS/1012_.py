from collections import deque
import sys
input = sys.stdin.readline
# dx = [-1, -2, -2, -1, 1, 2, 2, 1]
# dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [-1, -2, -1, -2, 1, 2, 1, 2]
dy = [-2, -1, 2, 1, -2, -1, 2, 1]
def bfs(sx, sy, ax, ay,s):
    q = deque()
    q.append((sx, sy))
    while q:
        a, b = q.popleft()
        if a == ax and b == ay:
            break
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                q.append((x, y))
                s[x][y] = s[a][b] + 1
    print(s[ax][ay])
    
        
t = int(input())
for i in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay,s)