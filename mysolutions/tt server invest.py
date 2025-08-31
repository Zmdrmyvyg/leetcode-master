def maxUpgradedServers(num_servers, money, sell, upgrade):
    n = len(num_servers)
    result = [0] * n
    
    for i in range(n):
        servers = num_servers[i]
        funds = money[i]
        upgrade_cost = upgrade[i]
        sell_value = sell[i]
        
        # TODO: 在这里写你自己的逻辑
        # 算出第 i 个网络最多能升级多少台服务器
        # 并把答案存到 result[i]
        max_up = 0
        for j in range(servers + 1):
            if upgrade_cost * j - sell_value * (servers - j) <= funds:
                max_up = j

        result[i] = max_up
        
    return result


# 示例测试
if __name__ == "__main__":
    num_servers = [4, 3]
    money = [8, 9]
    sell = [4, 2]
    upgrade = [4, 5]
    
    print(maxUpgradedServers(num_servers, money, sell, upgrade))  # 期望输出 [3, 2]