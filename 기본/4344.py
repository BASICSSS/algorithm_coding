import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    nums_sum = sum(nums[1:])
    nums_avg = nums_sum//nums[0]
    cnt = 0
    for i in nums[1:]:
        if i > nums_avg:
            cnt += 1
        else:
            pass
    result = round(100/nums[0]*cnt, 3)
    print(str(format(result, ".3f"))+"%")