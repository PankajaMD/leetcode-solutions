# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def order(self, node: TreeNode, level: int) -> None:
        if len(self.ans) == level:
            self.ans.append([])
        self.ans[level].append(node.val)
        if node.left is not None:
            self.order(node.left, level + 1)
        if node.right is not None:
            self.order(node.right, level + 1)

    
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return self.ans

        self.order(root, 0)
        return self.ans
