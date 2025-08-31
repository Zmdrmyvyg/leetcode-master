# 空间换时间！用dict记录
def TwoSum(nums, target):
    seen = {} # 字典
    com_i = -1
    for i in len(nums):
        complement = target - nums[i]
        if complement in seen:
            com_i = seen[complement]
            return (i, com_i)
        seen[nums[i]] = i