import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
m = max(nums)
answer = 0

for i in nums:
    answer += i / m *100
    

print(answer / n)