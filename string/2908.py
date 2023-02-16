# import sys
# input = sys.stdin.readline

# num1, num2 = input().split()
# num1 = int(num1[::-1])  # [::-1] : 역순
# num2 = int(num2[::-1])

# if num1 > num2:
#     print(num1)
# else :
#     print(num2)


a, b = input().split()

a = a[::-1]
b = b[::-1]

a.join("")
b.join("")

if int(a) > int(b):
    print(a)
else:
    print(b)