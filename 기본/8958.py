import sys
input = sys.stdin.readline
n = int(input())
result = 0
answer = 0

for _ in range(n):
    arr = input().rstrip()
    for i in range(len(arr)):
        if i == len(arr):
            break
        if arr[i]=="O":
            if arr[i] == arr[i+1]:
                answer += 1
            result += answer
        elif arr[i]=="X":
            answer = 0
    print(result)
    
    
# 확인 필요
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)
    