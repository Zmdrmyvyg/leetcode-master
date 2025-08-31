from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0  # 记录当前能到达的最远位置
        n = len(nums)
        
        for i in range(n):
            if i > maxReach:  # 如果当前位置超过了能到达的最远位置
                return False
            maxReach = max(maxReach, i + nums[i])  # 根据当前位置的值更新maxreach
        
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))  # True
    print(s.canJump([3, 2, 1, 0, 4]))  # False