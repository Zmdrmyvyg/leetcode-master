# map的用法
def getUnexpiredTokens(time_to_live, queries):
    map = {}  # user -> expire_time
    result = []

    for query in queries:
        parts = query.split()  # 含有三个部分
        action = parts[0]

        if action == "generate":
            user = parts[1]
            cur_time = int(parts[2])  # 注意有数学含义的东西要存成int
            map[user] = cur_time + time_to_live
        if action == "renew":
            user = parts[1]
            cur_time = int(parts[2])  # 注意有数学含义的东西要存成int
            if user in map and map[user] > cur_time:  # map的使用方法
                map[user] = cur_time + time_to_live
        if action == "count":
            cur_time = int(parts[1])  # 注意有数学含义的东西要存成int
            i = 0
            for user in map:
                if map[user] > cur_time:
                    i += 1
            # print(i)
            result.append(i)
    return result


time_to_live = 5
queries = [
    "generate aaa 1",
    "renew aaa 2",
    "count 6",
    "generate bbb 7",
    "renew aaa 8",
    "renew bbb 10",
    "count 15"
]

print(getUnexpiredTokens(time_to_live, queries))  
# 输出: [1, 0]