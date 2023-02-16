import sys

def find_lens(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total_sep_lans = 0
        for lan in array:
            total_sep_lans += lan // mid
        if total_sep_lans < target:
            end = mid - 1
        else:
            start = mid + 1
    return end
            
K, N = map(int, input().split())
array = [ int(input()) for _ in range(K)]
start = 0
end = len(array)

print(find_lens(array, N, start, end))
