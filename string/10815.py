import sys

input = sys.stdin.readline

n = int(input())
card = set(map(int, input().split()))

m = int(input())
m_card = list(map(int, input().split()))

for i in m_card:
    if i in card:
        print(1, end=" ")
    else:
        print(0, end=" ")
