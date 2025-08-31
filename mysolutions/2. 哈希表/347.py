from typing import List
from collections import defaultdict

def topKFrequent(nums, k):
    frequents = defaultdict(int)  # map的不定长初始化，会自动扩展
    # print(frequents)
    for i in nums:
        frequents[i] += 1

    # 如果对这个map按value排序的话，就不满足题目的时间复杂度要求
    # 所以只能用桶，[[出现了i次的数字们],[]]
    n = len(nums)
    buckets = [[] for _ in range(n+1)]
    for num, freq in frequents.items():
        buckets[freq].append(num)

    result = []
    for freq in range(n, 0, -1):  # 倒序遍历
        if buckets[freq]:
            result.extend(buckets[freq])  # 用extend的话是一个个元素加进去的，append是一坨
            if len(result) >= k:
                return result[:k]


if __name__ == "__main__":
    # 示例 1
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))  # 期望输出: [1,2]

    # 示例 2
    nums = [1]
    k = 1
    print(topKFrequent(nums, k))  # 期望输出: [1]