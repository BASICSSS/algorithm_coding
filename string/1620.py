import sys
input = sys.stdin.readline
n, m = map(int, input().split())

id = {}
name = {}
for i in range(1, n + 1):
    pokemon = input().rstrip()
    id[i] = pokemon
    name[pokemon] = i

for _ in range(m):
    quest = input().rstrip()
    if pokemon.isdigit():
        print(id[int(quest)])
    else:
        print(name[quest])