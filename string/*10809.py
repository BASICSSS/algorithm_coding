import sys
input = sys.stdin.readline

word = input().rstrip()

answers = [-1] * 26

for i in range(len(word)):
    idx = ord(word[i]) - 97
    if answers[idx] == -1:
        answers[idx] = i
        
for answer in answers:
    print(answer , end=" ")

# 선생님 코드
import sys
input = sys.stdin.readline

word = list(input().rstrip())

alphas = "abcdefghijklmnopqrstuvwxyz"

answers = []

for alpha in alphas:
    if alpha in word:
        answers.append(word.index(alpha))
    else:
        answers.append(-1)

for answer in answers:
    print(answer, end=" ")
    
    
# dict 풀이

import sys
input = sys.stdin.readline
word = input().rstrip()
dic = dict()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(word)):
    if word[i] not in dic.keys():
        dic[word[i]] = i
        
for i in alpha:
    if i in word:
        print(str(dic[i]), end =" ")
    else:
        print("-1", end=" ")