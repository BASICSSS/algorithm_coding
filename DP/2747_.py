import sys

## 이건 1초 이상으로 시간초과가 나올것이다.
# def fibo(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibo(num-1) + fibo(num-2)

# n = int(input())
# print(fibo(n))


# DP
def fibo(num):
    memo = [0,1]
    for i in range(2, num+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[num]

n = int(input())
print(fibo(n))
