# 滑动窗口，右边界遍历，左边界当这次满足条件时才试探性移动（while）
# 注意移动时机，把运算都做完了再移
# 这题很难

import sys
import math

def getMaxProduct(arr):
    n = len(arr)
    m = len(arr[0])
    # TODO: 在这里实现算法
    
    must = (m+1) // 2  # 每行至少m/2，向上取整
    # print(must)

    #. 拉平arr
    arr_flat = []
    for i in range(n):
        for elem in arr[i]:
            arr_flat.append((elem,i))
    arr_flat.sort() # sort()可以排序！！！由小到大
    # print(arr_flat)

    # 滑动窗口：找能满足must要求的最小窗口
    left = 0
    count_row = [0]*n

    min_cost = arr_flat[m*n-1][0] * len(arr_flat)
    max_product = 0

    # 滑动窗口的逻辑：右边界由小到大，左边界只在这次满足要求时才移动，长度为right-left+1
    for right in range(len(arr_flat)):
        _, row = arr_flat[right]
        count_row[row] += 1 # 一个数组，记录当前窗口中每row的数量
        while left <= right:  # 所以一定要用while写！
            # for k in range(n):
            #     if all(count_row[k] >= must):
            #         flag = 1
            if all(count_row[k] >= must for k in range(n)) == 0:
                break  # 如果left小都不满足，left变大更不满足
            cost = arr_flat[right][0] - arr_flat[left][0]

            if cost < min_cost:
                min_cost = cost
                max_product = cost * (right - left + 1)
            elif cost == min_cost:
                max_product = max(max_product, cost * (right - left + 1))

            _, row = arr_flat[left]
            count_row[row] -= 1
            left += 1

    return max_product


if __name__ == "__main__":
    n, m = 2, 3
    arr = [[1, 5, 7], [3, 9, 11]]
    print(getMaxProduct(arr))