import sys
input  = sys.stdin.readline

start, end = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(start):
    for j in range(i+1, start):
        for k in range(j+1, start):
            if arr[i] + arr[j] + arr[k] > end:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])
                
print(result)


##
n, m = map(int, input().split())

cards = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_of_cards = cards[i] + cards[j] + cards[k]
            if sum_of_cards > m:
                pass
            else:
                result = max(result, sum_of_cards)
        
print(result)
