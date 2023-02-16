from collections import Counter

def std(nums):
    nums.sort()
    nums_count = Counter(nums)
    commons = nums_count.most_common()
    return commons[0][0]
    
    # for i in range(len(commons) - 1):
    #     if commons[i][1] == commons[i+1][1]:
    #         tmp = commons[i][0]
    #     else:
    #         tmp = commons[i][0]
    #         break
    # return tmp


N = int(input())
nums = [ int(input()) for _ in range(N)]
print(std(nums))