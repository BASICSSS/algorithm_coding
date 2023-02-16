import sys
input = sys.stdin.readline

def binary_search(lans, target, left, right):
    while left <= right:
        mid = (left + right) //2
        y_mid = 0
        for lan in lans:
            y_mid += lan // mid
        if y_mid < target: # 경우
            right = mid -1
        elif y_mid >= target: # 경우
            left = mid +1
    return right # 경우
            
            
# k, n     
k, target = map(int, input().split())

lans = [int(input()) for _ in range(k)]

left, right = 1, max(lans)
print(binary_search(lans, target, left, right))



import sys
input = sys.stdin.readline

def binary_search(lans, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        y_mid = 0
        for lan in lans:
            y_mid += lan // mid
        if y_mid < target:
            right = mid - 1
        elif y_mid >= target:
            left = mid + 1
    return right

k, target = map(int, input().split())
lans = [int(input()) for _ in range(k)]

left , right = 1, max(lans)

print(binary_search(lans, target, left, right))

