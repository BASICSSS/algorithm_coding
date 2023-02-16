# import sys
# input = sys.stdin.readline

# words = input().rstrip().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x)
#     cnt_list.append(cnt)  # count 숫자를 리스트에 append

# if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#     print(unique_words[max_index])

from collections import Counter
alpha = input().upper()
alpha_counter = Counter(alpha)

most_common_words = alpha_counter.most_common(2)

if len(most_common_words) < 2:
    print(most_common_words[0][0])
elif most_common_words[0][1] == most_common_words[1][1]:
    print("?")
else:
    print(most_common_words[0][0])