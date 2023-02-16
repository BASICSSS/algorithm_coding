import sys
input = sys.stdin.readline

hour, minute = map(int, input().split())
num = int(input())

target = minute + num
hours = target//60
targets = target%60
hh = hour + hours

if target >= 60:
    if (hour+hours) >= 24:
        print(str(hh-24)+" "+str(targets))
    else:
        print(str(hh)+" "+str(targets))
else:
    print(str(hour)+" "+str(target))