import sys
input = sys.stdin.readline

def binary_search(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        y_mid = nums[mid]
        if y_mid < target:
            left = mid + 1
        elif y_mid > target:
            right = mid - 1
        elif y_mid == target:
            return mid
    return -1

n = int(input())
nums = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

nums.sort()
left, right = 0, len(nums)-1

for target in targets:
    if binary_search(nums, target, left, right) == -1:
        print(0)
    else:
        print(1)