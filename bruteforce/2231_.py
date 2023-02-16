import sys

N = int(sys.stdin.readline())

result = 0 #생성자 없는 경우를 고려해서 새로운 변수만들어서 아예 초기값이 정해주고 해당 변수에 저장해서 출력
for i in range(1, N + 1):
    sep_n = list(map(int, str(i)))
    if (i + sum(sep_n)) == N:
        result = i
        break
    
print(result)
    