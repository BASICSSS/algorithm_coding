a, b = map(int, input().split())

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)

# print(gcd(a, b))
# print(lcm(a, b))

# 내방식
def gcd(a, b):
    iter = 0
    gcd_result = 0
    while min(a, b) >= iter:
        iter += 1
        if a % iter == 0 and b % iter == 0: #뒤에서 부터 가서 연산횟수를 줄일 수도 있겠다.
            gcd_result = iter
    return gcd_result

def lcm(a, b):
    return a*b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

#연순으로 탐색해서 횟수 줄이기
# a, b = map(int, input().split())

# def gcd(a,b):
#     i = min(a,b)
#     while i>=1:
#         if a%i==0 and b%i==0:
#             return i
#         i -= 1
        
# def lcm(a,b):
#     return a*b// gcd(a,b)

# print(gcd(a,b))
# print(lcm(a,b))

#유클리드 호제법!
def gcd(a, b):
    while b > 0 :#0이 되었을 때가 최소공배수가됨
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b // gcd(a, b)

# math 라이브러리

import math
print(math.gcd(a, b))
print(math.lcm(a, b))

