nums = list(map(int, input().split()))
i = 0
answer = 0
 
while i<5:
    answer += nums[i]**2
    i += 1
    
print(answer%10)