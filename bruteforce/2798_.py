import sys
import itertools

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

result = []
for i in itertools.combinations(card_list, 3):
    if sum(i) <= M:
        result.append(sum(i))

print(max(result))
