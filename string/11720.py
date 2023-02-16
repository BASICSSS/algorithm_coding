import sys
input = sys.stdin.readline

n = int(input())
arr = input().rstrip()
answer = 0

for i in range(n):
    answer += int(arr[i])
    
print(answer)