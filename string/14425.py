import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# s = list()
s = set()

for _ in range(n):
    word = input().rstrip()
    # s.append(word)
    s.add(word)
    
cnt = 0
for _ in range(m):
    word = input().rstrip()
    if word in s:
        cnt += 1
        
print(cnt)