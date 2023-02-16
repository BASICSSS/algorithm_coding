from collections import Counter

N = int(input())
all_nums = list(map(int, input().split()))
M = int(input())
calc_nums = list(map(int, input().split()))
nums = Counter(all_nums)

for num in calc_nums:
    print(nums[num], end=' ')
