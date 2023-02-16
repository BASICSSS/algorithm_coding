import sys
n = int(sys.stdin.readline())

stair_value = [0] # 찾은 규칙성으로 인해 2번쨰 리스트는 0번쨰를 참조해야함 그래서 해당 값에 맞는 더미 만들어줌
for i in range(n):
    stair_value.append(int(sys.stdin.readline()))

memo = [[0,0],[stair_value[1], 0], [stair_value[1]+stair_value[2], stair_value[2]]] # 규칙이 적용안되는 0-2(3번쨰)까지 아예 전처리 해주었음
print(stair_value)
print(memo)

for i in range(3, n+1): # DP메모이제이션!
    memo.append([ memo[i -1 ][1]+stair_value[i], max(memo[i -2 ]) + stair_value[i] ]) # 규칙을 적용하여 DP

print(max(memo[n]))
