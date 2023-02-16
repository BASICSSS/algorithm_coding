import sys

def max_cutter(trees, target, start, end):
    while start <= end:
        mid = (start + end ) // 2
        sep_tree_sum = 0
        for tree in trees:
            if tree > mid:
                sep_tree_sum += tree - mid
        if sep_tree_sum >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(max_cutter(trees, M, 0, max(trees)))