import sys

a, b = map(int, input().split())

def reverse(a, b):
    return max(str(a)[::-1], str(b)[::-1])

print(reverse(a, b))