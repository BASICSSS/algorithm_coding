import sys
input = sys.stdin.readline

n1 = int(input())
n2 = input().rstrip()

for i in n2[::-1]:
    print(n1 * int(i))
    
print(n1 * int(n2))