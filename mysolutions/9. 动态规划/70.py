class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # 本质是个费伯拿切
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    # 示例测试
    print(sol.climbStairs(2))  # 输出 2
    print(sol.climbStairs(3))  # 输出 3
    print(sol.climbStairs(4))  # 输出 5