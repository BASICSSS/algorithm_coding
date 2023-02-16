import sys
input = sys.stdin.readline

n = int(input())
words = list(map(int, input().split()))

m = int(input())
word = list(map(int, input().split()))

for i in word:
    if i in words:
        print(words.count(i), end = " ")
    else:
        print(0, end= " ")
        

# 정답1
import sys
input = sys.stdin.readline

N = int(input())
cards = sorted([*map(int, input().split())])
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def binarySearch(arr, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid+1, end)
    else:
        return binarySearch(arr, target, start, mid-1)
    
for target in candidate:
    print(binarySearch(cards, target, 0, len(cards)-1), end=" ")
    
# 정답2
import sys
input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candidate:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
        

# 딕셔너리로 풀어보기
n = int(input())
arr1 = list(map(int, input().split()))

dict1 = dict()
# 숫자카드와 개수를 딕셔너리에 담기
for i in arr1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1


m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in dict1:
        print(dict1[i], end=' ')    # 존재하는 숫자 카드라면
    else:
        print(0, end=' ')           # 존재하지 않는 숫자 카드라면
        
# 내코드로 만들기
import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
m = int(input())
card = list(map(int, input().split()))

for i in card:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")
        
        
from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
keys = list(map(int, input().split()))

card_counter = Counter(cards)
i = 0
while i < m:
    print(card_counter[i])
    i += 1