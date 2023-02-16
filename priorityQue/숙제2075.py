import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
pq = []

for _ in range(n):
    nums = list(map(int, input().split()))# 12 7 9 15 5
    
    if not pq:
        for num in nums:
            heappush(pq, num)
    else:
        for num in nums:
            if num > pq[0]:
                heappop(pq)
                heappush(pq, num)


print(pq[0])
        
        
# 강이 코드 
# import sys
# import heapq
# N = int(sys.stdin.readline())

# heap =[]

# for i in range(N):
#     line = list(map(int, input().split())) # 12 7 9 15 5 => 5 ~~   5 -> 13
#                                            # 13 8 11 19 6
#     if not heap:
#         for num in line:
#             heapq.heappush(heap, num)
#     else:
#         for num in line:
#             if heap[0] < num:
#                 heapq.heappush(heap, num)
#                 heapq.heappop(heap)

# print(heapq.heappop(heap))