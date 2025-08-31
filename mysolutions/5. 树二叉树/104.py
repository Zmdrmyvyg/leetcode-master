# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # 到叶子节点之后一层，为0
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            depth = max(left_depth, right_depth) + 1
            return depth
        pass


# --------- 测试用例转换工具 -------------
def list_to_btree(lst):
    """
    将列表转换为二叉树，按照层序遍历顺序，None 表示空节点
    """
    if not lst:
        return None
    nodes = [TreeNode(x) if x is not None else None for x in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    # 示例
    lst = [3,9,20,None,None,15,7]
    root = list_to_btree(lst)
    print(Solution().maxDepth(root))  # 期望输出: 3