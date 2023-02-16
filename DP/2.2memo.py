import sys
import heapq

## 최소힙
# n = int(sys.stdin.readline())
# dq = [int(input()) for _ in range(9)]
# heap = []
# result = []
# for i in dq:
#     if i !=0:
#         heapq.heappush(heap,i)
#     else:
#         if not heap:
#             result.append(0)
#         else:
#             result.append(heapq.heappop(heap))

# for i in result:
#     print(i)

## 최대힙 튜플형태로 우선순위와 데이터를 분리해서 구성해주면 됨!
n = int(sys.stdin.readline())
dq = [int(input()) for _ in range(n)]

heap = []
result = []
for i in dq:
    if i != 0:
        heapq.heappush(heap, (-i, i))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

#why시간초과?



