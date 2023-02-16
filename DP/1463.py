# hint 10 생각해서 해보기
# 1 2 3 4 5 6 7 8 9 10
# 0 1 2 2 3 2 3 3 2 3

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)	
## d에 계산된 값을 저장해둔다. n + 1이라고 한 이유는, 1번째 수는 사실 d[1]이 아니고 d[2]이기 때문에,계산하기 편하게 d[1]을 1번째 인 것 처럼 만들어준다.

for i in range(2, n + 1):
    nums = [dp[i - 1]]
    if i % 3 == 0:
        nums.append(dp[i//3])
    if i % 2 == 0:
        nums.append(dp[i//2])
    dp[i] = min(nums) + 1
    # print(i, nums)
print(dp[n])

