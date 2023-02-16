import sys
input = sys.stdin.readline

answer = set()

for _ in range(10):
    n = int(input())
    answer.add(n%42)
    
print(len(answer))
    
    
# print(dir(set))
