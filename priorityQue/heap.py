from heapq import heappush, heappop, heapify

# print(dir(heapq))

pq = []
heappush(pq, 2)
print(pq)

heappush(pq,3)
print(pq)

heappush(pq, 1)
print(pq)

print(heappop(pq), pq)

pq = [3, 5, 1, 2, 7, 4, 8]
heapify(pq)
print(pq)

# 최대힙 구현 방법(heapq는 최소힙이다)
pq = []

# heappush(pq, (priority, data))
heappush(pq, (-2, 2))
print(pq)

heappush(pq, (-3, 3))
print(pq)

heappush(pq, (-1, 1))
print(pq)

print(heappop(pq), pq)

result = heappop(pq)
print(result)
print(result[1], pq)

priority, data = heappop(pq)
# print(priority)
print(data)