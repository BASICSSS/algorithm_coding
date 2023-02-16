from collections import Counter

def math_print(nums):
    nums.sort()
    num_counter = Counter(nums)
    common_num = num_counter.most_common(2)

    nums_len = len(nums) ##이렇게 안하면 시간초과 가능성?
    print(int(round(sum(nums)/N)))
    print(nums[int(N/2)])
    
    if N == 1:
        print(common_num[0][0])
    else:
        if common_num[0][1] == common_num[1][1]:
            print(common_num[1][0])
        else:
            print(common_num[0][0])

    print(max(nums) - min(nums))

N = int(input())
nums = [ int(input()) for _ in range(N)]
math_print(nums)


    


