import sys
input = sys.stdin.readline
chas = list(map(int, input().split()))

for i in range(6):
    if i <= 1:
        print(1-chas[i], end=" ")
    if i >= 2 and i <= 4:
        print(2-chas[i], end=" ")
    if i == 5:
        print(8-chas[i], end=" ")