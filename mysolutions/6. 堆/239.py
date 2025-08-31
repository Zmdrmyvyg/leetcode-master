from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TODO: 在这里写你的代码
        dq = deque()  # 队列
        result = []

        for i,num in enumerate(nums):  #下标i，值是num
            while dq and nums[dq[-1]] < num:  # 来了新的num,把队列（存的是i）里比它小的都删掉
                dq.pop()

            dq.append(i)
            
            if dq[0] <= i-k:  # 失效了，弹出
                dq.popleft()
            
            if i >= k-1:  #移动到i=k-1开始，窗口开始判断最大数。将最大的加入result
                result.append(nums[dq[0]])

        return result
        pass


# --------- 测试用例 -------------
if __name__ == "__main__":
    # 示例 1
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))  # 期望输出: [3,3,5,5,6,7]

    # 示例 2
    nums = [1]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))  # 期望输出: [1]

    # 示例 3
    nums = [1,-1]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))  # 期望输出: [1,-1]

    # 示例 4
    nums = [9,11]
    k = 2
    print(Solution().maxSlidingWindow(nums, k))  # 期望输出: [11]

    # 示例 5
    nums = [4,-2]
    k = 2
    print(Solution().maxSlidingWindow(nums, k))  # 期望输出: [4]