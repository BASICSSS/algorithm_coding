n = int(input())
cnt = 0

for i in range(1, n+1):
	if i <= 99:
		cnt += 1
	else:
		k = list(map(int, str(i)))
		if k[0] - k[1] == k[1] - k[2]:
			cnt += 1

print(cnt)

# 99보다 작고 1보다 큰 모든 수는 한수에 포함하고 99보다 큰 수는 str형으로 각 자리를 나누어 비교하여 등차수열인지 파악한다.
# else: 에서 k[0] - k[1] == k[1] - k[2]로 하는 이유는 n의 값은 1000보다 작은 자연수이므로 위 처럼 비교하면 된다.


import sys
input = sys.stdin.readline

N = int(input())

cnt = 0

for x in range(1,n+1):
    if x <= 99:
        cnt += 1
    elif x == 1000:
        pass
    else:
        str_x = str(x)
        if int(str_x[0]) - int(str_x[1]) == int(str_x[1]) - int(str_x[2]):
            cnt += 1
            

print(cnt)