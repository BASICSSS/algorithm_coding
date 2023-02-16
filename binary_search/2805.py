import sys
input = sys.stdin.readline

def binary_search(trees, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        y_mid = 0
        for tree in trees:
            if tree > mid:
                y_mid += tree - mid
        if y_mid < target:
            right = mid -1
        else:
            left = mid +1
    return right

n, target = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 1, max(trees)

print(binary_search(trees,target, left, right))