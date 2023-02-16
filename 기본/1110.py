N = int(input())  #입력받은 값을 int로 바꿈
num = N           #변하는 값
count = 0         #몇 번 사이클인지
 
while True:
    ten = num//10
    one = num %10
    next_ten = one
    next_one = (ten+one)%10
    num = next_ten *10 + next_one
    count += 1
    if(num == N):
        break
 
print(count)

