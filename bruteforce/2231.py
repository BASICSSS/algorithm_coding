import sys
input = sys.stdin.readline

n = int(input())
result = 0

for i in range(1, n+1):
    temp = i + sum(map(int, str(i)))
    
    if temp == n:
        result = i
        break
    
print(result)