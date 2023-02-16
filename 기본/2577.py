A = int(input())
B = int(input())
C = int(input())
result = list(str(A * B * C))


i = 0
while i <= 9:
    cnt = result.count(str(i))
    print(cnt)
    i += 1
   