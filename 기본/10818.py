# import sys
# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int, input().split()))
# answer = []
# answer.append(min(nums))
# answer.append(max(nums))

# print(answer[0], answer[1])

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# def min_max(nums):
#     nums.sort()
#     return (str(nums[0])+" " +str(nums[-1]))


# print(min_max(nums))

def min_max(nums):
    nums_min = 1000000
    nums_max = -1000000
    i = 0
    while i < len(nums):
        if nums_min > nums[i]:
            nums_min = nums[i]
        elif nums_max < nums[i]:
            nums_max = nums[i]
        i += 1
    return nums_min, nums_max

nums_min, nums_max = min_max(nums)
print(nums_min, nums_max)