# 以a[i]为结尾的sublist,要不是前面的某子集+a[i]，要不只有a[i]
def MaxSubArray(nums):
    cur_sum = nums[0]
    max_sum = nums[0]

    for i in range(1,len(nums)):
        if cur_sum + nums[i] >= nums[i]:
            cur_sum += nums[i]
        else:
            cur_sum = nums[i]
        
        if cur_sum > max_sum:
            max_sum = cur_sum
        
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(MaxSubArray(nums))