import sys

def search_nums(ref, target ):
    start, end = 0, len(ref) - 1
    while start <= end:
        mid = (start + end) // 2
        if ref[mid] < target:
            start = mid + 1
        elif ref[mid] > target:
            end = mid - 1
        elif ref[mid] == target:
            return 1
    return 0
    

N = int(sys.stdin.readline())
ref = list(map(int, input().split()))
ref.sort()
M = int(sys.stdin.readline())
array = list(map(int, input().split()))

for num in array:
    if search_nums(ref, num) == 1:
        print("1")
    else:
        print(0) 