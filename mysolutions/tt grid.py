n, m = map(int, input().split())

def count_path(n, m):
    dp = [[0]*(m+1) for _ in range(n+1)]  # 创建一个(n+1, m+1)的grid
    # print(dp)

    # 定义边界为1
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(m+1):
        dp[0][i] = 1
    
    # print(dp)
    
    #计算
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # print(dp)
    
    return dp[n][m]

print(count_path(n,m))
# print(n, m)