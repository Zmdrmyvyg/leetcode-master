from typing import List

class UnionFind:
    def __init__(self, n: int):
        # 每个节点的父亲一开始是自己
        self.parent = list(range(n + 1))

    def find(self, x: int) -> int:
        # 将每个节点直接对应到根节点
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # 返回 False 表示 x 和 y 已经在一个根上，也就是说这条边是多余的，可删除
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.parent[rootY] = rootX  # 一条边的两个节点不在一个根上，则把一个的根改成另一个
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u, v):  # union返回false的情况，删边
                return [u, v]
        return []


# 测试
if __name__ == "__main__":
    edges1 = [[1, 2], [1, 3], [2, 3]]
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

    s = Solution()
    print(s.findRedundantConnection(edges1))  # [2, 3]
    print(s.findRedundantConnection(edges2))  # [1, 4]